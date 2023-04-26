age =  input("  What is your current age? ")
new_Age = 90 - int(age)
months = new_Age * 12
weeks = new_Age * 52
days = new_Age * 365
message = f"You have {days} days, {weeks} weeks, {months} months left"
print(message)
