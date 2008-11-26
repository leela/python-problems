"""Learning how to write generalized code.
"""

def parse_csv(f):
    """Gets the file object as input and parse all the lines and return
    """
    return [i.strip().split(',') for i in f.readlines()]
