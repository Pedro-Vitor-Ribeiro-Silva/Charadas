import random
import os,json
import firebase_admin
from flask import Flask,jsonify,request
from flask_cors import CORS
from firebase_admin import credentials,firestore
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

FBKEY=json.loads(os.getenv('CONFIG_FIREBASE'))

cred = credentials.Certificate(FBKEY)
firebase_admin.initialize_app(cred)

db = firestore.client() #conecta ao db do firebase


@app.route('/', methods=['GET'])
def index():
    return 'Api on',200


# metodo GET
@app.route('/charadas/lista', methods=['GET'])
def charadaLista():
    charadas= []

    lista = db.collection('charadas').stream()

    for item in lista:
        charadas.append(item.to_dict())

    if charadas:
        return jsonify(charadas),200
    else:
        return jsonify({'mensagem':'ERRO! Nenhuma charada cadastrada'}), 404
    
@app.route('/charadas', methods=['GET'])
def charadaRandom():
    charadas= []

    lista = db.collection('charadas').stream()

    for item in lista:
        charadas.append(item.to_dict())

    if charadas:
        return jsonify(random.choice(charadas)),200
    else:
        return jsonify({'mensagem':'ERRO! Nenhuma charada cadastrada'}), 404

@app.route('/charadas/<id>', methods=['GET'])
def charadaId(id):
    doc_ref=db.collection('charadas').document(id)
    doc=doc_ref.get().to_dict()

    if doc:
        return jsonify(doc)
    else:
        return jsonify({'mensagem':'ERRO! Nenhuma charada encontrado'}), 404
    
@app.route('/charadas', methods=['POST'])
def charadaPost():
    dados = request.json

    if 'charada' not in dados or 'resposta' not in dados:
        return jsonify({'mensagem':'ERRO! Campos charada e resposta são obrigatórios'}), 400
    
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id= contador_doc.get('id')
    novo_id = int(ultimo_id) + 1
    contador_ref.update({'id':novo_id})#atualiza a coleção de id

    db.collection('charadas').document(str(novo_id)).set({
        'id':novo_id,
        'charada': dados['charada'],
        'resposta': dados['resposta']
})
    return jsonify({'mensagem':'Charada cadastrada com sucesso!'}),201


@app.route('/charadas/<id>', methods=['PUT'])
def charadaPut(id):
    dados= request.json

    if 'charada' not in dados or 'resposta' not in dados:
        return jsonify({'mensagem':'ERRO! Campos charada e resposta são obrigatórios'}), 400

    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
        'charada': dados['charada'],
        'resposta': dados['resposta']

        })
        return jsonify({'mensagem':'Charada atualizada com sucesso!'}),201
        
    else:
        return jsonify({'mensagem':'ERRO! Charada não encontrada!'}), 404
    

@app.route('/charadas/<id>',methods=['DELETE'])
def charadaDELETE(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({'mensagem':'ERRO! Charada não encontrada!'}), 404
    doc_ref.delete()
    return jsonify({'mensagem':'Charada excluída com sucesso!'}), 200
if __name__ == '__main__':
    app.run()
