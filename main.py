from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from generator import generate_lyrics
import os


import database
from database import db
from model import Lyric
app = Flask(__name__)

uri = os.getenv("DATABASE_URL")  
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    
app.config['SQLALCHEMY_DATABASE_URI']= uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
database.init_app(app)



import commands
commands.init_app(app)


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
        lyrics = generate_lyrics(song_title,  os.environ.get('Song_token'))
        
        db.session.add(Lyric(song_title, lyrics))
        db.session.commit()

        return render_template('lyrics.html', song_title = song_title, lyrics = lyrics)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
