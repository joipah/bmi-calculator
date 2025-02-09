def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
 
 
def lb_to_kg(lb):
    
    return lb * 0.4535923
 
 
def bmi(weight, height):
    results= weight / height ** 2
    print("Your BMI is", results)
    if height < 1.0 or height > 2.5 or weight < 20 or weight > 200:

        return None
unit=input("Enter 'lb' or 'kg'").lower()
if unit =='lb':
    weight=float(input("Enter weight in pounds:"))
    weight= weight * 0.4535923
elif unit=='kg':
    weight=float(input("Enter weight in kg:"))
else:
    print("Enter the specified values")
    exit()
  
    

height_ft=float(input("Enter ft:"))
height_in=float(input("Enter inches:")) #if inches is zero, enter 0


bmi(weight, height=ft_and_inch_to_m(height_ft, height_in))