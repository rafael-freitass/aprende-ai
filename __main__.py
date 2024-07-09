import google.generativeai as genai 
from dotenv import load_dotenv
import os
from flask import Flask, render_template, request 
app = Flask(__name__)


def configure():
    load_dotenv()
# API KEY
GOOGLE_API_KEY = genai.configure(api_key = os.getenv('api_key'))

# Modelo que vou usar
model = genai.GenerativeModel(model_name='gemini-1.0-pro')

# Dicionário para armazenar as opções de matérias
materias = {
    1: "Matemática",
    2: "Física",
    3: "Química",
    4: "Biologia",
    5: "Geografia",
    6: "História",
    7: "Português",
    8: "Literatura",
    9: "Inglês",

}

# Dicionário para armazenar os tipos de provas
tipos_prova = {
    1: "questões objetivas",
    2: "questões verdadeiro ou falso",
    3: "questões dissertativas",
    4: "questões de somatória",
}

# Dicionário para armazenar as dificuldades de provas
dificuldade_prova = {
    1: "Fácil",
    2: "Médio",
    3: "Difícil", 
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resource', methods = ['POST'])
def processar_fomulario():
    dados_formulario = request.json

    payload = {
        "materia": materias[dados_formulario["materia"]],
        "tipo_prova": tipos_prova[dados_formulario["tipo_prova"]],
        "dificuldade": dificuldade_prova[dados_formulario["dificuldade"]],
        "num_questoes": dados_formulario["num_questoes"]
    }
    prova_gerada = gerar_prova(payload)
    return gerar_prova(payload)


def gerar_prova(payload):
    prompt = f"Crie {payload["num_questoes"]} {payload["tipo_prova"]} de {payload["materia"]} nível {payload["dificuldade"]}. Utilize contextos e histórias no enunciado, coisas que fazem o estudante pensar e juntar informações pare responder. Não utilize ** para indicar a questão ou a resposta, faça do seguinte modelo: 1) questao.. Resposta: a) b) c) d)... Gabarito:"
    print(prompt)

    prova_gerada = model.generate_content(prompt)
    print(prova_gerada)
    return prova_gerada.text

if __name__ == '__main__':
    app.run(debug=True)