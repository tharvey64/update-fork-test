# JavaScript Data Structures

### Table of Contents:

* [Instruction](#instruction) - Your review and learning about JavaScript happens here.
* [Practice Problems](#practice-problems) - Test some of your new JavaScript knowledge.
* [Glossary](#glossary) - Keep learning and memorizing this vocabulary.

### What is a Data Structure

* A [`data structure`](#glossary) is a programming tool that allows us to hold multiple values at once.
* The two Python `data structures` we learned earlier were `lists` and `dictionaries`.
* The terms for these `data structures` in JavaScript are [`arrays`](#glossary) and [`objects`](#glossary).

#### JavaScript Arrays

* `Arrays` in JavaScript act exactly the same as `lists` in Python.
* `Arrays` are used to store multiple values.
* These values can be different data types (strings or numbers).
* We create `arrays` the same way we made `lists`. With square brackets `[]`.
* The values are separated with commas.
* `Arrays` can be assigned to variables.
* Here are some examples of JavaScript Arrays:

```javascript
var numbers = [1, 30, 26, 8, 99];

var randomInfo = ["word", 23, "python", 3];
```
* Every value inside of an array can be called an `element`.
* Remember to use JavaScript `syntax` when declaring your variables, and remember how that syntax is different from Python `syntax`?

#### JavaScript Objects

* A JavaScript [`object`](#glossary) is a data structure similar to a Python `dictionary`.
	* Some tutorials may refer to these as `associative arrays`. For the purpose of this tutorial we will use the term Javascript `objects`.
* `Objects` will have their information stored in a [`key:value`](#glossary) format.
* `Objects` follow the same parameters as python dictionaries:
	* They can be assigned to a variable.
	* They store their information as  `key:value` pairs. We also call this [`key:value mappings`](#glossary).
	* They separate each of their `key:value` elements with commas.
	* They are opened and closed with curly braces: `{}`.
* Below are two examples of creating a variable with a JavaScript Object:

```
var movie = {
	"title" : "Teenage Mutant Ninja Turtles",
	"release_year" : 1990,
	"imdb_rating" : 6.7,
	"director" : "Steve Barron",
};

var myPet = {
	"name": "Shadow",
	"type": "Dog",
	"color": "Black",
	"age": 16,
};
```

#### Iterable and Indexing

* Remember those words [`iterable`](#glossary) and [`indexing`](#glossary)? Just in case you need a refresher:
	* An `iterable` is a programming object that can return it's values one at a time
	* An [`Index`](#glossary) is what we use to reference a specific value inside an iterable. Remember that if you want to sound fancy, the plural of `index` is `indices`!
	* `Indices` always start from zero and increment by 1.
	* `Strings` and `Arrays` are iterables and we can target a specific character or value using an index.

```
var myPets = ["Fluffy", "Shadow", "Snapper", "Tweety"];

console.log(myPets[0]); // "Fluffy"
console.log(myPets[2]); // "Snapper"
```
* The same indexing procedure can be done with `Strings`:

```
var intro = "Hello World";

console.log(intro[0]); // "H"
console.log(intro[6]); // "W"
console.log(intro[9]); // "l"
```
* If you're wondering why JavaScript `objects` are not here, it's because they are not `iterables`. They're not `iterables`, because  they already have their own mapping reference. In the example below, "title", "year", and "cast" are the mapping reference for the "movie" `object`.

```
var movie = {
	"title" : "Zoolander",
	"year" : 2001
	"cast" : ["Will Ferrall", "Ben Stiller", "Owen Wilson"],
};

console.log(movie["title"]); // "Zoolander"
console.log(movie["year"]); // 2001
console.log(movie["cast"]); // ["Will Ferrall", "Ben Stiller", "Owen Wilson"]
```

***Note***

* Remember that nice `print()` function we were able to use in Python?
* JavaScript has something that does the same thing, it's called `console.log()`
* We used it a bunch of times in earlier examples but here's one more example:

```
var intro = "Hello World";

console.log(intro);
// "Hello World"

var myList = ["abc", "xyz", "123", "Will Ferrall"];

console.log(my_list[3]);
// "Will Ferrall"
```

---

# Exercises

#### Exercise 1

* Create a `array` containing the following strings.
	* "Leonardo"
	* "Raphael"
	* "Michaelangelo"
	* "Donnatello"
* Assign this `array` to a variable called `turtles`

#### Exercise 2

* Take the information below and make them into two separate dictionaries
* Assign those two dictionaries to two separate variables
* The variable names should be: `michaela` and `steve`
	* Remember, when declaring your variables, they are lowercase

```
Name: Michaela
Gender: Female
Height in cm: 178
Job: Visual Artist
Parents: Aimee, Louis
Pets: Fezzy, Rufus
```

```
Name: Steve
Gender: Male
Height in cm: 160
Job: Graphic Designer
Nickname: The Cow
Friends: Stephen, Stephanie, Stefan
Jobs: Graphic Designer at Acme Corp, Bartender at Banter
```

#### Exercise 3

* Console.log the `Job` of Michaela
* Console.log the `Pets` of Michaela
* Console.log the `Nickname` of Steve
* Console.log the `Jobs` of Steve

# <a name="glossary"></a>Glossary
You should memorize all these words. If you're having trouble remembering them, get yourself some index cards and make flashcards and study. These are import key words for programmers.

**Array** - A named collection of ordered values, where each value is accessible by a numbered index. Similar to a Python `list`.

**Assign** - To store a value in a variable.

**Data structure** - A programming tool that allows us to hold multiple values at once.

**Iterable** - A number that corresponds to an element's order within a list.

**Iterable** - A data structure that can return it's values one at a time.

**key:value** - A pair of items in an object. Keys are used to look up values in an object.

**key:value mappings** - The rules for converting a `key` to a `value`, or vica versa.

**Object** - A named data structure where each item has a key and a corresponding value.
