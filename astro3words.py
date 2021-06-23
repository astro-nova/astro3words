import what3words

# Connects to the what3words API using a public key (limited usage!!)
geocoder = what3words.Geocoder("6WEY7C3R")


def coords_to_words(ra, dec):
    """
    Given RA, Dec of the object, return its "What 3 words" coordinate string.

    Args:
        ra (float): Right Ascension of the object [degrees]
        dec (float): Declination of the object [degrees]

    Returns:
        str: 3-word string delimited by periods corresponding to this coordinate.
    """

    # TODO
    # 1. Catch exceptions if ra is outside (0, 360) range or dec outside (-90, 90)
    # 2. Accept different types of coordinate inputs: hms:dms string, different coord systems,
    # or Astropy SkyCoord objects

    if ra > 180: ra -= 360
    res = geocoder.convert_to_3wa(what3words.Coordinates(dec, ra))
    return res['words']

def words_to_coords(words):
    """
    Given three words, return the RA and dec coordinates of an object.

    Args:
        words (str): a string in the format "word1.word2.word3"

    Returns:
        tuple(float, float): Right ascension and declination of the object 
    """

    # TODO
    # Need to check here that the three words are given in the format "word1.word2.word3"
    # Need to catch exceptions as well

    res = geocoder.convert_to_coordinates(words)
    coords = res["coordinates"]
    ra, dec = coords["lng"], coords["lat"]
    if ra < 0: ra += 180
    return ra, dec