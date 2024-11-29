from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

# Usa o nome do módulo para configurar a raiz do projeto.
app = Flask(__name__)
# Permite que navegadores realizem requisições para o back-end Flask mesmo se estiverem hospedados em domínios ou portas diferentes.
CORS(app)



# Criar usuário
# vai ter uma route e um method
@app.route('/users', methods=['POST'])
def create_user():
    # O data esta vindo do javascript json
    data = request.json
    # todos vão ter um conn e cursor
    conn = get_connection()
    cursor = conn.cursor()

    # Vai usar o json cuja key são os IDs
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", 
                   (data['name'], data['email'], data['age']))
    conn.commit()
    return jsonify({"message": "User created successfully"}), 201

# Listar usuários
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_connection()
    #  vai buscar como dicionario
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users")

    # Ele vai buscar todos como fetchall
    users = cursor.fetchall()
    return jsonify(users), 200

# Atualizar usuário
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET name=%s, email=%s, age=%s WHERE id=%s", 
                   (data['name'], data['email'], data['age'], id))
    conn.commit()
    return jsonify({"message": "User updated successfully"}), 200

# Deletar usuário
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=%s", (id,))
    conn.commit()
    return jsonify({"message": "User deleted successfully"}), 200


# Produto

# PRODUTOS
@app.route("/produtos", methods=["POST"])
def add_produto():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO produtos(nome,marca,valor)
    VALUES(%s,%s,%s)
    """, (data["nome"], data["marca"], data["valor"]))
    conn.commit()
    return jsonify({"message": "Product created successfully"}), 201

@app.route("/produtos", methods=["GET"])
def pegarProdutos():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM produtos")
    products = cursor.fetchall()
    return jsonify(products), 200



#Trabalhando com uma procedure

@app.route("/produtos/procedure", methods=["POST"])
def add_produto_procedure():
    data = request.json  # Dados enviados no corpo da requisição

    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Chamada para a procedure
        cursor.execute("""
        CALL InsertProduto(%s, %s, %s)
        """, (data["nome"], data["marca"], data["valor"]))

        conn.commit()
        return jsonify({"message": "Product created successfully via procedure"}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to insert product"}), 500

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    app.run(debug=True)
