from packages.support import *
from packages.ply import lex
from packages.ply import yacc

tokens = ('MUL', 'LPAREN', 'RPAREN', 'NUMBER', 'SEPERATOR')
t_MUL = 'mul'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEPERATOR = r','

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):
    t.type = 'ERROR'
    t.value = t.value[0]
    t.lexer.skip(1)
    return t

def p_error(p):
    pass

def p_mul_expression(p):
    'expression : MUL LPAREN NUMBER SEPERATOR NUMBER RPAREN'
    p[0] = p[3] * p[5]

test = load_string("input.txt")
lexer = lex.lex()
lexer.input(test)

record = False
s = ''
c = []

parser = yacc.yacc()

while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    #print(tok.type, tok.value, tok.lineno, tok.lexpos)
    if tok.type == 'MUL' and record == False:
        record = True
    elif tok.type == 'ERROR':
        record = False
        s = ''
    elif tok.type == 'RPAREN' and record == True:
        record = False
        s = s + str(tok.value)
        c.append(s)
        s = ''
        continue
    
    if record:
        s = s + str(tok.value)

t = 0
for exp in c:
    v = parser.parse(exp)
    if v:
        t += v

print(t)
