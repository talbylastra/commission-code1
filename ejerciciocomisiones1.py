'''La empresa XXXXXX S.A. tiene la siguiente tabla
de parametros para pagar las comisiones de sus empleados 
o ejecutivos de venta:
1. Entre 2000000 - 10000000 el 7%
2. Entre 10000000 - 20000000 el 10%
3. Mayor 20000000 el 20%
'''
nombre = (input('Ingrese nombre vendedor '))
comision = int(input('Ingrese total ventas '))
if comision >= 2000000 and comision < 10000000:
    extra = comision*0.07
    print(float('{:.2f}'.format(extra)))
elif comision > 10000000 and comision < 20000000:
    extra = comision*0.10
    print(float('{:.2f}'.format(extra)))
elif comision >= 20000000:
    extra = comision*0.20
    print(float('{:.2f}'.format(extra)))
else:
    print('No tiene comision')

    
    
