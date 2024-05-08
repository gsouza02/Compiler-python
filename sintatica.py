from lexer import lexer


with open('ola-mundo.fpp', 'r') as file:
        code = file.read()

tokens = lexer(code)
print(tokens)