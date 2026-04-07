grammar Stock;

// Parser Rules
file : header row+ EOF;

header : 'Date' ',' 'Open' ',' 'High' ',' 'Low' ',' 'Close' ',' 'Volume' NEWLINE ;

row : datetime ',' price ',' price ',' price ',' price ',' volume NEWLINE? ;

datetime : DATE TIME? ;

price : FLOAT | INT ;

volume: INT;


// Lexer Rules
DATE : [0-9]+ '/' [0-9]+ '/' [0-9][0-9][0-9][0-9] ;     // ex. 1/1/2026
TIME : [0-9][0-9] ':' [0-9][0-9] ':' [0-9][0-9] ;       // ex. 16:00:00

FLOAT : [0-9]+ '.' [0-9]+ ;
INT : [0-9]+ ;

NEWLINE : '\r'? '\n' ;
WHITESPACE : [ \t] -> skip ;