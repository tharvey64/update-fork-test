# Reverse Polish Notation

* Reverse polish notation is a mathematical notation in which every operator follows all of its operands. Check out the explanation section on their [wikipedia page](http://en.wikipedia.org/wiki/Reverse_Polish_notation). 
* The mathematical operator goes at the end of the equation
* If there is more than one operator, that operator is placed after the second operand
* Examples:

```
3 4 + = 7

4 2 / = 2

3 4 - 5 + = 4
```

# Exercise

* Write a program that takes a string as an argument
* The string will be the reverse polish notation equation you are assessing. For example:
	* rpn("3 4 +") == 7
* The function will take in the equation and return the result 
