#!encoding:UTF-8
#!/usr/bin/python


print "Introduzca el nombre del fichero donde se encuentran los resultados: "
nombre_fichero = raw_input()

try:
  fichero = open(nombre_fichero)
except:
  print "El nombre del fichero introducido es incorrecto"

linea=fichero.readline()
while (linea != ""):
  aproxima = int (linea.split()[2])
  print ("nº de intervalos: %d" % (aproxima))
  for i in range (5):
    linea = fichero.readline()
    porcentaje = linea.split()[0]
    umbral = float(linea.split()[6])
    print ("%s de fallos para el umbral %2.5f" %(porcentaje,umbral))
  linea=fichero.readline()
