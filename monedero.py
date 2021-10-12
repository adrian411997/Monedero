import requests #esto hace que el programa use el modulo requests que se usa para consulta APIS, para usar este import tuviste que instalarlo con pip install requests en la terminal de windows
from io import open
from datetime import date

def esmoneda(cripto):#funcion que verifica que la moneda ingresada este dentro de la tupla llamada monedas
    return cripto.upper() in monedas

def nombre(cripto): #funcion que recibe el simbolo y retorna el nombre
    monedas_dict={}
    for coin in data["data"]:
        monedas_dict[coin["symbol"]]=coin["name"]
    return monedas_dict.get(cripto) #devuelve el nombre
def entero(variable):
	try:
		int(variable)
		return True
	except:
		return False

#inicializamos elemento
monedas=()
diccionario={}

COINMARKET_API_KEY = "8eab9534-756d-4565-8a12-1316dce891e5" # Esta es la llave de la API que nos permite hacer peticiones a la direccion URL de la API
headers = { #esto son los parametros que necesitamos pasar en la peticion para que la API nos pueda devolver la informacion
  'Accepts': 'application/json', # esto indica que el formato de la respuesta de la API sera JSON, que es un formato legible para Python, asi podra usar la informacion
  'X-CMC_PRO_API_KEY': COINMARKET_API_KEY #aqui asignamos que usaremos la clave de la API que definimos arriba
}
mis_posesiones = {}
mi_code = "1"
code_comp = 2
data=requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json() #aqui almacenamos  en data el resultado de la peticion a la direccion de la API usando requests.get y pasamos los parametros que definimos arriba
for cripto in data["data"]:# aqui creamos un for para recorrer todos los datos o cripto como se especifica en el for que estan en "data" que es el valor dentro de la variable data que tiene todas las criptomonedas de la API
    diccionario[cripto["symbol"]]=cripto["quote"]["USD"]["price"] #cada que recorremos la data almacenamos en el diccionario los datos de symbolo que es la abreviacion por ejemplo BTC junto con el precio de la moneda que consulta con quote.USD.price en el json
monedas = diccionario.keys() #almecenamos en monedas los simbolos del diccionario con el metodo keys()
 #imprimimos la variable monedas para verificar que elementos quedaron guardados 
