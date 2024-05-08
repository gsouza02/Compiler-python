# Definição das palavras reservadas e seus tokens correspondentes
reserved_words = {
    'fim' : 'FIM', 'inicio' : 'INICIO', 'retorna' : 'RETORNA', 'funcao' : 'FUNCAO', 'ou' : 'OU', 'e':'E', 
    'se' : 'IF', 'senao' : 'ELSE', 'verdade' : 'TRUE', 'mentira' : 'FALSE', 'vazio' : 'VOID', 'nulo' : 'NULL',
    'repita' : 'DO', 'enquanto' : 'WHILE', 'para' : 'FOR', 'escolha' : 'SWITCH', 'numeros' : 'INT', 
    'letra' : 'CHAR', 'palavras' : 'STRING', 'decimais' : 'FLOAT', 'logico' : 'BOOL'

}
reserved_simbols = {
    '(' : 'ABRE', ')' : 'FECHA', '+' : 'MAIS', '<' : 'MENOR', '=' : 'ATRIBUICAO', '-' : 'MENOS', '/' : 'DIV', '*' : 'VEZES',
      '!' : 'NAO', '#' : 'COMENTARIO', ',' : 'VIRGULA', '"' : 'ASPAS', '<=' : 'MENORIGUAL', '>=' : 'MAIORIGUAL', '==' : 'IGUAIS', 
      '!=' : 'DIFERENTE', '>' : 'MAIOR'
}

# Função lexer
def lexer(code):
    tokens = []
    current_token = ''
    verificaIguais = ''
    primeiroChar = ''
    segundoChar = ''

    for char in code:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                # Verifica se a palavra é uma palavra reservada
                if current_token.isdigit():
                    token_type = 'DIGIT'
                    
                else:
                    token_type = reserved_words.get(current_token, 'ID')

                tokens.append((token_type, current_token))
                current_token = ''
                
            else:
                if char != ' ':
                    if char == '<' or char == '=' or char == '>' or char == '!':
                        
                        if verificaIguais == '':
                            primeiroChar = char
                            verificaIguais += char
                        else:
                            verificaIguais += char
                            segundoChar = char
                            token_type = reserved_simbols.get(verificaIguais, 'NO')
                            
                            if token_type == 'NO':
                                token_type = reserved_simbols.get(primeiroChar, 'SIMBOLO')
                                tokens.append((token_type, primeiroChar))
                                primeiroChar = ''
                                verificaIguais = ''
                            else:
                                token_type = reserved_simbols.get(verificaIguais, 'SIMBOLO')
                                if token_type != 'SIMBOLO':
                                    tokens.append((token_type, verificaIguais))
                                primeiroChar = ''
                                verificaIguais = ''
                else:
                                token_type = reserved_simbols.get(verificaIguais, 'SIMBOLO')
                                if(token_type != 'SIMBOLO'):
                                    tokens.append((token_type, verificaIguais))
                                primeiroChar = ''
                                verificaIguais = ''
                                segundoChar = ''
                    

            if char != ' ' and char != '\n' and char != '\t' and char != '=' and char != '<' and char != '>' and char != '!': 
                token_type = reserved_simbols.get(char, 'SIMBOLO')
                tokens.append((token_type, char))

    # Verifica se há uma palavra pendente após o término do loop
    if current_token:
        if current_token.isdigit():
            token_type = 'DIGIT'
        else:
            token_type = reserved_words.get(current_token, 'ID')

        tokens.append((token_type, current_token))
    
    if primeiroChar:
        token_type = reserved_simbols.get(primeiroChar, 'SIMBOLO')
        tokens.append((token_type, primeiroChar))
        
        
    tokens.append(('EOF', 'EOF'))

    return tokens