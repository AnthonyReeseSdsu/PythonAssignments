currentLine = 1
stack = []
value= {}

class StackMachine:
    
    def __init__(self):
        return none

    def Execute(tokens):
        global currentLine
        if tokens[0] == 'add':
            try:
                stack.append(stack.pop() + stack.pop())
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'sub':
            try:
                stack.append(stack.pop() - stack.pop())
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'mul':
            try:
                stack.append(stack.pop() * stack.pop())
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'div':
            try:
                stack.append(stack.pop() / stack.pop())
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'push':
            stack.append(int(tokens[1]))

        elif tokens[0] == 'pop':
            if len(stack) == 0:
                raise IndexError("Invalid Memory Access")
            currentLine += 1
            x = stack.pop()
            print(x)
            return x

        elif tokens[0] == 'mod':
            try:
                stack.append(stack.pop() % stack.pop())
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'skip':
            try:
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    currentLine += b
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'save':
            try:
                value[tokens[1]] = stack.pop()
            except IndexError:
                raise IndexError("Invalid Memory Access")

        elif tokens[0] == 'get':
            try:
                stack.append(value[tokens[1]])
            except IndexError:
                raise IndexError("Invalid Memory Access")

        currentLine += 1
