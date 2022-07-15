import click


import click
from flask.cli import with_appcontext

from main import db, Lyrics

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
