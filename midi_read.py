"""
Hannes Reindl
Generating m-code from MIDI files
Latest Change: 11.04.2021
"""

import mido


def midi_to_note(midi_note):

        #A0 correspond to midi note 21
        A0 = 21

        if midi_note < A0:
                raise ValueError(f"midi notes below {A0} are not supported")

        if midi_note > 127:
                raise ValueError("midi notes above 127 are not supported")

        note_map = {
                0: "A",
                1: "A#",
                2: "B",
                3: "C",
                4: "C#",
                5: "D",
                6: "D#",
                7: "E",
                8: "F",
                9: "F#",
                10: "G",
                11: "G#",
        }

        notes_per_octave = len(note_map)
        #the notes are cyclic with length 12, thus we can use the modulo operator to get the note in the octave
        note = note_map[(midi_note - A0)%notes_per_octave]

        #to get the octave in which it should be played, use integer division and add it it to the correct position in the string

        note = note[:1] + str(midi_note//notes_per_octave - 1)  + note[1:]

        return note




        


def main():

        mid = mido.MidiFile("entchen.mid")

        # for i in range(55,257):
        #         print(f"{i}: ", end ="")
        #         print(midi_to_note(i))



        # print(mid)

        for msg in mid:
                # if msg.type == 'note_on' or msg.type == 'note_off':
                if msg.type == 'note_on':
                        print(midi_to_note(msg.note))



if __name__ == "__main__":
        main()