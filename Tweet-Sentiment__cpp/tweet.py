class Tweet:
    """Represents a single Tweet, including time and location meta data."""

    def __init__(self, message, timestamp, position):
        """
        Initialize a Tweet instance.

        message - a string that includes the full body of the tweet, including hashtags
        timestamp - a datetime.datetime instance describing when the tweet was posted
        position - a GeoPosition instance describing the location of the tweet
        """
        self._msg = message
        self._time = timestamp
        self._pos = position

    def message(self):
        """Return a string that comprises the full body of the tweet."""
        return self._msg

    def timestamp(self):
        """Return a datetime.datetime instance describing when the tweet was posted."""
        return self._time

    def position(self):
        """Return a GeoPosition instance describing the location of the tweet."""
        return self._pos
    
