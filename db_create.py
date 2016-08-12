from app import db
from models import BlogPost

# create the database and the db tables
db.create_all()

# insert
db.session.add(BlogPost("First", "First Comment"))
db.session.add(BlogPost("Second", "Second Comment"))

# commit the changes
db.session.commit()
