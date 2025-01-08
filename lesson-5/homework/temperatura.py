def convert_cel_to_far(selsiy = float(input("Enter a temperature in degrees C: "))):
    farangeyt = selsiy * 9/5 + 32  
    return f"{selsiy} degrees C = {round(farangeyt, 2)} degrees F"



def convert_far_to_cel(F = float(input("Enter a temperature in degrees F: "))):
    C = (F - 32) * 5/9
    return f"{F} degrees F = {round(C, 2)} degrees C"

print(convert_cel_to_far())
print(convert_far_to_cel())