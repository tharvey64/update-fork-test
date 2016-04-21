# Variables and Data Types

### <a name="home"></a>Table of Contents:
* [Instruction](#instruction) - In this section we will be learning what variables and data types look like in JavaScript. They are written almost the same as in Python. ***Almost...***
* [Practice Problems](#practice-problems) - test your new AND current knowledge!
* [Glossary](#glossary) - Make sure to look here to review your programming vocabulary!

# <a name="instruction"></a>Instruction

As we begin our first section on JavaScript, it's worth noting that you'll see a lot of similarities between this JavaScript lesson about variables and data types and the corresponding Python lesson on variables and data types that you completed earlier in this course. What you'll find is that the concepts you learned in the Python lesson, such as the definition of [`variable`](#glossary), are the same no matter what programming language you use, whether it's Python, JavaScript, or any other languages you may learn in the future, such as C, Ruby, Java, etc. This makes learning a second or third programming language much easier than learning your first programming language.

Recognize that we've intentionally made this JavaScript lesson very similar to its corresponding Python lesson. We hope that this journey through definitions like [`variable`](#glossary) and concepts like [`assignment`](#glossary) will help to solidify those ideas in your head.

You'll also notice key differences between JavaScript and Python and how the two languages implement variables and data types. You'll encounter some new concepts like [`camelCase`](#glossary) and [`syntax`](#glossary) that will push your understanding of programming to a new level.

Just because this section is similar to the corresponding Python lesson on variables and data types, you shouldn't make the mistake of skimming this new JavaScript material. Read it slowly and carefully, and make sure you understand all of it before moving on to the next section.

Sorry if we got kind of heavy there. We're serious about you succeeding as a programmer, but we also like to have fun along the way. [See: here's a picture of our favorite internet pug](http://itsdougthepug.tumblr.com/post/134559118051/netflix-party-of-one-doug).

### What are Variables?


 -  [`Variables`](#glossary): Terms we create to reference a value
 - A [`value`](#glossary) is a piece of data we can manipulate through programming, such as **31** or **"kthxbai"**.
 - Imagine each variable as an empty storage container. That variable storage container contains a value.
 - We can [`assign`](#glossary) any value/values to a variable using one equal sign (=), and we call this the [`assignment operator`](#glossary). At this point we are putting items into our storage container to use later.
* JavaScript Variable [`syntax`](#glossary) is different from Python syntax.
    * Syntax - The arrangement and order of words, letters, and characters in a program.
* A JavaScript variable is declared first with the word `var` followed by the name of your variable
    * It is written in [camelCase](#glossary). It cannot start with a number or special character.
        * `camelCase` is indicating a different word with a capitalized letter

```javascript
var book = "Introduction to Algorithms";

var favoriteNumber = 7;

var petName = "Barkley";
```

### Data Types

***Data Types again?!? Yep. Let's see if JavaScript has anything different...***

#### Strings

* [`Strings`](#glossary) are any combination of numbers and/or letters wrapped in quotes
* What do strings look like in JavaScript? Pretty much the same as Python. The only differences in the examples below is the `syntax`.
* JavaScript strings are declared with the keyword `var`, variables names use `camelCase`, and the line on which the variable is declared ends with a **semi-colon**.

```javascript
var variableName = "Hello World";

var song = "Mambo #5";

var numberString = "1234";
```
* We can do plenty of things with strings. Such as [`concatenation`](#glossary). Remember what that means?
    * We can add different strings together to form a brand new one.
* Here's an example of adding variables into a string.

```javascript
var name = "Chadwick Boseman";

var hero = "Black Panther";

console.log(name + " will be playing " + hero + " in the new superhero movie")
```
* [`console.log`](#glossary) allows us to print out text onto our computer terminal. Similar to `print` in Python

#### Numbers

***There is a major different between Python and JavaScript in this section.***

* Javascript just has numbers, you no longer need to concern yourself with Integers and Floats. ***FREEDOM!***
* As always here are some examples below

```javascript
var myNumber = 1234;
var myOtherNumber = 3.14159;
var awesomeNumber = 42;
```
If you didn't read this before you should take a gander now. It's still a bonus interesting bonus: [The importance of 42](http://www.independent.co.uk/life-style/history/42-the-answer-to-life-the-universe-and-everything-2205734.html).
# <a name="practice-problems"></a>Practice Problems
* Create the following variables and assign them any value you'd like
    * name
    * age
    * favorite_movie
    * favorite_athelete
    * year

# <a name="glossary"></a>Glossary
You should memorize all these words. If you're having trouble remembering them, get yourself some index cards and make flashcards and study. These are import key words for programmers.

**Assign** - To store a value in a variable.

**Assignment Operator** - A single equal sign. Looks like this **=** . Links a variable name (to the left of the assignment operator) and a value (to the right of the assignment operator).

**camelCase** - A convention for writing variable names where the first word in variable name is lowercase and each subsequent word is capitalized. Example: myVariableName.

**Concatenation** - Adding two strings together to form one string.

**console.log** - JavaScript function that allows us to print out text onto our computer terminal. Similar to `print` in Python.

**Floats** - Number values with decimal points, such as 3.14159.

**Integer** - A number value such as 2. Does not include fractions or decimal numbers.

**Syntax** - The arrangement and order of words, letters, and characters in a program.

**String** - A value that is enclosed in quotation marks.

**Value** - A piece of information that can be used by a computer, such as a string or a number.

**Variable** - Names that refer to a value.
