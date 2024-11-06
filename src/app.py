#from controller.restauranteController import RestauranteController

#if __name__ == "__main__":
#    app = RestauranteController()
#    app.executar()
    
from flask import Flask, jsonify, request
from db import mysql, init_app
import config

app = Flask(__name__)
app.config.from_object(config)
init_app(app)

# Endpoint para listar todos os restaurantes
@app.route('/restaurantes', methods=['GET'])
def get_restaurantes():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM restaurantes")
    rows = cursor.fetchall()
    cursor.close()
    restaurantes = [{"id": row[0], "nome": row[1], "ativo": bool(row[2]), "categoria": row[3]} for row in rows]
    return jsonify(restaurantes)

# Endpoint para buscar restaurante por ID
@app.route('/restaurantes/<int:id>', methods=['GET'])
def get_restaurante(id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM restaurantes WHERE id = %s", (id,))
    row = cursor.fetchone()
    cursor.close()
    if row:
        restaurante = {"id": row[0], "nome": row[1], "ativo": bool(row[2]), "categoria": row[3]}
        return jsonify(restaurante)
    return jsonify({"mensagem": "Restaurante não encontrado"}), 404

# Endpoint para adicionar restaurante
@app.route('/restaurantes', methods=['POST'])
def add_restaurante():
    data = request.get_json()
    nome = data.get('nome')
    ativo = data.get('ativo', True)
    categoria = data.get('categoria')
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO restaurantes (nome, ativo, categoria) VALUES (%s, %s, %s)",
                   (nome, ativo, categoria))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensagem": "Restaurante adicionado com sucesso"}), 201

# Endpoint para atualizar restaurante
@app.route('/restaurantes/<int:id>', methods=['PUT'])
def update_restaurante(id):
    data = request.get_json()
    nome = data.get('nome')
    ativo = data.get('ativo')
    categoria = data.get('categoria')
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE restaurantes SET nome = %s, ativo = %s, categoria = %s WHERE id = %s",
                   (nome, ativo, categoria, id))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensagem": "Restaurante atualizado com sucesso"}), 200

# Endpoint para deletar restaurante
@app.route('/restaurantes/<int:id>', methods=['DELETE'])
def delete_restaurante(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM restaurantes WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return jsonify({"mensagem": "Restaurante deletado com sucesso"}), 200

if __name__ == '__main__':
    app.run(debug=True)
