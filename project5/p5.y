%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
extern void yyerror (char*);
%}

//tokens

%token RENAME AS WHERE UNION INTERSECT MINUS TIMES JOIN DIVIDEBY CNO CITY 
%token CNAME SNO PNO TQTY OPENP CLOSEP RELOP COMMA
%token SNAME QUOTA PNAME COST AVQTY SNUM STATUS PNUM COLOR WEIGHT QTY S P 
%token SP PRDCT CUST ORDERS OPENB CLOSEB INTEGER

%%
start : expression	{printf("ACCEPT\n"); }  /* YYACCEPT;}*/
	;
expression : one_relation_expression | two_relation_expression 
	;
one_relation_expression : renaming | restriction | projection
			;
renaming : term RENAME attribute AS attribute
	;
term : relation | OPENP expression CLOSEP 
	;
restriction : term WHERE comparison
	;
projection : term | term OPENB attribute_commalist CLOSEB
	;
attribute_commalist : attribute | attribute COMMA attribute_commalist
	;
two_relation_expression : projection binary_operation expression
	;
binary_operation : UNION | INTERSECT | MINUS | TIMES | JOIN | DIVIDEBY
	;
comparison :  attribute compare number
	;
compare : RELOP
	;
number : val | val number
	;
val : INTEGER
	;
attribute : CNO | CITY | CNAME | SNO | PNO | TQTY | 
		  SNAME | QUOTA | PNAME | COST | AVQTY |
		  SNUM | STATUS | PNUM | COLOR | WEIGHT | QTY
	;
relation : S | P | SP | PRDCT | CUST | ORDERS
	;

/*
int main(void)
{
	yyparse();
	return 0;
}

int yywrap(void)
{
	return 1;
}
*/
