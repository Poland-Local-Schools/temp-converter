'''the temp converter will take degrees F(Fahrenheit) and convert it to 
degreees C(Celsius) and degrees K(Kelvin)

We need:
1. A way to input temperatures.
2. Variable for that input.
3. The formula to convert F to C - (temp in F-32) * 5/9
4. Formula to convert C to K - (temp in C+273.15) 
5. Print statement to get the results. '''

print("Welcome to my temperature converter app!\n")

temp = input("what is the temp today? ") # This line asks the user for an anser (input).

temp_f = int(temp) #This line converts the string from our input into a number.

temp_c = int((temp_f-32)*5/9) # converts F to C as a whole number. DONT FORGET THE DOUBLE (()).

temp_k = temp_c + 273.15

print(f"\nToday's temp is {temp_c} degrees Celcius!\n")
print(f"Today's temp is {temp_k} degrees Kalvin!\n")

