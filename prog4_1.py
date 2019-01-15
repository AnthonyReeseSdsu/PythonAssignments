def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def Tokenize(str):
    correctTokens = ['push', 'pop', 'add', 'sub', 'mul', 'div', 'mod', 'skip', 'save', 'get']
    tokens = []

    wrong = [x for x in str.split() if not (x in correctTokens or isNumber(x))]
    if len(wrong) != 0:

        raise ValueError("Unexpected token: " + wrong[0])
   
    tokens = str.split()

    return tokens


def Parse(tokens):
    soloTokens = [ 'add', 'sub', 'mul', 'div','pop', 'mod', 'skip']
    duoTokens = ['push', 'get', 'save']

    if tokens[0] in soloTokens and len(tokens) != 1:
        raise ValueError("Parse error: " + ' '.join(str(x) for x in tokens))
    elif tokens[0] in duoTokens:
        if len(tokens) != 2 or not isNumber(tokens[1]):

            raise ValueError("Parse error: " + ' '.join(str(x) for x in tokens))

    return(True)

