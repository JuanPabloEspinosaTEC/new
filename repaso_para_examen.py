lenght = float(input("enter lenght: "))
hight = float(input("enter hight: "))
print("The area of the rectangle is " + str(lenght * hight) + " cm2")

note1 = float(input("enter grade 1: "))
note2 = float(input("enter grade 2: "))
note3 = float(input("enter grade 3: "))
print("The avarage grade is " + str((note1 + note2 + note3) / 3))

Dolars = float(input("Enter the amount of dolars: "))
change = float(input("Whats the chage dolar to euro(1 dolar is = to how many euros): "))
print("The change for " + str(Dolars) + " is " + str(Dolars * change))

C = float(input("Enter temperature in Celcuis: "))
F = (C * 1.8) + 32
K = C + 273.15
print("The value in kelvins is " + str(K) + " and the value in Fahrengeit is " + str(F))

P = float(input("Enter value of product: "))
D = float(input("Enter discount product: "))
print("The final value is " + str(P * (100 - D) / 100))

P = float(input("Enter weight in KG: "))
H = float(input("Eneter hight in cm: "))
IMC = (P / H**2) * 10000
if IMC < 1.8:
  st = "LOW"
elif IMC < 24.9:
  st = "NORMAL"
elif IMC < 29.9:
  st = "HIGH"
else:
  st = "HIPER_HIGH"

print("your imc is " + str(IMC) + " and is " + st)
