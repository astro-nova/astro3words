from astro3words import coords_to_words, words_to_coords
import what3words
import pytest
import numpy as np

def test_coords_to_words():
    """
    Tests conversion of (ra, dec) coordinates to 3 words 
    with some edge coordinate cases.
    """

    ra_list = [0, 90, 180, 360, 195.5]
    dec_list = [-90, 0, 89.9, 90]

    for ra in ra_list:
        for dec in dec_list:
            words = coords_to_words(ra, dec)
            assert isinstance(words, str)

def test_words_to_coords():
    """
    Tests backwards conversion: find 3 words for a list
    of coordinates, then make sure that these words
    map to the same coordinates within 1" precision.
    """

    ra_list = [0, 90, 180, 360, 195.5]
    dec_list = [-90, 0, 89.9, 90]
    precision = 1/3600

    for ra in ra_list:
        for dec in dec_list:
            words = coords_to_words(ra, dec)
            ra_out, dec_out = words_to_coords(words)

            # Calculate angular distance
            ra_diff = ra - ra_out 
            dec_diff = dec - dec_out
            if ra_diff > 180: ra_diff -= 360 # Wrap around between 0 and 360

            # Use small-angle approx of angular distance
            dist2 = ((ra_diff * np.pi / 180)**2 * 
                    np.cos(dec * np.pi/180)**2 +
                    (dec_diff*np.pi/180)**2)
            dist = np.sqrt(dist2)
            assert dist < precision

test_words_to_coords()