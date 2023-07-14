def año_bisiesto(bisiesto):
    if bisiesto % 4 ==0:

            if bisiesto % 100 !=0:

                print("es bisiesto")

            else:

                print("no es bisiesto")
    else:
        print("no es bisiesto")

print("digite un año")

año=int(input())

año_bisiesto(año)
