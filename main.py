from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import os
from generator import generate_lyrics


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= os.getenv('DATABASE_URL')

db = SQLAlchemy(app)

class Lyric(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(40), nullable = False)
    song = db.Column(db.Text)

    def __init__(self, title, song):
        self.title = title
        self.song = song

    def __repr__(self):
        return self.title + ": "+ self.song


@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        return redirect(f'/{request.form.get("song_title")}')
    else:
        return render_template('main.html')

@app.route('/<string:song_title>', methods = ['POST', 'GET'])
def lyrics(song_title):
    if request.method == 'POST':
        return redirect(f'/{request.form.get("song_title")}')
    else:
        lyrics = generate_lyrics(song_title, 'hf_cHnyvYKrzAfrPouCcRMJspmjWSBhJdfLk') #os.getenv('Song_token')
        
        # db.session.add(Lyric(song_title, lyrics))
        # db.session.commit()

        return render_template('lyrics.html', song_title = song_title, lyrics = lyrics)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
