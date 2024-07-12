from flask import Flask, request, jsonify, render_template
from text_to_speech.exception import TTSException
from text_to_speech.components.get_accent import get_accent_message, get_accent_tld
from text_to_speech.components.textToSpeech import TTSapplication
from flask_cors import CORS
import sys

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        raise TTSException(e, sys)

@app.route('/accent_list', methods=['GET'])
def accent_list():
    try:
        accent_list = get_accent_message()
        return jsonify({'accent_list': accent_list})
    except Exception as e:
        raise TTSException(e, sys)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            data = request.json['data']
            accent_input = request.json['accent']
            accent = get_accent_tld(accent_input)
            result = TTSapplication().text2speech(data, accent)
            return jsonify({"data": result})
    except Exception as e:
        raise TTSException(e, sys)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
