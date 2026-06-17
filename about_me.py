#1. Setting up variables
first_name = "Robert"
last_name = "Green"
age = 44
city = "Cincinnati"
job = "Insurance Agent"
why_code = "I want to learn how to code to change my career"
fun_fact = "I workout everyday"

#2.Printing header with string multiplication trick
print (f"="* 40)
print (f"Student Profile")
print (f"="* 40)

#Printing the formatted profile using f-strings for better readability
print (f"Name: {first_name} {last_name}")
print (f"Age: {age}")
print (f"City: {city}")
print (f"Job: {job}")
print (f"\n Why I'm learning to code:")
print (f'"{why_code}"')
print (f"\nFun Fact: {fun_fact}")
print (f"="* 40)