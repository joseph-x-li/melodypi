from mido import MidiFile, merge_tracks

def analyze(mid, transpose=True, wrap=True, merge=False):
    """Analyze a midi file to play better on a melodica with only 37 notes.
    
    Only notes 2F(53) => 5F(89) are playable.
    
    The provided file must not contain extraneous tracks.

    Args:
        mid (mido.MidiFile): MIDI file to analyze
        transpose (bool, optional): Allow transposition of all tracks to fit melodica range. Defaults to True.
        wrap (bool, optional): After transposition (if it was enabled), 
            wrap them to the closest playable octave. 
            For example, (-1G, 0G, 1G) => 2G. Defaults to True.
        merge (bool, optional): Merge separate tracks together. Defaults to False.
    """
    
    if transpose:
        tracksums = [0 for _ in range(128)]
        print(f"Scanning...")
        for i, track in enumerate(mid.tracks):
            print(f"Track {i}: {track.name}")
            for msg in track:
                if msg.type in ('note_on', 'note_off'):
                    tracksums[msg.note] += 1
        
        totalevents = sum(tracksums)

        print(f"Scanned {totalevents} note events")

        running = 0
        prefixes = []
        for x in tracksums:
            prefixes.append(running)
            running += x
            
        assert running == totalevents
        answer, answercoverage = None, None
        for t in range(128 - 37):
            left = prefixes[t]
            right = prefixes[t + 37] if t < (128 - 37) else running
            coverage = right - left
            if answer is None or coverage >= answercoverage:
                answercoverage, answer = coverage, t
        realtranspose = 53 - answer
        print(f"Transposing...")
        for i, track in enumerate(mid.tracks):
            print(f"Track {i}: {track.name}")
            for msg in track:
                if msg.type in ('note_on', 'note_off'):
                    msg.note += realtranspose
                    
        print(f"Transposed tracks {'up' if realtranspose > 0 else 'down'} by {abs(realtranspose)} semitones")
                    
    if wrap:
        llimit, rlimit = 53, 89
        wrappedup = wrappeddn = 0
        print("Wrapping...")
        for i, track in enumerate(mid.tracks):
            print(f"Track {i}: {track.name}")
            for msg in track:
                if msg.type in ('note_on', 'note_off'):
                    if msg.note < llimit:
                        diff = llimit - msg.note
                        msg.note += 12 * ((diff - 1) // 12 + 1)
                        wrappedup += 1
                        
                    if msg.note > rlimit:
                        diff = msg.note - rlimit
                        msg.note -= 12 * ((diff - 1) // 12 + 1)
                        wrappeddn += 1
                        
        print(f"{wrappedup} note events were wrapped up")
        print(f"{wrappeddn} note events were wrapped down")
        
    if merge:
        mid.tracks.append(merge_tracks(mid.tracks))
        del mid.tracks[:-1]

    return mid
    
    
        
    
#     fig, ax = plt.subplots()
#     ax.bar(range(128), cnt)
#     ax.set_title("Note Frequencies")
#     ax.set_xlabel("Note")
#     ax.set_ylabel("Occurances")
#     ax.set_xticks(range(128))
#     ax.set_xticklabels([note2beep(x) for x in range(128)])
#     plt.show()