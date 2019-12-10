from flask import Flask, jsonify, request
from text_processing import TextProcessing

app = Flask(__name__)
textProcessing = TextProcessing()

@app.route("/")
def home():
    return "<h1>Welcome to Natural Language Processing API !!</h1>"

# @app.route('/translate/<string:text>&<string:language_to>', methods=['GET'])
# def translate(text, language_to):
#     try:
#         code, text = textProcessing.translate(text,language_to)
#     except Exception as e:
#         code = 301
#         text = e
#     return jsonify({'code' : code, 'text' : str(text)})

@app.route('/translate', methods=['POST'])
def translate():
    params = request.get_json()
    text = params['text']
    language_to = params['language_to']
    try:
        code, text = textProcessing.translate(text, language_to)
    except Exception as e:
        code = 301
        text = e
    return jsonify({'code' : code, 'text' : str(text)})

# @app.route('/nouns/<string:text>', methods=['GET'])
# def getNouns(text):
#     try:
#         code, nouns = textProcessing.getNounsText(text)
#     except Exception as e:
#         code = 301
#         nouns = e
#     return jsonify({'code' : code, 'nouns' : str(nouns)})

@app.route('/nouns', methods=['POST'])
def getNouns():
    params = request.get_json()
    text = params['text']
    try:
        code, nouns = textProcessing.getNounsText(text)
    except Exception as e:
        code = 301
        nouns = str(e)
    return jsonify({'code' : code, 'nouns' : nouns if type(nouns) == str else [noun for noun in nouns]})

if __name__ == '__main__':
    app.run(debug=True)