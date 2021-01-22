from geo import GeoPosition

class State:
  """Represent a state, including geographic information."""

  def __init__(self, code, boundaries):
    self._code = code
    self._boundaries = []
    for b in boundaries:
      self._boundaries.append( tuple(GeoPosition(lat,long) for (lat,long) in b) )
    self._centroid = self._computeCentroid()

  def abbrev(self):
    """Return the two letter abbreviation for the state."""
    return self._code

  def centroid(self):
    """Return a GeoPosition that represents the centroid of the state."""
    return self._centroid

  def numBoundaries(self):
    """Return the number of distinct boundaries defining the state."""
    return len(self._boundaries)

  def getBoundary(self, index):
    """Return a tuple of GeoPositions defining the boundary of given index."""
    return self._boundaries[index]

  def _computeCentroid(self):
    """Compute and return the centroid of the state upon initialization."""
    # First, for each individual boundary we compute its area and centroid
    # (Note: we will be loose and treat the geopositions as planar for this computation)
    results = []
    for b in self._boundaries:
      cx = cy = a = 0
      for k in range(len(b)):
        # consider point k and the one before it (knowing that -1 maps to last point)
        temp = (b[k-1].longitude() * b[k].latitude() - b[k].longitude() * b[k-1].latitude())
        a += temp
        cx += temp * (b[k-1].longitude() + b[k].longitude()) 
        cy += temp * (b[k-1].latitude() + b[k].latitude())
      if a != 0:
        a *= 0.5
        cx /= (6*a)
        cy /= (6*a)
        a = abs(a)
        results.append( (cy,cx,a) )

    # For states that have two or more pieces, we compute a composite centroid as a
    # weighted average
    if len(results) > 1:
      cy = sum( results[k][0]*results[k][2]  for k in range(len(results)) )
      cx = sum( results[k][1]*results[k][2]  for k in range(len(results)) )
      total = sum( entry[2] for entry in results )
      geo = GeoPosition(cy/total, cx/total)
    else:
      geo = GeoPosition(results[0][0], results[0][1])
    return geo
  
def load_states():
  """Return a dictionary mapping two-letter state abbreviations to State instaces for the US."""
  from us_states import us_states
  return [State(k,v) for k,v in us_states.items() if k != 'PR']   # ignore Puerto Rico
