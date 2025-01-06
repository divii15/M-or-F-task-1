#TASK 1
#6)find user is Male or Female
#input:Male
#ouput:user is Male


Gender = input("Enter your gender: ")
if Gender == "Male" or Gender == "male" or Gender == "MALE":
    print("User is Male")
elif Gender == "Female" or Gender == "female" or Gender == "FEMALE":
    print("User is Female")
else:
    print("Invalid input")
