from math import sin, cos, atan2, radians, sqrt

class GeoPosition:
  """Represents a geographic position in terms of latitude and longitude."""

  def __init__(self, latitude, longitude):
    """Initialize a GeoPosition having the given latitude and longitude."""
    self._lat = latitude
    self._long = longitude

  def __str__(self):
    """Produce a string representation of the form <latitude, longitude>"""
    return '<%8.4f, %8.4f>' % (self._lat, self._long)

  def longitude(self):
    """Return the longitude of the position."""
    return self._long

  def latitude(self):
    """Return the latitude of the position."""
    return self._lat

  def distance(self, other):
    """Return the great circle distance (in miles) between this position and another.

    Uses the "haversine" formula.
    http://en.wikipedia.org/wiki/Haversine_formula
    """
    earth_radius = 3963.2  # miles
    lat1 = radians(self._lat)
    lat2 = radians(other._lat)
    lon1 = radians(self._long)
    lon2 = radians(other._long)
    dlat, dlon = lat2-lat1, lon2-lon1
    a = sin(dlat/2) ** 2  + sin(dlon/2) ** 2 * cos(lat1) * cos(lat2)
    c = 2 * atan2(sqrt(a), sqrt(1-a));
    return earth_radius * c;

  def project(self):
    """Return an (x,y) tuple representing a planar projection of the U.S. location.

    This relies on an Albers pojection.

    Derived from Mike Bostock's Albers javascript implementation for D3
    http://mbostock.github.com/d3
    http://mathworld.wolfram.com/AlbersEqual-AreaConicProjection.html
    """
    if self._lat < 25:
      return _hawaii(self)
    elif self._lat > 51:
      return _alaska(self)
    else:
      return _lower48(self)
    

def _albers_projection(origin, parallels, translate, scale):
  """Return an Albers projection from geographic positions to x-y positions.
  
  Derived from Mike Bostock's Albers javascript implementation for D3
  http://mbostock.github.com/d3
  http://mathworld.wolfram.com/AlbersEqual-AreaConicProjection.html

  origin -- a geographic position
  parallels -- bounding latitudes
  translate -- x-y translation to place the projection within a larger map
  scale -- scaling factor
  """
  phi1, phi2 = [radians(p) for p in parallels]
  base_lat = radians(origin.latitude())
  s, c = sin(phi1), cos(phi1)
  base_lon = radians(origin.longitude())
  n = 0.5 * (s + sin(phi2))
  C = c*c + 2*n*s
  p0 = sqrt(C - 2*n*sin(base_lat))/n

  def project(position):
      lat, lon = radians(position.latitude()), radians(position.longitude())
      t = n * (lon - base_lon)
      p = sqrt(C - 2*n*sin(lat))/n
      x = scale * p * sin(t) + translate[0]
      y = scale * (p * cos(t) - p0) + translate[1]
      return (x, y)
  return project

_lower48 = _albers_projection(GeoPosition(38, -98), [29.5, 45.5], [480,250], 1000)
_alaska = _albers_projection(GeoPosition(60, -160), [55,65], [150,440], 400)
_hawaii = _albers_projection(GeoPosition(20, -160), [8,18], [300,450], 1000)
