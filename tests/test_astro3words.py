from astro3words import coords_to_words
import what3words
import numpy as np

def test_coords_to_words():
    """
    Tests conversion of (ra, dec) coordinates to 3 words 
    with some edge coordinate cases.
    """

    ra_list = [0, 1.1, 90, 180, 360, 195.5]
    dec_list = [-90, -89.9, 0, 89.9, 90]

    for ra in ra_list:
        for dec in dec_list:
            words = coords_to_words(ra, dec)
            assert isinstance(words, str)

