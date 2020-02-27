%{
#include "y.tab.h"
#include <stdio.h>
#include <stdlib.h> 
void yyerror(char*);
int yyparse(void);
%}

%%

 /* on reading this*/	/* do this*/	
RENAME		return RENAME;
AS			return AS;
WHERE			return WHERE;
UNION  		return UNION; 
INTERSECT  		return INTERSECT; 
MINUS			return MINUS;	
TIMES			return TIMES;	
JOIN			return JOIN;
DIVIDEBY		return DIVIDEBY;
CNO			return CNO;	
CITY			return CITY;
CNAME			return CNAME;	
SNO			return SNO;
PNO			return PNO;	
TQTY			return TQTY;
SNAME			return SNAME;
QUOTA			return QUOTA;
PNAME			return PNAME;
COST			return COST;
AVQTY			return AVQTY;
S#			return SNUM;
STATUS		return STATUS;
P#			return PNUM;
COLOR			return COLOR;
WEIGHT		return WEIGHT;
QTY			return QTY;
S			return S;
P			return P;
SP			return SP;
PRDCT			return PRDCT;
CUST			return CUST;
ORDERS		return ORDERS;
","			return COMMA;
"("			return OPENP;
")"			return CLOSEP;
"["			 return OPENB; 
"]"			return CLOSEB;
"<"	                return RELOP;
">"                     return RELOP;
"<="		return RELOP;
">="                   return RELOP;
"\="		return RELOP;
"<>" 		return RELOP;
[0-9]			return INTEGER;
[ \t\n]			;
.			yyerror("REJECT\n");

%%

void yyerror(char* str)
{
	fprintf(stderr,"REJECT\n");
	exit(1);
}
int yywrap(void)
{
	return 1;
}
int main(void)
{
	yyparse();
}

