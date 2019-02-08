from app import app, db
from app.models import User, Post

#Runs the site

if __name__ == '__main__':
    app.run(host='jack_wall.netsoc.co', port=8080)

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}
