from flask import Flask, jsonify, request
app = Flask(__name__)

Lista_itens = ['Bruno']

@app.route('/itens', methods=['GET'])
def pegar_itens():
    return jsonify(Lista_itens)

@app.route('/add_lista', methods=['POST'])
def add_item():
    data = request.get_json()
    novo_item = {'id': len(Lista_itens) + 1, 'nome': data['nome']}
    Lista_itens.append(novo_item)
    return jsonify(novo_item)

@app.route('/item/<int:item_id>', methods=['GET'])
def pegar_cada_item(item_id):
    resultado='Não encontrado'
    for valor in Lista_itens:
        if item_id ==valor['id']:
         resultado =valor
    return jsonify(resultado)

@app.route('/deletar_item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    resultado = 'Nao encontrado'
    for valor in Lista_itens:
        if item_id == valor['id']:
            Lista_itens.remove(valor)
            resultado='Removido com sucesso'
    return jsonify(resultado)

@app.route('/atualizar_item/<int:item_id>', methods=['PUT'])
def atualizar_item(item_id):
    resultado = 'Nao encontrado'
    for valor in Lista_itens:
        if item_id == valor['id']:
            data = request.get_json()
            valor['nome']=data['nome']
            resultado='Atualizado com sucesso'
    return jsonify(resultado)



if __name__ == '__main__':
    app.run(debug=True)
