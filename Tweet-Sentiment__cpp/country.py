from cs1graphics import Canvas, Text, Polygon, Drawable, Point

class _RenderedState(Drawable):

  def __init__(self, state):
    Drawable.__init__(self)
    self._label = Text(state.abbrev(), 9, Point(*state.centroid().project()))
    self._bounds = None
    self._polys = []
    for k in range(state.numBoundaries()):
      b = state.getBoundary(k)
      p = Polygon()
      for geo in b:
        x,y = geo.project()
        p.addPoint(Point(x,y))
        if x > 0:  # hack to deal with Alaska going past 180 date line
          self._bounds = _mergeBounds([x,x,y,y], self._bounds)
      self._polys.append(p)

  def _draw(self):
    for p in self._polys:
      p._draw()
    self._label._draw()

  def getBounds(self):
    return self._bounds

  def setFillColor(self, color):
    for p in self._polys:
      p.setFillColor(color)


class Country:

  def __init__(self, states, width=950):
    ratio = 0.5263
    self._canvas = Canvas(width, ratio*width)
    self._canvas.setTitle('United States')
    self._states = {}                          # map from abbrev to RenderedState
    bounds = None
    self._canvas.setAutoRefresh(False)
    for s in states:
      rendered = _RenderedState(s)
      self._canvas.add(rendered)
      self._states[s.abbrev()] = rendered
      bounds = _mergeBounds(rendered.getBounds(), bounds)
    self._canvas.zoomView(width/950.0, Point(0,0))
    self._canvas.setAutoRefresh(True)
#    self._canvas.setView(Point(bounds[0],bounds[3]), Point(bounds[1],bounds[2]))

  def setTitle(self, title):
    """Set the Canvas title to the given string."""
    self._canvas.setTitle(title)

  def setFillColor(self, stateCode, color):
    """Set the fill color of the state with given abbreviation to the indicated color."""
    if not isinstance(stateCode, str):
      raise TypeError('state code must be a string')
    if stateCode not in self._states:
      raise ValueError('unknown state code: ' + stateCode)
    self._states[stateCode].setFillColor(color)


def createUSA(width=950):
  """Create a Country instance with given width initialized with USA data."""
  from state import load_states
  states = load_states()
  usa = Country(states, width)
  return usa
  
def _mergeBounds(a, b):  # assume that one is real
  if b is None:
    return a
  else:
    return [min(a[0],b[0]), max(a[1],b[1]), min(a[2],b[2]), max(a[3],b[3])]
  

if __name__ == '__main__':
  import sys

  try:
    width = int(sys.argv[1])
  except:
    width = 950

  usa = createUSA(width)
