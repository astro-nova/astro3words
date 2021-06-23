from astro3words import coords_to_words, words_to_coords
import what3words
import pytest

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
            assert ra_out == pytest.approx(ra, abs=precision)
            assert dec_out == pytest.approx(dec, abs=precision)