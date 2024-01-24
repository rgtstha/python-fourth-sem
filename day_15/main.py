from designer import Designer
from developer import Developer


designer1 = Designer(
    name = "Binaya",
    address= "Kathmandu",
    salary= 50000,
    tool= 'figma',
)

developer1 = Developer(
    name = "Charitra",
    address="bhaktapur",
    salary=60000,
    programming_lang= "Python"
)

designer1.print_details()
developer1.print_details()

        