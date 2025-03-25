from flask import Flask,jsonify
from flask_cors import CORS 
import random
app = Flask(__name__)
CORS(app) 

charadas = [
    {'id': 1, 'charada': 'O que é, o que é? Anda com os pés na cabeça.', 'resposta': 'Piolho'},
    {'id': 2, 'charada': 'O que é, o que é? Quanto mais se tira, maior fica.', 'resposta': 'Buraco'},
    {'id': 3, 'charada': 'O que é, o que é? Tem boca, mas não fala, tem asas, mas não voa.', 'resposta': 'Rio'},
    {'id': 4, 'charada': 'O que é, o que é? Sobe e desce, mas não sai do lugar.', 'resposta': 'Escada'},
    {'id': 5, 'charada': 'O que é, o que é? Tem dentes, mas não morde.', 'resposta': 'Alho'},
    {'id': 6, 'charada': 'O que é, o que é? Corre a casa toda e depois se esconde em um canto.', 'resposta': 'Vassoura'},
    {'id': 7, 'charada': 'O que é, o que é? Quanto mais se perde, mais se tem.', 'resposta': 'Sono'},
    {'id': 8, 'charada': 'O que é, o que é? Tem chapéu, mas não tem cabeça, tem boca, mas não fala.', 'resposta': 'Garrafa'},
    {'id': 9, 'charada': 'O que é, o que é? Voa sem ter asas e chora sem ter olhos.', 'resposta': 'Nuvem'},
    {'id': 10, 'charada': 'O que é, o que é? Entra na água e não se molha.', 'resposta': 'Sombra'},
    {'id': 11, 'charada': 'O que é, o que é? Fica cheio de boca para baixo e vazio de boca para cima.', 'resposta': 'Chapéu'},
    {'id': 12, 'charada': 'O que é, o que é? Tem muitas casas, mas não tem paredes, tem ruas, mas não tem carros, tem montanhas, mas não tem árvores.', 'resposta': 'Mapa'},
    {'id': 13, 'charada': 'O que é, o que é? Anda, mas não tem pés, corre, mas não tem pernas, e chora, mas não tem olhos.', 'resposta': 'Rio'},
    {'id': 14, 'charada': 'O que é, o que é? Tem coroa, mas não é rei, tem escamas, mas não é peixe.', 'resposta': 'Abacaxi'},
    {'id': 15, 'charada': 'O que é, o que é? Quanto mais se seca, mais molhado fica.', 'resposta': 'Toalha'}
]


@app.route('/')
def index():
    return 'Api on'

@app.route('/charadas', methods=['GET'])
def charadarandom():
    return jsonify(random.choice(charadas)),200

@app.route('/charadas/id/<int:id>', methods=['GET'])
def charada(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada),200
    else:
        return jsonify({'mensagem':'ERRO! Usuário não encontrado'}), 404




if __name__ == '__main__':
    app.run(debug=True)
