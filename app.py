from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    URL = "https://xkcd.com/1000/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template('home.html', data = data)  #1st route for home 

@app.route('/pastComic')
def pastComic():
    URL = "https://xkcd.com/1000/info.0.json"
    req = requests.get(url = URL)
    data = req.json()
    return render_template('home.html', data = data) 

@app.route('/album')
def album():
    return render_template('album.html')  # second route for album 

if __name__ == '__main__':
    app.run(debug=True)


