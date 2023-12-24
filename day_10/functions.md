# Functions
- Functions are a block of code that can be called by its name.
- Functions are used to avoid repetition of code.
- Functions are used to make code reusable.
- Functions are used to make code modular.
- Functions are used to make code readable.

## Syntax
```python
def function_name(parameters):
    # code to be executed
    return <expression>
```
- def is a keyword used to define a function.
- function_name is the name of the function.
- () is used to pass parameters to the function.

## How to call a function?
```python
def function_name():
    # code to be executed

function_name()
```


## Types
- Built-in functions
- User-defined functions

## Built-in functions
- Built-in functions are functions that are already defined in python.
- Built-in functions are available in python by default.

### Examples
- print()
- input()
- len()
- type()

## How to know if a function is built-in or user-defined?
- We can use the type() function to know if a function is built-in or user-defined.

```python
print(type(print)) # prints <class 'builtin_function_or_method'>
```

```python
def greet():
    print("Hello")

print(type(greet)) # prints <class 'function'>
```

## User-defined functions
- User-defined functions are functions that are defined by the user.
- User-defined functions are not available in python by default.
- User-defined functions are defined using the def keyword.



## Types Function Arguments

- Required arguments (positional arguments)
- Keyword arguments
- Default arguments
- Arbitrary arguments ( *args )
- Arbitrary keyword arguments ( **kwargs )

### Required arguments (positional arguments)

- Most common type of arguments.
- Values are passed to the function based on the position or order.
- The number of arguments passed to the function must match the number of parameters defined in the function.

### Example 1
```python
def greet(name):
    print("Hello", name)

greet("Ranjit") ✔️ #prints value
greet() ❌ #throws error
```

### Example 2
```python
def greet(name, age):
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
greet("Ranjit") ❌ #throws error
greet(20, "Ranjit") ❌ #throws error
```

In Python, we can use type hints to indicate the expected types of the parameters.

```python
def greet(name: str, age: int):
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
```
---
**Note:**
This is just a hint and not a constraint. We can still pass any type of value to the function.
---
To make it a constraint, we can use the assert keyword.

```python
def greet(name: str, age: int):
    assert type(name) == str, "name must be a string"
    assert type(age) == int, "age must be an integer"
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", 20) ✔️ #prints value
```
