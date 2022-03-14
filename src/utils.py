
def readInput(file):
    dct = {}
    with open(file) as f:
        for line in f:
            try:
                key, val = line.strip().replace(" ","").split(':')
                dct[key] = val
            except:
                continue
    return dct