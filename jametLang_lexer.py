from sly import Lexer

class leksikal(Lexer):
    tokens = { PRINT, NAME, NUMBER, STRING, IF, THEN, ELSE, FOR, FUN, TO, ARROW, EQEQ }
    ignore = '\t '

    literals = { '=', '+', '-', '/', '*', '(', ')', ',', ';' }

    PRINT = r'c3t4k'
    IF = r'j1k4'
    THEN = r'm4k4'
    ELSE = r'l41n'
    FOR = r'l00p'
    TO = r's4mp41'
    FUN = r'fun951'
    ARROW = r'-->'
    NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'
    STRING = r'\".*?\"'
    
    EQEQ = r'=='

    @_(r'\d+')
    def NUMBER(self, t):
        t.value = int(t.value)
        return t

    @_(r'#.*')
    def COMMENT(self, t):
        pass

    @_(r'\n+')
    def newline(self,t ):
        self.lineno = t.value.count('\n')


if __name__ == '__main__':
    lexer = leksikal()
    env = {}
    while True:
        try:
            text = input('j4m3t > ')
        except EOFError:
            break
        if text:
            lex = lexer.tokenize(text)
            for token in lex:
                print(token)
