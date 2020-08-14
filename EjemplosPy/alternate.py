# lista basta 
lista = ["antonio", "altamirano" , "avestruz" , "arandano" , "audi" , "arbol" , "arabia saudita" , "bernardo" , "bustos" , "buey" , "bugambilia" , "bayern" , "bebida" , "botswana" , "carlos" , "cretin" , "campañol" , "cereza" , "cartoon network" , "cajeta" , "chile" , "demian" , "diaz" , "delfin" , "durazno", "dove" , "detergente" , "durango" , "eugenio" , "encalada" , "elefante" , "enebro" , "echo" , "engrane" , "eslovaquia" , "fernanda" , "fuentes" , "flamingo" , "frambuesa" , "factis" , "foco" , "francia", "gerardo" , "gutierrez" , "garrapata" , "gardenia" , "gap" , "gelatina" , "guatemala" , "hector" , "herrera" , "hormiga" , "higuera" , "huawei" , "hoz" , "hidalgo" , "ignacio" , "itzel" , "iguana" , "iris" , "intel" , "impresora" , "inglaterra" , "josue" , "jimenez" , "jirafa" , "jitomate" , "jelly belly" , "jicaleta" , "jamaica" , "karla" , "king" , "koala" , "kiwi" , "kellogs" , "kilobytes" , "kenya" , "luis" , "lozano" , "lagarto" , "lima" , "lenovo" , "led" , "lituania" , "maritza" , "mejia" , "mariquita" , "milenrama" , "mcdonals" , "medalla" , "mexicali" ,"nicolas" , "nacher", "nutria" , "nebeda" , "nissan" , "nitrogeno" , "nigeria" , "octavio" , "ordaz" , "oso hormiguero" , "orquidea" , "oreo" , "octanol" , "oregon" , "pedro" , "paz" , "perdiz" , "papaya" , "pelikan" , "polonio" , "polonia" , "quetzalcoatl" , "quintero" , "quetzal" , "quinoa" , "quacker state" , "queso" , "quintana roo" , "rodrigo" , "rodriguez" , "rata" , "romero" , "renault" , "rehilete" , "roma" , "saul" , "sosa" , "serpiente" , "sauco" , "samsonite" , "sacapuntas" , "suecia" , "tiana" , "tejada" , "tejon" , "tomillo" , "tesla" , "timon" , "taiwan" , "uriel" , "ubeda" , "urraca" , "uva" , "ubisoft" , "uracilo" , "uruguay" , "vanya" , "viedas" , "vibora" , "vaina" , "vans" , "viento" , "vaticano" , "walter" , "washington" , "wombat" , "wasabi" , "windows" , "whisky" , "wellington" , "wellington" , "ximena" , "xocoyotzin" , "xoloitzcuincle" , "xigua" , "xiaomi" , "xilofono" , "xalapa", "yolanda" , "yaniz" , "yegua" , "yuca" , "yamaha" , "yoyo" , "yugoslavia" , "zlatan" , "zapien" , "zarigueya" , "zarza" , "zara" , "zepelin" , "zacatecas"] 
marcas = ["apple", "dove", "hersheys"]
paises = ["mexico", "paraguay", "brasil"]

# hacemos nuestro check 
check_categoria = input("pon tu categoría: ")
check = input("Letra: ")

# utilizamos algunos algoritmos de comprensión 
# y buscamos que empieze con x letra 
if check_categoria == "paises":
    res = [i for i in paises if i[0].lower() == check.lower()] 
elif check_categoria == "marcas":
    res = [i for i in marcas if i[0].lower() == check.lower()] 
else:
    res = "no hay palabras que empiecen con esa letra" 

#resultado 
print("BASTA: "+ "Las palabras que empiezan con " + str(check) + " son: " + str(res))
