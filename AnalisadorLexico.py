from enum import Enum


class Categoria(Enum):
    # Identificador

    IDENTIFICADOR = {'tipo': 'IDENTIFICADOR', 'lexema': ''}

    # Constantes numericas

    CONSTANTE_INTEIRA = {'tipo': 'CONSTANTE NUMERICA', 'lexema': "constInt"}
    CONSTANTE_PONTO_FLUTUANTE = {'tipo': 'CONSTANTE NUMERICA', 'lexema': "constFloat"}

    # Caractere

    CARACTERE_SIMPLES = {'tipo': 'CARACTERE', 'lexema': ''}

    # Cadeia de caracteres

    CADEIA_CARACTERES = {'tipo': 'CADEIA DE CARACTERES', 'lexema': ''}

    # Booleano

    # Ja definido nas palavras reservadas os possiveis valores para
    # o tipo de dado booleano

    # Palavras reservadas da linguagem

    TIPO_INTEIRO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'int'}
    TIPO_PONTO_FLUTUANTE = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'float'}
    TIPO_CARACTERE = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'char'}
    TIPO_BOOLEANO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'bool'}
    TIPO_CADEIA_CARACTERES = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'string'}
    VALOR_VERDADEIRO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'TRUE'}
    VALOR_FALSO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'FALSE'}
    OPERADOR_NEGACAO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'not'}
    OPERADOR_CONJUNCAO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'and'}
    OPERADOR_DISJUNCAO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'or'}
    COMANDO_IF = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'if'}
    COMANDO_ELSE = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'else'}
    COMANDO_WHILE = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'while'}
    COMANDO_DO = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'do'}
    COMANDO_FOR = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'for'}
    COMANDO_INPUT = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'input'}
    COMANDO_PRINT = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'print'}
    COMANDO_FUNCTION = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'function'}
    TIPO_VOID = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'void'}
    COMANDO_RETURN = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'return'}
    COMANDO_MAIN = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'main'}
    COMANDO_INT2STRING = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'int2string'}
    COMANDO_FLOAT2STRING = {'tipo': 'PALAVRA RESERVADA', 'lexema': 'float2string'}

    # Operadores

    OPERADOR_SOMA = {'tipo': 'OPERADOR', 'lexema': '+'}
    OPERADOR_SUBTRACAO = {'tipo': 'OPERADOR', 'lexema': '-'}
    OPERADOR_MULTIPLICACAO = {'tipo': 'OPERADOR', 'lexema': '*'}
    OPERADOR_DIVISAO = {'tipo': 'OPERADOR', 'lexema': '/'}
    OPERADOR_RELACIONAL = {'tipo': 'OPERADOR', 'lexema': ''}  # vale para qualquer relacional

    # Atribuicao

    ATRIBUICAO = {'tipo': 'ATRIBUICAO', 'lexema': '='}

    # Delimitadores

    ABRE_PARENTESES = {'tipo': 'DELIMITADORES', 'lexema': '('}
    FECHA_PARENTESES = {'tipo': 'DELIMITADORES', 'lexema': ')'}
    ABRE_COLCHETES = {'tipo': 'DELIMITADORES', 'lexema': '['}
    FECHA_COLCHETES = {'tipo': 'DELIMITADORES', 'lexema': ']'}
    ABRE_CHAVES = {'tipo': 'DELIMITADORES', 'lexema': '{'}
    FECHA_CHAVES = {'tipo': 'DELIMITADORES', 'lexema': '}'}
    ASPAS_SIMPLES = {'tipo': 'DELIMITADORES', 'lexema': "'"}
    ASPAS_DUPLAS = {'tipo': 'DELIMITADORES', 'lexema': '"'}
    PONTO = {'tipo': 'DELIMITADORES', 'lexema': '.'}
    PONTO_VIRGULA = {'tipo': 'DELIMITADORES', 'lexema': ';'}
    VIRGULA = {'tipo': 'DELIMITADORES', 'lexema': ','}


