
### Keyword arguments

- Values are passed to the function based on the parameter name.
- Allows us to pass arguments in any order.
- The number of arguments passed must match the number of parameters defined in the function.
- This makes the code more readable.


### Example 1
```python
def person(name, age):
    print("Hello", name, "you are", age, "years old")

person(name="Ranjit", age=20) ✔️ #prints value

person(age=20, name="Ranjit") ✔️ #prints value

person("Ranjit", 20) ✔️ #prints value

person("Ranjit", age=20) ✔️ #prints value

person(name="Ranjit", 20) ❌ #throws error

person(age=20, "Ranjit") ❌ #throws error
```

#### Assignment
Write a function that takes two numbers as arguments and returns their sum.

```python
def perform_math_operation(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        # Check for division by zero
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Unsupported operator."

result_addition = perform_math_operation(num1=5, num2=3, operator='+')
```

### Default arguments
- default arguments are used to provide a default value to a parameter.

- If we don't pass a value to a parameter, the default value will be used.

```python
def greet(name="Ranjit"):
    print("Hello", name)

greet() ✔️ #prints Hello Ranjit
greet("Ranjit") ✔️ #prints Hello Ranjit
```

```python
def greet(name="Ranjit", age):
    print("Hello", name, "you are", age, "years old")

greet(20) ❌ #throws error
greet("Ranjit", 20) ✔️ #prints Hello Ranjit you are 20 years old
```

Always remember, positional arguments must come before other arguments.

#### Hint with default arguments

```python
def greet(name: str = "Ranjit", age: int = 20):
    print("Hello", name, "you are", age, "years old")

greet() ✔️ #prints Hello Ranjit you are 20 years old
```

### Arbitrary arguments
- Also known as variable-length arguments.
- Allows us to pass any number of arguments to a function.
- The parameter name is prefixed with *.
- The arguments are stored in a tuple.
- If we don't know how many arguments to pass to a function, we can use this type of argument.
- Generally, denoted as *args.


```python
def greet(*names):
    print("Hello", names)

greet("Ranjit", "Rahul", "Rohit") ✔️ #prints Hello ('Ranjit', 'Rahul', 'Rohit')
```

```python
def greet(*names):
    # names are stored in a tuple
    for name in names:
        print("Hello", name)

greet("Ranjit", "Rahul", "Rohit") ✔️ 

```

Use case: We can use this type of argument to find the sum of any number of numbers.

```python
def add(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

print(add(1, 2, 3, 4, 5)) ✔️ #prints 15

print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) ✔️ #prints 55
```

### Arbitrary keyword arguments
- Allows us to pass any number of keyword arguments to a function.
- The parameter name is prefixed with **.
- Generally, denoted as **kwargs.
- It allows us to pass keyword arguments in any order.
- The arguments are stored in a dictionary.

```python
def greet(**names):
    print("Hello", names)

greet(name1="Ranjit", name2="Rahul", name3="Rohit") ✔️ #prints Hello {'name1': 'Ranjit', 'name2': 'Rahul', 'name3': 'Rohit'}
```

Use case:
Imagine a case where science and maths are compulsory subjects and the student can choose any number of optional subjects.

```python
def percent(math, sci, **optional):
   print ("maths:", math)
   print ("sci:", sci)
   s=math+sci
   for k,v in optional.items():
      print ("{}:{}".format(k,v))
      s=s+v
   return s/(len(optional)+2)

result=percent(math=80, sci=75, Eng=70, Hist=65, Geo=72)
print ("percentage:", result)
```

```python
def print_info(name, **kwargs):
    print(f"Name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info("John", age=25, city="New York", occupation="Engineer")

```



### Additional Knowledge

## Keyword-only arguments
- Keyword-only arguments are used to force the caller to use keyword arguments for specific parameters.

- Use of keyword-only arguments is optional.

- You should put an asterisk (*) before the keyword-only argument.

Python's built-in print() function is a good example of keyword-only arguments.

```python
print("Hello", "World", sep=" ", end="\n")
```

- sep and end are keyword-only arguments.

Another example:

```python
def greet(name, *, age):
    print("Hello", name, "you are", age, "years old")

greet("Ranjit", age=20) ✔️ #prints Hello Ranjit you are 20 years old
greets("Ranjit", 20) ❌ #throws error
```

## Lambda Functions
- Also known as anonymous functions.
- A function without a name.
- A function with no name is called an anonymous function.
- It is defined using the lambda keyword.
- It can have any number of arguments but only one expression.

### Syntax:
```python
lambda arguments: expression
```

### Example 1:
```python
# normal function
def add(num1, num2):
    return num1 + num2

print(add(5, 3)) # prints 8

# lambda function
add = lambda num1, num2: num1 + num2

print(add(5, 3)) # prints 8
```

### Example 2:
```python
# normal function
def square(num):
    return num * num

print(square(5)) # prints 25

# lambda function

square = lambda num: num * num

print(square(5)) # prints 25
```

Use case: We can use lambda functions as arguments to other functions.

```python
def my_func(func, num):
    return func(num)

print(my_func(lambda num: num * num, 5)) # prints 25

Some built-in functions like map(), filter(), reduce() accept lambda functions as arguments.

### map()

- map() function applies a given function to each item of an iterable (list, tuple etc.) and returns a list of the results.

```python
# map function example
def square(num):
    return num * num

numbers = [1, 2, 3, 4, 5]

squared_numbers = map(square, numbers)

print(list(squared_numbers)) # prints [1, 4, 9, 16, 25]
```

```python
# map function example
numbers = [1, 2, 3, 4, 5]

squared_numbers = map(lambda num: num * num, numbers)
