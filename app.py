from flask import Flask, request, jsonify
from flask_cors import CORS



app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    return '<h1>Hola, me llamo Eduardo 😋</h1>'

@app.route('/misDatos', methods=['GET'])
def getData():
	response = {
		"carne": 201900772,
		"Nombre": "Mynor Eduardo Peñate Velasquez"
	}
	return response
@app.route('/inversor', methods=['POST'])
def invertData():
	response = {}
	text = request.form.get('cadena_entrada')
	response["Texto invertido"]=text[::-1]
	return response
@app.route('/comprobarNIT', methods=['POST'])
def checkNit():
	response = {}
	nit = request.form.get('no_nit')
	response['resultado'] = validar_nit(nit)
	return (response)


# Validar nit

def validar_nit(nit):
    '''Funcion para validar NIT'''
    # Elimina espacios en blanco
    nit_n = nit.replace(' ', '')
    # Elimina el guion del nit
    nit_ok = nit_n.replace('-', '')
    # Base para multiplicar
    base = 1

    # Guarda el digito validador, el ultimo
    dig_validador = nit_ok[-1]

    # Guarda el resto de numeros para sumar
    dig_nit = list(nit_ok[0:-1])

    # Reverse invierte el orden de los digitos del original
    # El array inverso se refleja al original
    dig_nit_rev = dig_nit.reverse()  # None

    try:
        suma = 0
        # Por cada numero del nit en inversa
        for n in dig_nit:
            base += 1
            suma += int(n) * base

        # Guarda el residuo
        resultado = suma % 11
        comprobacion = 11 - resultado

        if suma >= 11:
            resultado = suma % 11
            comprobacion = 11 - resultado

        if comprobacion == 10:
            if dig_validador.upper() == 'K':
                return True

        elif comprobacion == int(dig_validador):
            return True

        else:
            return False

    except:
        return False


# Codigo extra

@app.route('/pokemon', methods=['GET','POST'])
def pokemon():

	response = {}

	if request.method == 'POST':

		nombre_p = request.form.get('nombre_poke')
		especie_p = request.form.get('especie_poke')
		tipo_p = request.form.get('tipo_poke')
		foto_p = request.form.get('foto_poke')

		if mis_pokemon.crear(nombre_p,especie_p,tipo_p,foto_p) == True:

			response['estado'] = 1
			return response

		response['estado'] = 0
		return response

	if request.method == 'GET':

		return  mis_pokemon.devolver_pokemon()

if __name__ == "__main__":
	app.run(threaded=True, port=5000,debug=True)