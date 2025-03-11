def classify_age(age):
    if age < 0:
        print("Invalid age. Please enter a valid integer. ")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teenager.")
    elif age <= 64:
        print("You are an Adult. ")
    else:
        print("You are a Senior")
        
while True:
    try:
        age = int(input("How old are you? "))
        classify_age(age)
    except ValueError:
        print("Invalid Input. Please enter a valid integer. ")
        
    more = input("Other more to classify? (yes/no): ")
    if more.lower() !='yes':
        print("Exiting the program.")
        break
    
   