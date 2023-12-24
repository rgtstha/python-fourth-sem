def person(name:str, age:int):
    assert type(name) == str , "name argument must be string"
    assert type(age) == int, "age must be integer"
    
    print(f"Person name is {name} and age is {age}")


person(34, "Ram")