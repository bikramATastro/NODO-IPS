from astroquery.gaia import Gaia
#search for detected entries in gaia database
def gaia_query(ra, dec, rad=2.0):
    """
    

    Parameters
    ----------
    ra : float
    dec : float
    rad : float, optional
        serach radius in arc-sec. The default is 2.0.

    Returns
    -------
    list
        [gaia_ra, gaia_dec]

    """
    coord = SkyCoord(ra=ra, dec=dec, unit=(u.degree, u.degree), frame='icrs')
    radius = u.Quantity(rad, u.arcsec)
    j = Gaia.cone_search_async(coord, radius)
    r = j.get_results()
    return [r['ra'][0], r['dec'][0]]
