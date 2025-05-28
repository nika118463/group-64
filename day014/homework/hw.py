#false
#true
#true

temperature = int(input("enter temprature: "))

cooling_on = (temperature > 30) 

if cooling_on:
    print("cooling on.")
else:
    print("cooling off.")