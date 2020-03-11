from flask import Flask
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def home():
    return "Minha primeira API."

@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(debug=True)