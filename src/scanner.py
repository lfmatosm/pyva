import ply.lex as lex

# List of token names.   This is always required
tokens = (
    'ID',         #identifier
    'NUMBER',     #0,1,2,3...
    'PLUS',       #+
    'MINUS',      #-
    'TIMES',      #*
    'DIVIDE',     #/
    'LPAREN',     #(
    'RPAREN',     #)
    'LBRACKET',   #[
    'RBRACKET',   #]
    'LKEY',       #{
    'RKEY',       #}
    'COLON',      #,
    'SEMICOLON',  #;
    'DOT',        #.
    'ATTR',       #=
    'LTHAN',      #<
    'GTHAN',      #>
    'LEQTHAN',    #<=
    'GEQTHAN',    #>=
    'EQUALS',     #==
    'NEQUALS',    #!=
    'AND',        #&
    'NOT',        #!
    'BOOLEAN',    #boolean
    'CLASS',      #class
    'EXTENDS',    #extends
    'PUBLIC',     #public
    'STATIC',     #static
    'VOID',       #void
    'MAIN',       #main
    'STRING',     #String
    'RETURN',     #return
    'INT',        #int
    'IF',         #if
    'ELSE',       #else
    'WHILE',      #while
    'PRINT',      #System.out.println
    'LENGTH',     #length
    'TRUE',       #true
    'FALSE',      #false
    'THIS',       #this
    'NEW',        #new
    'NULL'        #null
)

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LKEY = r'{'
t_RKEY = r'}'
t_COLON = r','
t_SEMICOLON = r';'
t_DOT = r'\.'
t_ATTR = r'='
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LEQTHAN = r'<='
t_GEQTHAN = r'>='
t_EQUALS = r'=='
t_NEQUALS = r'!='
t_AND = r'&&'
t_NOT = r'!'
t_BOOLEAN = r'boolean'
t_CLASS = r'class'
t_EXTENDS = r'extends'
t_PUBLIC = r'public'
t_STATIC = r'static'
t_VOID = r'void'
t_MAIN = r'main'
t_STRING = r'String'
t_RETURN = r'return'
t_INT = r'int'
t_IF = r'if'
t_ELSE = r'else'
t_WHILE = r'while'
t_PRINT = r'System.out.println'
t_LENGTH = r'length'
t_TRUE = r'true'
t_FALSE = r'false'
t_THIS = r'this'
t_NEW = r'new'
t_NULL = r'null'


# Regular expression rules with value definitions
def t_ID(t):
    r'[a-zA-Z][0-9|a-zA-Z|_]*'
    t.value = str(t.value)
    return t


def t_NUMBER(t):
    r'(0|[1-9][0-9]*)'
    t.value = int(t.value)
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
class Factorial {
    public static void main(String[] a) {
        System.out.println(new Fac().ComputeFac(10));
    }
}

class Fac {
    public int ComputeFac(int num) {
        int num_aux;
        if (num < 1)
            num_aux = 1;
        else
            num_aux = num * (this.ComputeFac(num - 1));
        return num_aux;
    }
}
 '''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)