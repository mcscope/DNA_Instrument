from pyo import *
import random
from nucleotides import A, C, T, G, N
from music import Instrument



def midi_sine(note):
    return Instrument(SineLoop,
                      {
                          "freq": midiToHz(note),
                          "feedback": 0.05
                      })


def midi_robot(note):
    return Instrument(SumOsc,
                      {
                          "freq": midiToHz(note),
                          "ratio": 0.7,
                      })




nucleotide_instrument = {
    A: midi_robot(80),
    T: midi_robot(84),
    G: midi_sine(60),
    C: midi_sine(65),
    N: midi_sine(75)
}


def nucleotide_to_instrument(nucleo):
    return nucleotide_instrument[nucleo]
