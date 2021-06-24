from numpy import deg2rad
import what3words
from typing import Tuple
from astropy.coordinates import SkyCoord
from astropy import units as u

# Connects to the what3words API using a public key (limited usage!!)
geocoder = what3words.Geocoder("6WEY7C3R")


def coords_to_words(*args, **kwargs) -> str:
    """
    Given RA, Dec of the object, return its "What 3 words" coordinate string.

    Args:
        ra (float or str): Right Ascension of the object [degrees or hms] AND
        dec (float or str): Declination of the object [degrees or dms], OR
        l (float): Galactic latitute [degrees] AND
        b (float): Galactic longitude [degrees], OR
        coord_string (str): 'XXhXXmXXs +XXdXXmXXs" string acceptable by AstroPy SkyCoord function. 
        format (str): coordinate format

    Returns:
        str: 3-word string delimited by periods corresponding to this coordinate.
    """
    # TODO
    # 1. Accept different types of coordinate inputs: hms:dms string, different coord systems,
    # or Astropy SkyCoord objects

    if ( (len(args) > 0 and isinstance(args[0], float)) or
       ("ra" in kwargs and isinstance(kwargs['ra'], float)) or
       ("l" in kwargs and isinstance(kwargs['l'], float))):
        c = SkyCoord(*args, **kwargs, unit=u.deg)
        print(c)
    else:
        c = SkyCoord(*args, **kwargs)
    c = c.transform_to('icrs')
    ra, dec = c.ra.deg, c.dec.deg

    # Check that the input is sensible
    if (ra < 0) or (ra > 360) or (dec < -90) or (dec > 90):
        raise ValueError("RA must be between 0 and 360, and Dec between -90 and 90!")
    
    # Convert ra to longitude-style (-180 < lon <180)
    if ra >= 180: ra -= 360

    # Search what3words API for the given latitude/longitude
    res = geocoder.convert_to_3wa(what3words.Coordinates(dec, ra))
    return res['words']


def words_to_coords(words:str) -> Tuple[float, float]:
    """
    Given three words, return the RA and dec coordinates of an object.

    Args:
        words (str): a string in the format "word1.word2.word3"

    Returns:
        tuple(float, float): Right ascension and declination of the object 
    """

    # Check that the input is sensible
    try:
        assert len(words.split('.')) == 3
    except:
        raise ValueError("Please pass the three word string in the format 'word1.word2.word3'.")

    # Search what3words API for the input coordinates
    res = geocoder.convert_to_coordinates(words)

    # If not found, raise an exception
    try:
        coords = res["coordinates"]
    except:
        raise ValueError("Error: these 3-word-coordinates are not found.")

    # Otherwise, return ra/dec
    ra, dec = coords["lng"], coords["lat"]
    if ra < 0: ra += 360
    return ra, dec
