sourcefiles = queens.c binomial.c
compiler = clang

default:    ;$(compiler) -O9 -std=c99 $(sourcefiles)
debug:      ;$(compiler) -Wall -Wextra -std=c99 $(sourcefiles)
run:        ;$(compiler) -O9 -std=c99 $(sourcefiles) && ./a.out 4
clean:      ;rm -rf *.out
