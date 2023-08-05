from math import ceil, floor


class PdfTxtError(Exception):
    pass


def character_in_region(c, x0, y0, x1, y1):
    return c.x0 >= x0 and c.x1 <= x1 and c.y0 >= y0 and c.y1 <= y1


def fetch_left_most_coordinate(characters):
    return floor(min([c.x0 for c in characters]))


def fetch_right_most_coordinate(characters):
    return ceil(max([c.x1 for c in characters]))


def parse_float_list(text):
    """
    text: expecting a comma separated list of numbers
    optionally contained in (brackets).

    Returns a list of floats.
    """
    if text is None:
        return []

    if isinstance(text, list):
        text = text[0]

    return [float(r.strip()) for r in text.strip(")").strip("(").split(",")]
