# ANSWER =============================
groups = [1,2,3,4,5,6,7,8,9,10]

name = input("Please enter your name:")
age = input("Please enter your age:")
kills = input("Please enter confirmed kills:")
years = input("Please input years of service:")
group = int(input("Please enter combat group:"))
while True:
    if group in groups:
        print("Welcome",name)
        break
    else:
        print("Invalid Group Number")
        group = int(input("Please enter combat group:"))
if age > 30:
	print("$1000 has been transfered to your bank account")
elif age < 30:
	print("$500 has been transfered to your bank account")
elif kills > 10:
	print("You've been given a ticket to claim the lightsaber in the dispensary")
elif years > 10:
	print("$5000 has been transfered to your bank account")