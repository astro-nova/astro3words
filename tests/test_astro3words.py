from astro3words import coords_to_words
import what3words
import numpy as np

def test_coords_to_words():
    """
    Tests conversion of (ra, dec) coordinates to 3 words 
    with some edge coordinate cases.
    """

    ra_list = [-1.5, 0, 10, 180, 180.5, 361, np.inf]
    dec_list = [-92.1, -90, -85.3, 0, 85.3, 90.0, 91, -np.inf]

    for ra in ra_list:
        for dec in dec_list:
            words = coords_to_words(ra, dec)
            assert isinstance(words, str)