eleccion = int(input("Menu principal: \n 1 - Recibir cantidad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
while eleccion != 0:
    if eleccion == 1:
        print("\nHaz seleccionado Recibir cantidad")
        print("Los codigos otorgados para este ejercicio serán de " + str(mi_code) + " para el usuario y el del quien vamos a pedir será de " + str(code_comp))
        verif_user = input("Ingrese su codigo de usuario para incializar la petición: ")
        while entero(verif_user) == False: #Validamos la entra del codigo por si es un numero
            print("Ingrese un numero")
            verif_user = input("Ingrese su codigo de usuario para inicalizar la petición: ")
        while verif_user != mi_code: #Si hemos ingresado un numero, entonces se procederá a realizar la verificacion si coincide con el codigo establecido
            print("El código ingresado es incorrecto, por favor, ingrese el código correcto")
            verif = int(input("Ingrese su codigo de usuario para inicalizar la petición: "))
        print("Codigo aceptado")
        while True:
            moneda=input("Indique el nombre de la moneda que desea recibir: ").upper() #ingresamos la moneda a verificar
            while not esmoneda(moneda.upper()): #validamos que la moneda cumpla la validacion de la funcion esmoneda en que caso de que no sea moneda seguira pidiendo el dato hasta que lo sea
                print("Moneda Invalida.")
                moneda=input("Ingrese el nombre de la moneda: ")
            ing = int(input("Ingrese la cantidad que desea pedir: "))
            verif_comp = int(input("Ingrese el codigo del usuario al que desea pedir: "))
            while verif_comp != code_comp:
                print("El código no pertenece a un usuario activo")
                verif_comp = int(input("Ingrese el codigo del usuario al que desea pedir: "))
            if moneda in mis_posesiones: #Aqui se usa las condicionales por si la moneda que se ingreso ya existe en nuestras pertenencias, los valores se suman, de lo contrario, se agregará al diccionario,
                mis_posesiones[moneda] += ing
            else:
                mis_posesiones[moneda] = ing
            print(mis_posesiones)
            print("La operacion se ha ejecutado con éxtio")
            operacion = "Pedido"
            archivo_text = open("Registros.txt", "a") #Procedemos a crear un txt para almacenar los registros de nuestros movimientos.
            fecha = str(date.today())
            archivo_text.write("\n" + "\nTipo: " + operacion + "\nFecha: " + str(fecha) + "\nMoneda: " + moneda + "\nCantidad: " + str(ing) + "\nCódigo: " + str(mi_code) + "\nMonto: " + str(mis_posesiones))
            archivo_text.close()
            decision = int(input("¿Desea realizar otro pedido? \n 1 - Si \n 2 - No \n Su eleccion: ")) #Por si queremos repetir otra vez la operación.
            if decision == 2:
                eleccion = int(input("Menu principal: \n 1 - Recibir cantidad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                break
            else:
                continue
    elif eleccion == 2:
        print("\nHaz seleccionado Transferir monto")
        while True:
            verif_user = input("Ingrese su codigo de usuario para proceder con la transferencia: ")
            while entero(verif_user) == False:
                print("Ingrese un numero")
                verif_user = int(input("Ingrese su codigo de usuario para proceder con la transferencia: "))
            while verif_user != mi_code:
                print("El código ingresado es incorrecto, por favor, ingrese el código correcto")
                verif = int(input("Ingrese su codigo de usuario para proceder con la transferencia: "))
            moneda=input("Indique el nombre de la moneda que desea transferir: ").upper()
            while not esmoneda(moneda): #validamos que la moneda cumpla la validacion de la funcion esmoneda en que caso de que no sea moneda seguira pidiendo el dato hasta que lo sea
                print("Moneda Invalida.")
                moneda=input("Ingrese el nombre de la moneda: ")
            if moneda in mis_posesiones:
                trans = int(input("Indique la cantidad de " + moneda + " que desea transferir: "))
                verif_comp = int(input("Ingrese el codigo del usuario al que desea transferir: "))
                while verif_comp != code_comp:
                    print("El código no pertenece a un usuario activo")
                    verif_comp = int(input("Ingrese el codigo del usuario al que desea transferir: "))
                if trans > mis_posesiones[moneda]: #Una condicional por si lo que queremos transferir, excede a lo que tenemos
                    print("El valor deseado excede a sus pertenencias actuales")
                else:
                    mis_posesiones[moneda] -=trans
                    print("La operacion se ha ejecutado con éxtio")
                    operacion = "Transferencia"
                    archivo_text = open("Registros.txt", "a")
                    fecha = str(date.today())
                    archivo_text.write("\n" +"\nTipo: " + operacion + "\nFecha: " + str(fecha) + "\nMoneda: " + moneda + "\nCantidad: " + str(trans) + "\nCódigo: " + str(mi_code) + "\nMonto: " + str(mis_posesiones))
                    archivo_text.close()
                    decision = int(input("¿Desea realizar otro pedido? \n 1 - Si \n 2 - No \n Su eleccion: "))
                    if decision == 2:
                        eleccion = int(input("Menu principal: \n 1 - Recibir cantidad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                        break
                    else:
                        continue
            else:
                print("No se encontró " + moneda + " dentro de sus pertenencias")
                decision = int(input("¿Desea realizar otra transferencia? \n 1 - Si \n 2 - No \n Su eleccion: "))
                if decision == 2:
                    eleccion = int(input("Menu principal: \n 1 - Recibir cantidad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                    break
                else:
                    continue
    elif eleccion == 3:
        print("\nHaz seleccionado Mostrar balance de una moneda")
        while True:
            moneda=input("Indique el nombre de la moneda que desea consultar: ").upper() #ingresamos la moneda a verificar
            while not esmoneda(moneda): #validamos que la moneda cumpla la validacion de la funcion esmoneda en que caso de que no sea moneda seguira pidiendo el dato hasta que lo sea
                print("Moneda Invalida.")
                moneda=input("Ingrese el nombre de la moneda: ")
            if moneda in mis_posesiones: #No se si la actividad era asi, pero solo se podrá pedir el balance de una moneda si esta, existe dentro de nuestras posesiones.
                total = diccionario[moneda] * mis_posesiones[moneda]
                print("El nombre de la moneda " + moneda + " es: " + nombre(moneda)+ "\n Posee un total de " + str(mis_posesiones[moneda]) + "\n Su saldo actual de esta moneda es de: " + str(round(total,2)))
                operacion = "Balance de moneda"
                archivo_text = open("Registros.txt", "a")
                fecha = str(date.today())
                archivo_text.write("\n" + "\nTipo: " + operacion + "\nFecha: " + str(fecha) + "\nMoneda: " + moneda + "\nCódigo: " + str(mi_code) + "\nMonto: " + str(round(total,2)))
                archivo_text.close()
                decision = int(input("¿Desea consultar otra moneda? \n 1 - Si \n 2 - No \n Su eleccion: "))
                if decision == 2:
                    eleccion = int(input("Menu principal: \n 1 - Recibir cantitdad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                    break
                else:
                    continue
            else:
                print("No se encontró " + moneda + " dentro de sus propiedades actuales")
                decision = int(input("¿Desea consultar otra moneda? \n 1 - Si \n 2 - No \n Su eleccion: "))
                if decision == 2:
                    eleccion = int(input("Menu principal: \n 1 - Recibir cantidad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                    break
                else:
                    continue
    elif eleccion == 4:
        print("\nHaz seleccionado Mostrar balance general")
        while True:
            if len(mis_posesiones) != 0:
                total = 0
                for element in mis_posesiones.keys():
                    total += diccionario[element] * mis_posesiones[element] 
                    print(element + ":\n Tiene un total de: " + str(mis_posesiones[element]) + "\n Su total en USD es : " + str(diccionario[element] * mis_posesiones[element]))
                print("Poseé un monto tal de: USD " + str(round(total,2)))
            else:
                print("Acualmente, usted no posee criptomonedas en sus posesiones\nRealice un pedido u otra acción")
                eleccion = int(input("Menu principal: \n 1 - Recibir canitdad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
                break
            operacion = "Balance general"
            archivo_text = open("Registros.txt", "a")
            fecha = str(date.today())
            archivo_text.write("\n" + "\nTipo: " + operacion + "\nFecha: " + str(fecha) + "\nCódigo: " + str(mi_code) + "\nMonto: USD " + str(round(total,2)))
            archivo_text.close()
            eleccion = int(input("Menu principal: \n 1 - Recibir canitdad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
            break
    elif eleccion == 5:
        print("\nHaz seleccionado Mostrar historial de transacciones")
        while True:
            archivo_texto = open('Registros.txt','r')
            texto = archivo_texto.read()
            print(texto)
            archivo_texto.close()
            eleccion = int(input("Menu principal: \n 1 - Recibir canitdad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n Su eleccion: "))
            break
    elif eleccion == 6:
        print("Gracias por usar el programa. Hasta luego")
        break
    else:
        print("Seleccione uno de los digitos correspondientes")
        eleccion = int(input("Menu principal: \n 1 - Recibir canitdad \n 2 - Transferir monto \n 3 - Mostrar balance de una moneda \n 4 - Mostrar balance general \n 5 - Mostrar historial de transacciones \n 6 - Salir del programa \n"))
