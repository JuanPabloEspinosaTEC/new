PMesas = 170
PSillasA = 25
PCarpas = 630
PSillasN = 20
Total = 0
NA = int(input("Ingresa el numero de adultos: "))
NN = int(input("Ingrese el numero de niños: "))
Descuento = int(input("Ingrese el descuento(numero entero EJ: 20 es 20%): "))
TotalSillas = (NA * PSillasN) + (NN * PSillasA)
Total =+ TotalSillas
print("Total de sillas: " + str(TotalSillas) + " Pesos")
N = NA
MesasA = 0
while N > 0:
  N = N - 10
  MesasA = MesasA + 1
MesaA2 = MesasA
MesasA = MesasA * PMesas
N2 = NN
MesasN = 0
while N2 > 0:
  N2 = N2 - 10
  MesasN = MesasN + 1
mesa22 = MesasN
MesasN = MesasN * PMesas
print("Total de mesas para adultos: " + str(MesasA) + " Pesos")
print("Total de mesas para niños: " + str(MesasN) + " Pesos")
X = mesa22 + MesaA2
TotalC = 0
while X > 0:
  X = X - 6
  TotalC = TotalC + 1
TotalC = TotalC * PCarpas
print("Total de carpas: " + str(TotalC) + " Pesos")
SubTotal = (TotalSillas) + (MesasN) + (MesasA) + (TotalC)
print("Subtotal: " + str(SubTotal) + " Pesos")
Imp = float(SubTotal) * 0.16
print("El impuesto seria de " + str(Imp) + " pesos")
TotalFinal = SubTotal + Imp
print("Total ya con impuestos es de: " + str(TotalFinal) + " pesos")
Des = SubTotal / 100 * Descuento
print("El descuento es de: " + str(Des) + " pesos")
FIN = TotalFinal - Des
print("Total final con descuento: " + str(FIN))

