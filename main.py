import sys
import time
from pyo import *

from dna_to_music import nucleotide_to_instrument
from seq_reading import sequences_in_file
from music import make_instrument

# Useful pyo example lines

# Randomly choose from a list.
# rnd = Choice(choice=freqs, freq=[3,4])
# Call after a time
# a = CallAfter(callback, 2, [300,301])
# Call repeatedly after intervals
# p = Pattern(callback, .125)

# Convert midi not to frequency
# freqs = midiToHz([60,62,64,65,67,69,71,72])

SERVER = None

seq = sequences_in_file("assets/sequences/patience_full.fasta").next()


def play_music():
    note_length = float(1.0/10)

    envelope = Adsr(attack=note_length/4,
                 decay=note_length/4,
                 sustain=note_length/4,
                 release=note_length/4,
                 dur=note_length,
                 mul=.5)

    # we want this in the outer scope
    wave = None

    def each_note():
        global wave
        nucleo = seq.next()
        instrument = nucleotide_to_instrument(nucleo)
        wave = make_instrument(instrument, env=envelope, dur=note_length)
        envelope.play()


    p = Pattern(each_note, note_length)
    p.play()

    time.sleep(100*10)


def main():
    global SERVER
    SERVER = Server()
    SERVER.boot()
    SERVER.start()

    play_music()

    SERVER.stop()
    SERVER.shutdown()
    sys.exit(0)


if __name__ == "__main__":
    main()
