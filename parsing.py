# https://github.com/vishnubob/python-midi
# https://github.com/bspaans/python-mingus

import mido, time
from mido import MidiFile

mid = MidiFile('./door.mid')


def note2beep(note):
    oct, note = divmod(note, 12)
    

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    print(type(track))
    for msg in track:
        print(msg)

    # ['_setattr', 'bin', 'bytes', 'channel', 'copy', 'dict', 'from_bytes', 'from_dict', 'from_hex', 'from_str', 'hex', 'is_meta', 'is_realtime', 'note', 'time', 'type', 'velocity']