# Python Data Structures

---

# Instruction

---
### Introduction

* In this section we will be looking at Python [`Data Structures`](#glossary).
* A data structure is a programming tool that allows us to hold multiple values at once. Remember, values include things like numbers and strings.
* The two key data structures we will be looking at are [`lists`](#glossary) and [`dictionaries`](#glossary)

### Lists

* A `list` is a `data structure` in python that allows use to store various data types. For now, the data types we know are strings and numbers.
* We create `lists` using square brackets, `[]`, and separate the different values with commas.
* The values that make up a list are called its [`elements`](#glossary).
* Notice we can assign the `list` `data structure` to a `variable`.
* `Lists` are similar to `Arrays` if you are coming from another programming language such as JavaScript or Ruby.

```
numbers = [1, 30, 26, 8, 99]

random_info = ["word", 23, "python", 3]
```
* Every element in a list has an [`index`](#glossary), which is a number that corresponds to an element's order within a list. The first element will have an index of zero.
* We can use this index to call a specific value. The syntax would be the variable name followed by square brackets containing the index number.

```
my_pets = ["Fluffy", "Shadow", "Snapper", "Tweety"]

my_pets[0] // "Fluffy"
my_pets[2] // "Snapper"
```
* The same indexing procedure can be done with `Strings`

```
intro = "Hello World"

intro[0] // "H"
intro[6] // "W"
intro[9] // "l"
```
### Dictionary

* Just like lists, dictionaries are data structures.
* Dictionaries are notoriously difficult to understand, especially for beginning programmers. If you find this section harder to comprehend than the last, that is OK and expected. Try your best to re-read the section and look through the glossary for additional help.
* A `dictionary` holds information in a [`key:value`](#glossary) format.
* Dictionaries can be assigned to variables and abide by the following rules:
    * They store their information as  `key:value` pairs.
    * They separate each of their `key:value` elements with commas.
    * They are opened and closed with curly braces: `{}`
* Below are two examples of `assigning` a dictionary to a variable.
* If you are coming from another programming language, Python `dictionaries` are similar to `hashes` or `associative arrays`

```
movie = {
    "title" : "Teenage Mutant Ninja Turtles",
    "release_year" : 1990,
    "imdb_rating" : 6.7,
    "director" : "Steve Barron",
}

my_pet = {
    "name": "Shadow",
    "type": "Dog",
    "color": "Black",
    "age": 16,
}
```
* There's two key differences between lists and dictionaries. First, you can **only** use numbers to index into lists. You can use any value to index into a dictionary. See the example below:
* Example indexing with lists:

```
my_pets = ["Fluffy", "Shadow", "Snapper", "Tweety"]

my_pets[0] // "Fluffy"
my_pets[2] // "Snapper"
```
* Example indexing with dictionaries:

```
my_info = {'name': 'jeff', 42: 'favorite number', 'age': 31}

my_info['name'] // 'jeff'
my_info[42] // 'favorite number'
```
* The second difference between dictionaries and lists is that lists are always in the same order. For example, `my_pets` from the example above will always be in this order: `["Fluffy", "Shadow", "Snapper", "Tweety"]`. While `my_info` might be in this order: `{'name': 'jeff', 42: 'favorite number', 'age': 31}` or it could be in a different order like this: `{'age': 31, 42: 'favorite number', 'name': 'jeff'}`.

### Other Data Structures

* There are two other data structures in Python. They are `tuples` and `sets`
* This prework will not go in depth with either but feel free to follow the links below if you wish to read about them.
    * [Python Tuples](http://www.tutorialspoint.com/python/python_tuples.htm)
    * [Python Sets](http://www.python-course.eu/sets_frozensets.php)

### Iterable and Indexing

* You will be hearing the word [`iterable`](#glossary) throughout your programming career.
* An iterable is a programming object that can return its values one at a time.
* Both `Lists` and `Strings` are iterables.

***Note***

* Python3 comes with a built in function (we'll go over functions later) that will allow us to view information in our terminal.
* This is called `print()`. You may have seen it a few times in our recent chapters. 
* Here's an example of how it can be used

```
intro = "Hello World"

print(intro)
// "Hello World"

my_list = ["abc", "xyz", "123", "Will Ferrall"]

print(my_list[3])
// "Will Ferrall"
```
---

#</a>Glossary

---
You should memorize all these words. If you're having trouble remembering them, get yourself some index cards and make flashcards and study. These are import key words for programmers.

* **Data structure** - A programming tool that allows us to hold multiple values at once.

* **Element** - One of the values in a list.

* **Index** - A number that corresponds to an element's order within a list.

* **Iterable** - A programming object that can return it's values one at a time.

* **key:value** - A pair of items in a dictionary. Keys are used to look up values in a dictionary.

* **List** - A named collection of ordered values, where each value is accessible by a numbered index.
