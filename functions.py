
def length_str(text):
    if type(text) is float:
        text = ''
    return len(text.rstrip().lstrip())