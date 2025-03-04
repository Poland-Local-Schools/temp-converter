'''The temp convert will take degrees F to C to K

We need:
1. a way to input temos
2. Variable for that input
3. the formula to convert F to C - (temp in F - 32) * 5/9
4. the formula to convert C to K - (temp in C + 273.15)
5. Print statemnt and get results'''

print("welcome to my temp converter app!")

temp = input("what is the temp today? ")


temp_f = int(temp) # this line converts the string from our input into a number

temp_c = int((temp_f-32)*5/9) # this converts f to c as a whole number 


temp_k = (temp_c+273.15)

print(f"todays temp is \n{temp_c} degrees Celsius!")
print(f"todays temp is \n{temp_k} degrees Kelvin!")