class AnalisadorLexico():
    row = 0
    col = 0
    line = ""
    sourceFile = ""
    EOF = False

    def __init__(self, sourcePath):
        self.sourceFile = open(sourcePath, 'r')
        self.row = 0
        self.col = 0
        self.EOF = False
        self.newLineSource()

    def newLineSource(self):
        self.line = self.sourceFile.readline()
        self.row += 1
        self.col = 0
        if not self.line:
            # self.row -= 1
            self.EOF = True
            # print('### ( row:{},col:{}) EOF = {}'.format(self.row,self.col,self.EOF),end='\n')

    def nextElement(self):
        self.col += 1
        out = self.line[self.col]

        if self.col >= len(self.line) - 1:
            self.newLineSource()
            self.col = 0

        return out

    def increaseCol(self):
        self.col += 1;
        if self.col >= len(self.line) - 1:
            self.newLineSource()
            self.col = 0

    def decreaseCol(self):
        self.col -= 1;

    def nextToken(self):
        if self.EOF:
            return "EOF"
        self.decreaseCol()  # retornar a posição de parada, pois o ultimo caracter lido não entra no token
        currentRow = self.row
        tk = self.nextElement()
        # TODO create current row
        resultToken = ""

        while tk in [' ', "\t", "\r", "\n"]:  #
            tk = self.nextElement()
        # teste de letras

        if tk.isalpha():  # teste de identificadores e palavras reservadas
            c = self.nextElement()
            while c.isalnum() or c == '_':
                tk += c
                c = self.nextElement()



        elif tk.isnumeric():  # teste de constantes numéricas positivas
            c = self.nextElement()
            countPoint = 0
            while c.isnumeric() or c in ['.']:
                if c in ['.']:
                    countPoint += 1
                    if countPoint == 2:
                        resultToken = "Erro lexico"
                        break
                tk += c
                c = self.nextElement()
                #            if c in ['.']:


        elif tk in [">", "<", "=", "!"]:  # teste de operadores relacionais e atribuição
            c = self.nextElement()
            if c == '=':
                tk += c
                self.increaseCol()

        elif tk in ["'", '"']:
            c = self.nextElement()
            delimitador = tk[0]
            while c != delimitador:
                if c in ['\\']:  # TODO caso de aceitacao do escape

                    tk += c
                    c = self.nextElement()
                tk += c
                c = self.nextElement()
            tk += c
            self.increaseCol()

        elif tk in ['(', ')', '[', ']', '{', '}', "'", '"', ';', ',', '+', '-', '*', '/', ';']:
            # c = self.nextElement()
            self.increaseCol()
        else:
            resultToken = "Erro lexico"
            self.increaseCol()

        if resultToken == "":
            resultToken = self.idToken(tk)
        # out = '{} :( row:{},col:{}) => Token = {}'.format(tk,currentRow,self.col-len(tk), self.idToken(tk))
        out = {'name': tk, 'row': currentRow, 'col': self.col - len(tk) + 1, 'token': resultToken}
        return out

    def idToken(self, strToken):
        if strToken == '':
            return 0
        out = ''

        tipo = 0
        for op in Categoria:
            strAux = op.value['lexema']
            if strAux == strToken:
                tipo = 1
                break

        if tipo == 1:
            out = op.value;

        elif strToken in [">", "<", ">=", "<=", "==", "!="]:
            out = Categoria.OPERADOR_RELACIONAL.value

        elif strToken.lstrip('-').isdigit():
            out = Categoria.CONSTANTE_INTEIRA.value

        elif strToken.lstrip('-').replace('.', '', 1).isdigit() and strToken[len(strToken) - 1] != ['.']:
            out = Categoria.CONSTANTE_PONTO_FLUTUANTE.value

        elif strToken[0] == "'" and len(strToken) == 3:
            out = Categoria.CARACTERE_SIMPLES.value

        elif strToken[0] == '"' and len(strToken) >= 3:
            out = Categoria.CADEIA_CARACTERES.value

        elif strToken[0].isalpha:
            out = Categoria.IDENTIFICADOR.value

        else:
            out = "Erro lexico"
        return out


aL = AnalisadorLexico('programa1.txt')
tk = aL.nextToken()

while tk != "EOF":
    print(tk)
    tk = aL.nextToken()

print(tk)