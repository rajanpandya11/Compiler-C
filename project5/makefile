p5: lex.yy.c y.tab.c
	gcc lex.yy.c y.tab.c -o p5

lex.yy.c: y.tab.c p5.l
	lex p5.l

y.tab.c: p5.y
	yacc -d p5.y

clean: 
	rm -f lex.yy.c y.tab.c y.tab.h p5
