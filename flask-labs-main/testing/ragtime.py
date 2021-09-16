from flask_migrate import Migrate
from app import create_app, db
from app.models import Role, User

app = create_app()
migrate = Migrate(app, db, render_as_batch=True)

@app.shell_context_processor ##Automatically adds new entries to your database
def make_shell_context():
    return dict(db=db, User=User, Role=Role)