def display():
    print('this is a computer')


def student(name, age, gender):
    print("Name =", name, ",age =", age, "Gender =", gender)


def max2(a, b):
    if a > b:
        return a
    else:
        return b


def sum2(a, b):
    return a + b


def teacher(name, age, gender):
    return name


print("sum of 2 number =", sum2(5, 8))
print("max of 2 number=", max2(3, 9))
display()
student("Dara", 18, 'M')



def my_function(fname: str):
    print(fname + " Refsnes")


# my_function("Hello")

# Default parameter value


def default_para_fun(country="Norway"):
    print("I am from " + country)


default_para_fun("Sweden")
default_para_fun("India")
default_para_fun()

# Return values
def return_value_fun(x):
    return 5 * x


result = return_value_fun(10)
print(result)

# Keyword arguments


def keyword_arguments_fun(child3, child2, child1):
    print("The youngest child is " + child3)


# keyword_arguments_fun(child1="Emil", child3="Thorn", child2="Tobias")

# Arbitrary arguments, *args
def arbitrary_arguments_fun(*kids):
    print("The youngest child is " + kids[2])


# arbitrary_arguments_fun("Emil", "Tobias", "Linus")

# Arbitrary keyword arguments, **kwargs
def arbitrary_keyword_arguments_fun(**kid):
    print("His last name is " + kid["city"])


# arbitrary_keyword_arguments_fun(
#     fname="Tobias", lname="Refsnes", age=36, city="Trondheim")

# Passing a list as an argument


def passing_list_as_argument_fun(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

