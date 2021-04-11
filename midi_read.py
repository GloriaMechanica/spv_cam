"""
Hannes Reindl
Generating m-code from MIDI files
Latest Change: 11.04.2021
"""

import mido
import myconstants


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



        for msg in mid:
                if not msg.is_meta:
                        print(msg)
                        

        offset = 11 #until now we only have the notes E5, F5#, G5#, A5, B5, C6#, D6# available, so to get a valid m-code offset the midi notes
        notes = list()
        time_note_played = list()
        time_pause_between_notes = list()

        for msg in mid:
                if msg.type == 'note_off':
                        time_note_played.append(round(msg.time,4))
                if msg.type == 'note_on':
                        notes.append(midi_to_note(msg.note + offset))
                        time_pause_between_notes.append(round(msg.time,4))


        file_overhead = f"#define $POSE {myconstants.POSE} \n#define $DOWN {myconstants.DOWN} \n"


        with open("entchen.mc", 'w') as my_file:
                my_file.write(file_overhead)

                                 


        

        print(notes)
        print([round(num,2) for num in time_note_played])
        print([round(num,2) for num in time_pause_between_notes])
 




if __name__ == "__main__":
        main()