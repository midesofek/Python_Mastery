### FUNCTIONS ###

# Examples
# print(), input(), type(), int(), float(), len(), str(), list(), dict()
# min(), max(), sum(), sorted(), open(), file(), help(), and dir()

## input ##
# first_name = input("What is your first name?")
# age = input("How old are you chad?")
# print("Hello", first_name, "You are", age, "years old!")

last_name = 'Yetayeh'       # str
country = 'Finland'         # str
age = 250                   #int

print(type(('name', 'name','Asabeneh')))
print(type({'name':'Asabeneh'}))
print(type(zip([1,2],[3,4])))
print(type(last_name))
print(type(country))
print(type(1+4j))
print(type(age))

# multiple variables in one line
main_goal, next_milestone, daily_goal, locked_in = 'Smash $5M + $200k monthly', "Cross $200k", "$300 per day", True
print(main_goal, next_milestone, daily_goal, locked_in)

### DATA CASTING
# int to float
num_int = 200
print('num_int:', num_int)
num_float = float(num_int)
print('num_float:', num_float)

# string to int
num_str = '200000'
num_int2 = int(num_str)
print(num_str, num_int2)

# int to string
num_int3 = 200
print('num_int3:', type(str(num_int3)))

# float to int
pie = 3.14
print('pie:', int(pie))

# str to list
name_str = "Sofek"
name_list = list (name_str)
print('name_list:', name_list)

## len ##
print(len("Mide"))
print(len(name_str), "Mide" > name_str)

## TASK ##
num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two 
exp = num_one ** num_two
floor_div  = num_one // num_two
# circle_radius = int(input("Enter circle radius: "))
# area_of_circle = 3.14 * circle_radius **2
# circum_of_circle = 2 * 3.14 * circle_radius
# print("RESULTS:",area_of_circle, circum_of_circle)

# name_first = input("Enter your first name: ")
# name_last = input("Enter your last name: ")
# full_name = name_first + " " + name_last
# print("Your full name is:", full_name)
# name_country = input("Enter your country: ")
# name_age = input("Enter your age: ")
# print("You are", full_name, "from", name_country, "and you are", name_age, "years old.")
# print('Congratulations🤩')

