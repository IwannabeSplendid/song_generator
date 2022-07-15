from database import db

class Lyric(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(40), nullable = False)
    song = db.Column(db.Text)

    def __init__(self, title, song):
        self.title = title
        self.song = song

    def __repr__(self):
        return self.title + ": "+ self.song