from pathlib import Path
import sys
import flask_sqlalchemy 


sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))

# Use models to seed database with 100 users, 100 items, and 100 comments.

from flask_sqlalchemy import SQLAlchemy
import sqlalchemy.orm
from backend.app.models.domain import users, items, comments 

def seed_db(db: sqlalchemy.orm.Session, users: int = 100, items: int = 100, comments: int = 100):
    
    # Seed users
    for i in range(users):
        user = users.UserCreate(
            username=f"user{i}",
            email=f"user{i}@email.com",
            password="password",
            is_active=True,
        )

        db.add(user)

    # Seed items
    for i in range(items):
        item = items.ItemCreate(
            title=f"Item {i}",
            description="Description",
            price=100,
            owner_id=1,
        )

        db.add(item)

    # Seed comments
    for i in range(comments):
        comment = comments.CommentCreate(
            body=f"Comment {i}",
            seller_id=1,
        )

        db.add(comment)

    db.commit()
    db.refresh(db)

    # read contents of database
    print(db.query(users.User).all())