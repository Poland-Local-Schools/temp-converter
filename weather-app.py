'''the temp converter will take degrees F and convert it to degrees Celcius and degrees Kelvin
We need: 
-a way to input temps.
-variable for that input
-the formula to convert f to c - (temp in f-32) * 5/9
-the formula to convert c to k (temp in c + 273.15)
-print statement to get the results'''

print("welcome to the temperature converter app!")
temp = input("what is the temp today? ")

temp_f = int(temp)

temp_c = (temp_f-32)*5/9
temp_k= temp_c+273.15
print(f"Todays temp is {int(temp_c)} degrees Celcius.")
print(f"Todays temp is {int(temp_k)} degrees Kelvin.")
