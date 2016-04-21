# Loops and Conditionals

### <a name="home"></a>Table of Contents:
* [Instruction](#instruction) - JavaScript Loops and Conditionals coming at ya
* [Practice Problems](#practice-problems) - Testing your new knowledge
* [Glossary](#glossary) - More vocabulary words!

# <a name="instruction"></a>Instruction
#### Introduction

* JavaScript also gives us `Conditional` and `Looping` functionality
	* [`Conditional`](#glossary) statements give us the ability to check conditions and change the behavior of the program accordingly.
	* [`Loops`](#glossary) repeatedly execute a set of programming commands.
* The utilization and syntax in this section is much different between JavaScript and Python.

#### Conditionals - The If/Else statement

* We used many conditional statements in the previous sections and we're not going to stop now. The If/Else statement is almost the same in JavaScript. Almost...
* Remember the `if/else` statement will have conditions which allow us to run a block of code when that condition is true. We call this [`control flow`](#glossary).
* JavaScript If/Else syntax: `if`, `else if`, and `else`
* Each condition is followed with their code block wrapped in curly braces `{}`

```
if (this condition is true){
	run this code
} else if (this condition is true){
	run this code
} else {
	run this code
};
```
* JavaScript not only requires curly braces `{}` around the code blocks but also parenthesis `()` around the conditions

```
var favNum = 8;

if (favNum < 5){
	return "Your number is less than five";
} else if (favNum < 10){
	return "Your number is less than ten";
} else {
	return "Your number is pretty"
};

[output] "Your number is less than ten"
```

#### For Loops

* For Loops are not only a big part of Python, and JavaScript but a big part of programming in general.
* JavaScript [`for loops`](#glossary) work and act much differently than what you may be used to from the previous Python sections.
* Let's make an array of animals and loop through it to console.log out all the animals one by one:

```
var animals = ["dog", "cat", "bird", "turtle", "fish", "hamster", "lizard"];

for (var i = 0; i < animals.length+1; i++){
	console.log(animals[i])
};

"dog"
"cat"
"bird"
"turtle"
"fish"
"hamster"
"lizard"
```
* So that loop looks very different than what we did in Python.
* Notice there are three parts in the for loop parenthesis section:
* `var i = 0` - this part initializes a variable **`i`** to the value 0.
	* `i` is just a placeholder, we could just have easily written `var x = 0`
	* `i` is used as a best practice because it usually references the `index` value inside an iterable.
* `i < animals.length + 1` - this is a condition saying as long as `i` is less than the length of the animals `array`
	* We used a `+1` at the end to make sure we console log "lizard"
* `i++` is telling us that after the loop runs the code block it will increment the value of `i` by one
	* We can also manipulate this to be anything we want. `e.g. i += 2`
* The code between the curly brackets `{}` will be what is run at every loop until the loop is completed
* Here's one more example:

```
numbers = [1,22, 54, 32, 87, 99, 80]

for (var i = 0; i<numbers.length+1; i++){
	console.log(numbers[i])
};

1
22
54
32
87
99
80
```

#### While Loops

* Remember we had access to another loop? The [`while loop`](#glossary) works in JavaScript the same way as Python.
* Again, there are a few syntax differences between Python and JavaScript.
* Here is an example:

```
var i = 0;

while (i < 10){
	console.log(i)
	i += 1
};

console.log("all done!");

[output]
1
2
3
4
5
6
7
8
9
all done!
```
* The loop is evaluating the condition in the parenthesis `i < 10`
* If the condition is true the code will run. If the condition is false JavaSCript will exit the statement.
	* Notice inside the code block we are incrementing i so it will eventually make the condition evaluate to false.
* If your condition will always remain true the loop will never end. This is known as an `inifite loop`
* Below is a similar example except the condition was changed and it has now become an infinite loop

```
var i = 10;
while (i > 5){
	console.log(i);
	i += 1;
};
```

#### Built In Methods

* Like Python, JavaScript comes with their own built in [`methods`](#glossary)
* We already saw one of them in the for loop examples. That is the `.length` method

***.length***

* `.length` can be written behind any variable that is an iterable and return the number of elements contained within that iterable.
	* Remember an iterable is a data type or data structure that can be looped through, such as a string or array.
* Below is an example of grabbing the length in an array:

```
[input] var turtles = ["Leo", "Raph", "Donny", "Mickey"];
[input] console.log(turtles.length);
[output] 4
```
* How about a string?

```
[input] var hi = "Byte Academy rulez";
[input] console.log(hi.length);
[output] 18
```
* How about JavaScript Objects?

```
var hero = {
	"Name": "Peter Parker",
	"Universe": "Marvel",
	"City": "New York",
	"Age": 18,
};
[input] console.log(hero.length);
[output] undefined
```
* Woah what is this undefined result? Well JavaScript Objects read these data structures as key:value mappings, so it is not an `iterable` that can be measured with the `.length` method

***Examples with Functions***

* Let's take a look at these concepts in action
* I want a function that will tell me the length of any array I give it

```
var names = ["Peter Parker", "Matt Murdock", "Charles Xavier"]

var numbers = [123, 654, 32, 8012, 43, 2, 78, 984, 12]

var arrLengths = function(arr){
	console.log(arr.length)
};

arrLengths(names) === 3

arrLengths(numbers) === 9
```

---

# Exercises

#### FizzBuzz

* FizzBuzz is a common interview brain teaser.
* You will have to write a function that will take in a number as an argument
* If the number is divisible by 3, print "Fizz"
* If the number is divisible by 5, print "Buzz"
* If the number is divisible by 3 and 5, print "FizzBuzz"
* If the number is not divisible by 3 or 5, print "This number is not fizzy"

# <a name="glossary"></a>Glossary
You should memorize all these words. If you're having trouble remembering them, get yourself some index cards and make flashcards and study. These are import key words for programmers.

**Block** - A section of code that is grouped together

**Condition** - An expression that functions similar to a question and evaluates to either True or False

**Control flow** - The order which statements or expressions are executed in a program

**For loop** - A type of loop that begins with a for statement which gives us the ability to iterate over items in a sequence.

**Loop** - Repeated execution of a set of programming commands

**Method** - While there are key differences between methods and functions, at this point, know that we're using "method" as a synonym for "function".

**While loop** - A loop that repeatedly executes a set of commands as long as a given condition is True.
