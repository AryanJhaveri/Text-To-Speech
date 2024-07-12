from text_to_speech.exception import TTSException
from flask import Flask, request, rennder_template
from text_to_speech.components.get_accent import get_accent_message, get_accent_tld
from flask_cors import CORS, cross_origin
from text_to_speech.components.textToSpeech import TTSapplication
import sys

app= Flask(__name__)
CORS(app)

@app.route('/',method=['GET'])
@cross_origin()
def home():
    try:    
        accent_list = get_accent_message
        return rennder_template('index.html', accent_list=accent_list)
    except Exception as e:
        raise TTSException(e, sys)

@app.route('/predict', methods=['GET','POST'])
@cross_origin
def predict():
    try:
        if request =="POST":
            data = request.json(['data'])
            accent_input = request.json(['accent'])
            accent = get_accent_tld(accent_input)
            result = TTSapplication().text2speech(data, accent)
            return {"data": result.decode("utf8")}
    except Exception as e:
        raise TTSException(e , sys)
    

if __name__ == '__main__':
    app.run(post=5000, debug =True)
    