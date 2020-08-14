alumno = input("alumno=")

mate = {"luis":9.6 , "oscar":9.0 , "andy":8.5 , "arantza":8.0}

mate["alex"] = 9.0

 
quimica = {"luis":10 , "oscar":7.0 , "andy":7.8 , "arantza":7.5 , "alex":8.0}

quimica["yubi"] = 8.5


fisica = {"luis":9.6 , "oscar":9.0 , "andy":7.5 , "arantza":7.7 , "alex":7.9 , "yubi":7.0}

fisica["kat"] = 9.2
 

dibujo = {"luis":9.4 , "oscar":8.5 , "andy":8.0 , "arantza":8.0 , "alex":8.2 , "yubi":7.0 , "kat":8.5}

dibujo["fer"] = 9.6


if alumno in mate.keys() == False:
    mate.update({alumno : 0.0})

promedio = (mate[alumno] + quimica[alumno] + fisica[alumno] + dibujo[alumno])/4
print(promedio)
