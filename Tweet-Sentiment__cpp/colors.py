# A fixed gradient of sentiment colors from negative (blue) to positive (red)
# Colors chosen via Cynthia Brewer's Color Brewer (colorbrewer2.com)
SENTIMENT_COLORS = [
    (49,54,149), (69,117,180), (116,173,209), (171,217,233),
    (224,243,248), (255,255,191), (254,224,144), (253,174,97),
    (244,109,67), (215,48,39), (165,0,38), ]
GRAY = (170,170,170)

def get_sentiment_color(sentiment, scale=4):
    """Returns a color corresponding to the sentiment value.

    sentiment -- a number between -1 (negative) and +1 (positive)
    """
    if sentiment is None:
        return GRAY
    scaled = (scale * sentiment + 1) / 2.0
    index = int( scaled * len(SENTIMENT_COLORS) ) # Rounds down
    if index < 0:
        index = 0
    if index >= len(SENTIMENT_COLORS):
        index = len(SENTIMENT_COLORS) - 1
    return SENTIMENT_COLORS[index]

