import tabula
import re
import sys
import os

v = set()
f = set()


def cls():
    os.system('cls' if os.name=='nt' else 'clear')

df = tabula.read_pdf("baremos.pdf", pages='all', lattice=True)

nanxv = [9,10,14,18,22,27,31,40,46]
nanxf = [43]
nansum = 0
impssv = [6,13,17,24,26,30,34,39,42,49]
impssf = []
impsssum = 0
actv = [1,5,12,25,29,36,41,48]
actf = [16,21]
actsum = 0
syv = [8,23,38,47]
syf = [4,15,20,28,33,45]
sysum = 0
aggv = [2,3,19,32,35,37,50]
aggf = [7,11,44]
aggsum = 0
offset = 0


edad = int(input("Cuantos años tienes?\n"))
while(edad<18):
    print("Debes ser mayor a 18 años\n")
    edad = int(input("Cuantos años tienes?\n"))

if 18<= edad <=24:
    tablenumber=0
elif 25<= edad <=30:
    tablenumber=1
elif 31<= edad <=45:
    tablenumber=2
elif 46<= edad <=60:
    tablenumber=3
else:
    tablenumber=4
sexo = input("1.Hombre\n2.Mujer\n")

if (int(sexo) == 1):
    offset = 5
    sexo = "hombres"
elif (int(sexo) == 2):
    sexo = "mujeres"
else:
    while (sexo != 1 or sexo !=2):
        print("Sexo elegido es invalido\n")
        sexo = input("1.Hombre\n2.Mujer\n")

rowoffset = len(df[tablenumber])-4

with open('preguntas.txt', encoding='utf8') as file:
    for line in file:
        inp = input(line.strip() + "\n")
        if inp.lower() == "v":
            v.add(int(line.strip().split(".")[0].strip()))
        elif inp.lower() == "f":
            f.add(int(line.strip().split(".")[0].strip()))
        else:
            while(inp.lower() == "v" or inp.lower() == "f"):
                print('Seleccion invalida, use V/F\n')
                inp = input(line.strip() + "\n")
        cls()
for verdadero in v:
    if (verdadero in nanxv):
        nansum+=1
    elif (verdadero in impssv):
        impsssum+=1
    elif (verdadero in actv):
        actsum+=1
    elif (verdadero in syv):
        sysum+=1
    elif (verdadero in aggv):
        aggsum+=1

for falso in f:
    if (falso in nanxf):
        nansum+=1
    elif (falso in impssf):
        impsssum+=1
    elif (falso in actf):
        actsum+=1
    elif (falso in syf):
        sysum+=1
    elif (falso in aggf):
        aggsum+=1

#nansum = 2
#impsssum = 7
#actsum = 7
#sysum = 3
#aggsum = 3

print("\n")
print("Neuroticismo ansiedad (N-Anx): "+ str(nansum) + "\n")
print("Impulsividad-Búsqueda de sensaciones (ImpSS): "+ str(impsssum) + "\n")
print("Actividad (Act): "+ str(actsum) + "\n")
print("Sociabilidad (Sy): "+ str(sysum) + "\n")
print("Agresividad-Hostilidad (AggHost): "+ str(aggsum) + "\n\n")

print("El %s de los %s es menos ansioso que tu\n" % (df[tablenumber].loc[rowoffset - nansum][1 + offset],sexo))
print("El %s de los %s es menos impulsivo que tu\n" % (df[tablenumber].loc[rowoffset - impsssum][2 + offset],sexo))
print("El %s de los %s es menos activo que tu\n" % (df[tablenumber].loc[rowoffset - actsum][3 + offset],sexo))
print("El %s de los %s es menos sociable que tu\n" % (df[tablenumber].loc[rowoffset - sysum][4 + offset],sexo))
print("El %s de los %s es menos agresivo que tu\n" % (df[tablenumber].loc[rowoffset - aggsum][5 + offset],sexo))


