import click
from database import db

def create_db():
    """Creates database"""
    db.create_all()
    
def drop_db():
    """Cleans database"""
    db.drop_all()
    
    
def init_app(app):
    for command in [create_db, drop_db]:
        app.cli.add_command(app.cli.command()(command))