from flask import Flask
app= Flask(__name__)

@app.route('/')
def home():
  return "Merhaba, Buluttan Selam!"

@app.route('/denemme')
def denemme():
  return "Hakkımda Sayfası"
