#Embedded file name: /Users/versonator/Jenkins/live/Binary/Core_Release_64_static/midi-remote-scripts/VCM600/MixerComponent.py
from _Framework.MixerComponent import MixerComponent as MixerComponentBase
from VCM600.TrackEQComponent import TrackEQComponent
from .TrackFilterComponent import TrackFilterComponent
from .OneButtonFXComponent import OneButtonFXComponent

class MixerComponent(MixerComponentBase):

    def __init__(self, num_tracks, session, *a, **k):
        self._session = session
        self._track_eqs = [ TrackEQComponent() for _ in xrange(num_tracks) ]
        self._track_filters = [ TrackFilterComponent() for _ in xrange(num_tracks) ]
        self._track_fx1s = [ OneButtonFXComponent('FX1') for _ in xrange(num_tracks)]
        self._track_fx2s = [ OneButtonFXComponent('FX2') for _ in xrange(num_tracks)]
        super(MixerComponent, self).__init__(num_tracks, *a, **k)
        map(self.register_components, self._track_eqs)
        map(self.register_components, self._track_filters)
        map(self.register_components, self._track_fx1s)
        map(self.register_components, self._track_fx2s)

    def track_eq(self, index):
        if not (index in range(len(self._track_eqs))): raise AssertionError
        return self._track_eqs[index]

    def track_filter(self, index):
        if not (index in range(len(self._track_filters))): raise AssertionError
        return self._track_filters[index]

    def track_fx1(self, index):
        if not (index in range(len(self._track_fx1s))): raise AssertionError
        return self._track_fx1s[index]
    
    def track_fx2(self, index):
        if not (index in range(len(self._track_fx2s))): raise AssertionError
        return self._track_fx2s[index]


    def _reassign_tracks(self):
        super(MixerComponent, self)._reassign_tracks()
        tracks = self.tracks_to_use()
        for index in range(len(self._channel_strips)):
            track_index = self._track_offset + index
            track = tracks[track_index] if len(tracks) > track_index else None
            if len(self._track_eqs) > index:
                self._track_eqs[index].set_track(track)
            if len(self._track_filters) > index:
                self._track_filters[index].set_track(track)
            if len(self._track_fx1s) > index:
                self._track_fx1s[index].set_track(track)
            if len(self._track_fx2s) > index:
                self._track_fx2s[index].set_track(track)
            self._session.log_message('Track index %s' % track_index)
            self._session.log_message('Track %s: EQ: %s, Filter: %s, FX1: %s, FX2: %s' % 
                    (track_index, self._track_eqs[index]._device, self._track_filters[index]._device, self._track_fx1s[index]._device, self._track_fx2s[index]._device))
            
            
    def tracks_to_use(self):
        return tuple(self.song().visible_tracks) + tuple(self.song().return_tracks)
            