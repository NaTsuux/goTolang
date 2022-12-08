
grammar goTolang;

SKIP_
 : ( SPACES | COMMENT ) -> skip
 ;
/*
 * parser rules
 */

file_input: file_input_no_eof EOF;
file_input_no_eof: (NEWLINE | stmt | ('@' DECORATOR NEWLINE)? '[' file_input_no_eof+ ']')+;

stmt: simple_stmt
    | if_stmt
    | NEWLINE
    ;
simple_stmt: small_stmt NEWLINE;
small_stmt: expr_stmt # Bexpr
            | pass_stmt # Bpass
            | goback_stmt # Bgoback
            | goto_stmt # Bgoto
            | label_stmt # Blabel
            ;
goto_stmt: 'goto' NUMBER # Bto
            | 'goif' '{'or_test '}' NUMBER # Bif
            ;
label_stmt: '->' NUMBER;
expr_stmt: testlist_star_expr (augassign (testlist) | ('=' (testlist_star_expr))*);
testlist_star_expr: or_test (',' or_test)* (',')?;
augassign: ('+=' | '-=' | '*='  | '/=' | '%=' | '&=' | '|=' | '^=' |
            '<<=' | '>>=' | '**=' | '//=');
// For normal and annotated assignments, additional restrictions enforced by the interpreter
pass_stmt: 'pass';
goback_stmt: 'goback' '<-' NUMBER;

if_stmt: 'if' NEWLINE '{' NEWLINE ( or_test ':' suite)+ '}'; // suite带NEWLINE，所以NEWLINE放()+里会出奇怪问题
suite: simple_stmt | NEWLINE stmt+ ;

or_test: and_test ('or' and_test)*;
and_test: not_test ('and' not_test)*;
not_test: 'not' not_test | comparison;
comparison: expr (comp_op expr)*;
comp_op: '<'|'>'|'=='|'>='|'<='|'!='|'in'|'not' 'in'|'is'|'is' 'not';
expr: xor_expr ('|' xor_expr)*;
xor_expr: and_expr ('^' and_expr)*;
and_expr: shift_expr ('&' shift_expr)*;
shift_expr: arith_expr (('<<'|'>>') arith_expr)*;
arith_expr: term (('+'|'-') term)*;
term: factor (('*'|'/'|'%'|'//') factor)*;
factor: ('+'|'-'|'~') factor | power;
power: atom_expr ('**' factor)?;
atom_expr: atom trailer*;
atom: ('(' (testlist_comp)? ')' |
       '[' (testlist_comp)? ']' |
       'True' | 'False' |
       NAME | NUMBER | STRING | '...' | 'None');
testlist_comp: or_test ( (',' or_test)* (',')? );
trailer: '(' (arglist)? ')' | '[' subscriptlist ']' | '.' NAME;
subscriptlist: subscript (',' subscript)* (',')?;
testlist: or_test (',' or_test)* (',')?;
arglist: argument (',' argument)*  (',')?;
subscript: or_test;
argument: or_test;

/*
 * lexer rules
 */

BOOL_TRUE: 'True';
BOOL_FALSE: 'False';

DECORATOR: 'NICE' | 'OK' | 'POOR';

STRING
 : STRING_LITERAL
 ;

NUMBER
 : INTEGER
 | FLOAT_NUMBER
 ;

INTEGER
 : DECIMAL_INTEGER
 | OCT_INTEGER
 | HEX_INTEGER
 | BIN_INTEGER
 ;

IF : 'if';
OR : 'or';
AND : 'and';
NOT : 'not';
PASS : 'pass';

NEWLINE
 : ( SPACES
   | ( '\r'? '\n' | '\r' | '\f' ) SPACES?
   )
 ;


NAME
 : ID_START ID_CONTINUE*
 ;

STRING_LITERAL
 : SHORT_STRING
 ;

DECIMAL_INTEGER
 : NON_ZERO_DIGIT DIGIT*
 | '0'+
 ;

OCT_INTEGER
 : '0' [oO] OCT_DIGIT+
 ;

