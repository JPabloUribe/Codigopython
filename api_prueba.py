from flask import Flask, request, jsonify #request para ver los datos enviados en solicitudes, jsonify convierte py  a json 
from flask_cors import CORS


app = Flask(__name__)  
CORS(app)

list_jugadores = []

# Crear jugador
@app.route('/crear_jugador', methods=["POST"])
def crear_jugador():
    try:
        jugador = request.get_json()

        list_jugadores.append({
            "nombre": jugador["nombre"],
            "edad": jugador["edad"],
            "estatura": jugador["estatura"]
        })
        return jsonify(list_jugadores)
    except Exception as e:
        return {"Error": f"El error es: {e}"}, 404

# Leer todos los jugadores 
@app.route('/leer', methods=["GET"])
def mostrar_jugadores():
    try:
        if not list_jugadores:
            return {"error": "No hay jugadores registrados"}
        return jsonify(list_jugadores)
    except Exception as e:
        return {"Error": f"El error es: {e}"}, 404

# Actualizar jugador 
@app.route('/actualizar_jugador', methods=["PUT"])
def actualizar_jugador():
    try:
        datos = request.get_json()
        nombre = datos.get("nombre")
        nuevo_dato = datos.get("nuevo_dato")
        parametro = datos.get("parametro")

        for jugador in list_jugadores:
            if jugador["nombre"] == nombre:
                if parametro == "edad":
                    jugador["edad"] = nuevo_dato
                elif parametro == "estatura":
                    jugador["estatura"] = nuevo_dato
                return jsonify(jugador)

        return {"error": "Jugador no encontrado"}
    except Exception as e:
        return {"Error": f"El error es: {e}"}, 404

# Eliminar jugador (DELETE) opcion sacada de chat gpt 
# @app.route('/eliminar_jugador', methods=["DELETE"])
# def eliminar_jugador():
#     try:
#         datos = request.get_json()
#         nombre = datos.get("nombre")

#         jugador_a_eliminar = None
#         for jugador in list_jugadores:
#             if jugador["nombre"] == nombre:
#                 jugador_a_eliminar = jugador
#                 break

#         if jugador_a_eliminar:
#             list_jugadores.remove(jugador_a_eliminar)
#             return jsonify(list_jugadores)
#         else:
#             return {"error": "Jugador no encontrado"}
#     except Exception as e:
#         return {"Error": f"El error es: {e}"}, 404

# Eliminar jugador 
@app.route('/eliminar_jugador', methods=["DELETE"])
def eliminar_jugador():
    try:
        opcion = request.get_json()
        nombre = opcion.get("nombre")

        for i, jugador in enumerate(list_jugadores):
            if jugador["nombre"] == nombre:
                list_jugadores.pop(i)
                return {"message": "Jugador eliminado", "jugadores": list_jugadores}

        return {"error": "Jugador no encontrado"}, 404
    except Exception as e:
        return {"Error": f"El error es: {e}"}, 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
