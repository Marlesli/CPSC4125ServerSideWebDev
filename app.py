from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')  #1st route for home 

@app.route('/album')
def album():
    return render_template('album.html')  # second route for album 

if __name__ == '__main__':
    app.run(debug=True)


