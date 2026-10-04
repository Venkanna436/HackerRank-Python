def wrap(string, max_width):
    newstring = ''
    i = 0
    while i < len(string) and i + max_width < len(string):
        newstring = newstring + string[i : i + max_width] + '\n'
        i += max_width
    newstring = newstring + string[i:] + '\n'
    return newstring