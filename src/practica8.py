#!/usr/bin/python
#!encoding: UTF-8
import sys
import modulo8


argumentos=sys.argv[1:]
if(len(argumentos)==2):
      n=int(argumentos[0])
      aproxima = int(argumentos[1])
      umbral=[]
      for i in range(2,7):
	umbral.append(float(argumentos[i]))
      nombre_fichero = argumentos[7]
else:       
      n=(int(raw_input("Introduzca el nº de intervalos (n>0)")))
      aproxima =(int(raw_input("Introduzca el nº de aproximaciones")))
      print "introduzca 5 umbrales de error: "
      umbral=[]
      for i in range(5):
	  print "Introduzca el umbral", i,":"
	  umbral.append(float(raw_input()))
      nombre_fichero=raw_input("Introduzca el nombre del fichero para almacenar los resultados: ")
      
if (n>0):
      try:
	fichero = open (nombre_fichero, "a")
      except: 
	fichero = open (nombre_fichero, "w")
      fichero.write("nº intervalos: %d\n" % (aproxima))
      for i in range(5):
	  porcentaje = modulo8.error (n,aproxima, umbral[i])
	  fichero.write("%2.2f%% de fallos para el umbral %2.5f\n" % (porcentaje, umbral[i]))
      fichero.close()
      
     