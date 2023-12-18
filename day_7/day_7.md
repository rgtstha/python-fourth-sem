
## Boolean Data Type
1. **bool** - Boolean represents one of two values: True or False.

    ```python
    a = True
    b = False

    print(type(a)) # <class 'bool'>
    print(a) # True
    print(b) # False

    print(10 > 5) # True
    ```
## Set Data Type
1. **set** - Set is used to store multiple items in a single variable. it is unordered and unindexed. Duplicate values are not allowed. It is used to perform mathematical set operations like union, intersection, etc.

    ```python
    a = {1, 2, 3, 4, 5}
    b = {"apple", "banana", "cherry"}
    c = {1, "apple", True, 1.5}

    print(type(a)) # <class 'set'>
    print(a) # {1, 2, 3, 4, 5}
    print(a[0]) # TypeError: 'set' object is not subscriptable

    # Mutating set
    a.add(6)
    print(a) # {1, 2, 3, 4, 5, 6}

    # adding duplicate value
    a.add(6)
    print(a) # {1, 2, 3, 4, 5, 6} # duplicate value is not added

    # adding multiple values
    
    #union and intersection
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print(a.union(b)) # {1, 2, 3, 4, 5, 6, 7, 8}
    print(a.intersection(b)) # {4, 5}

    ```
2. **frozenset** - Frozenset is used to store multiple items in a single variable. Frozenset is immutable. It is the unchangeable version of set.

    ```python
    a = frozenset({1, 2, 3, 4, 5})
    b = frozenset({"apple", "banana", "cherry"})
    c = frozenset({1, "apple", True, 1.5})

    print(type(a)) # <class 'frozenset'>
    print(a) # frozenset({1, 2, 3, 4, 5})
    print(a[0]) # TypeError: 'frozenset' object is not subscriptable
    ```
## Mapping Data Type
1. **dict** - Dictionary is used to store data in key:value pairs. Dictionary is mutable. It is unordered and unindexed.

    ```python
    a = {"name": "John", "age": 36}
    b = {1: "apple", 2: "banana", 3: "cherry"}
    c = {1: "apple", "color": ["red", "green", "blue"]}

    my_dict = {}
    my_dict["name"] = "John"
    my_dict["age"] = 36

    print(my_dict) # {'name': 'John', 'age': 36}

    print(my_dict["name"]) # John
    print(my_dict.get("name")) # John

    print(my_dict.keys()) # prints all keys
    ```

    ```
## None Data Type
1. **None** - None is used to define a null value, or no value at all.

    ```python
    a = None
    b = None
    c = None
    ```

# Mutable vs Immutable
<!-- table -->
| Mutable | Immutable |
| --- | --- |
| Mutable objects can change their value  | Immutable objects can not change their value. |
| Eg: List, Set, Dictionary are mutable. |Eg: Tuple, Range, Boolean, Frozenset, Bytes, Bytearray, Memoryview, None are immutable. |

# Assignemnts for strings
1. Create a variable named `name` and assign your name to it. Print the value of the variable.

    ```python
    name = "Ranjit Shrestha"
    print(name)
    ```

2. From the variable `name`, print the first character, last character, first 3 characters, last 3 characters, and reverse of the string.

    ```python
    name = "Ranjit Shrestha"
    print(name[0]) # R
    print(name[-1]) # a
    print(name[0:3]) # Ran
    print(name[-3:]) # tha
    print(name[::-1]) # ahtserhS tijnaR
    ```

# Assignments for list
1. Create a list named `fruits` and assign 3 fruits to it. Print the value of the variable. Add 2 more fruits to the list. Print the value of the variable. Remove 1 fruit from the list. Print the value of the variable.

    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits) # ['apple', 'banana', 'cherry']

    fruits.append("orange")
    fruits.append("mango")
    print(fruits) # ['apple', 'banana', 'cherry', 'orange', 'mango']

    fruits.remove("apple")
    print(fruits) # ['banana', 'cherry', 'orange', 'mango']
    ```

2. From the variable `fruits`, print the first fruit and last fruit.

    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0]) # apple
    print(fruits[-1]) # cherry
    ```

3. From the variable `fruits`, print the first 3 fruits, last 3 fruits, and reverse of the list.

    ```python
    fruits = ["apple", "banana", "cherry", "orange", "mango"]
    print(fruits[0:3]) # ['apple', 'banana', 'cherry']
    print(fruits[-3:]) # ['cherry', 'orange', 'mango']
    print(fruits[::-1]) # ['mango', 'orange', 'cherry', 'banana', 'apple']
    ```

# Assignments for tuple
1. Create a tuple named `fruits` and assign 3 fruits to it. Print the value of the variable. Add 2 more fruits to the tuple. Print the value of the variable. Remove 1 fruit from the tuple. Print the value of the variable.

    ```python
    fruits = ("apple", "banana", "cherry")
    print(fruits) # ('apple', 'banana', 'cherry')

    fruits = fruits + ("orange", "mango")
    print(fruits) # ('apple', 'banana', 'cherry', 'orange', 'mango')

    fruits = fruits[1:]
    print(fruits) # ('banana', 'cherry', 'orange', 'mango')
    ```