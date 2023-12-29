def print_info(name, **kwargs):
    print("Name:", name)
    for detail, value in kwargs.items():
        print(f"{detail}:", value)

print_info(
    name = "Ram",
    age = 23,
    address ="Kathmandu",
    mobile = '984312345',
    occupation = 'student'
    )