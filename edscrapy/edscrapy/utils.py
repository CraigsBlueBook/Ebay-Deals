def iextract(value, index=0):
    try:
        return value[index]
    except:
        return ""
def istrip(value):
    try:
        return value.strip()
    except:
        return value