HEX_INTEGER
 : '0' [xX] HEX_DIGIT+
 ;

BIN_INTEGER
 : '0' [bB] BIN_DIGIT+
 ;

FLOAT_NUMBER
 : POINT_FLOAT
 | EXPONENT_FLOAT
 ;

DOT : '.';
STAR : '*';
OPEN_PAREN : '(' ;
CLOSE_PAREN : ')';
COMMA : ',';
COLON : ':';
SEMI_COLON : ';';
POWER : '**';
ASSIGN : '=';
OPEN_BRACK : '[' ;
CLOSE_BRACK : ']';
OR_OP : '|';
XOR : '^';
AND_OP : '&';
LEFT_SHIFT : '<<';
RIGHT_SHIFT : '>>';
ADD : '+';
MINUS : '-';
DIV : '/';
MOD : '%';
IDIV : '//';
NOT_OP : '~';
LESS_THAN : '<';
GREATER_THAN : '>';
EQUALS : '==';
GT_EQ : '>=';
LT_EQ : '<=';
NOT_EQ_2 : '!=';
AT : '@';
ARROW : '->';
INV_ARROW: '<-';
ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MULT_ASSIGN : '*=';
DIV_ASSIGN : '/=';
MOD_ASSIGN : '%=';
AND_ASSIGN : '&=';
OR_ASSIGN : '|=';
XOR_ASSIGN : '^=';
LEFT_SHIFT_ASSIGN : '<<=';
RIGHT_SHIFT_ASSIGN : '>>=';
POWER_ASSIGN : '**=';
IDIV_ASSIGN : '//=';


UNKNOWN_CHAR
 : .
 ;

/*
 * fragments
 */

/// shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
/// shortstringitem ::=  shortstringchar | stringescapeseq
/// shortstringchar ::=  <any source character except "\" or newline or the quote>
fragment SHORT_STRING
 : '\'' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f'] )* '\''
 | '"' ( STRING_ESCAPE_SEQ | ~[\\\r\n\f"] )* '"'
 ;

/// stringescapeseq ::=  "\" <any source character>
fragment STRING_ESCAPE_SEQ
 : '\\' .
 | '\\' NEWLINE
 ;

/// nonzerodigit   ::=  "1"..."9"
fragment NON_ZERO_DIGIT
 : [1-9]
 ;

/// digit          ::=  "0"..."9"
fragment DIGIT
 : [0-9]
 ;

/// octdigit       ::=  "0"..."7"
fragment OCT_DIGIT
 : [0-7]
 ;

/// hexdigit       ::=  digit | "a"..."f" | "A"..."F"
fragment HEX_DIGIT
 : [0-9a-fA-F]
 ;

/// bindigit       ::=  "0" | "1"
fragment BIN_DIGIT
 : [01]
 ;

/// pointfloat    ::=  [intpart] fraction | intpart "."
fragment POINT_FLOAT
 : INT_PART? FRACTION
 | INT_PART '.'
 ;

/// exponentfloat ::=  (intpart | pointfloat) exponent
fragment EXPONENT_FLOAT
 : ( INT_PART | POINT_FLOAT ) EXPONENT
 ;

/// intpart       ::=  digit+
fragment INT_PART
 : DIGIT+
 ;

/// fraction      ::=  "." digit+
fragment FRACTION
 : '.' DIGIT+
 ;

/// exponent      ::=  ("e" | "E") ["+" | "-"] digit+
fragment EXPONENT
 : [eE] [+-]? DIGIT+
 ;

fragment SPACES
 : [ \t]+
 ;

fragment COMMENT
 : '#' ~[\r\n\f]*
 ;

/// id_start     ::=  <all characters in general categories Lu, Ll, Lt, Lm, Lo, Nl, the underscore, and characters with the Other_ID_Start property>
fragment ID_START
 : '_'
 | [A-Z]
 | [a-z]
 ;

/// id_continue  ::=  <all characters in id_start, plus characters in the categories Mn, Mc, Nd, Pc and others with the Other_ID_Continue property>
fragment ID_CONTINUE
 : ID_START
 | [0-9]
 ;