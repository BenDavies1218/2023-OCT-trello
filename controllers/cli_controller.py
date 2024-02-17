from datetime import date
from flask import Blueprint
from init import db, bcrypt
from models.user import User
from models.card import Card
from models.comment import Comment

db_commands = Blueprint("db", __name__)


@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables created")


@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables dropped")


@db_commands.cli.command("seed")
def seed_tables():
    users = [
        User(
            email="admin@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
            is_admin=True,
        ),
        User(
            name="User 1",
            email="user1@email.com",
            password=bcrypt.generate_password_hash("123456").decode("utf-8"),
        ),
    ]
    db.session.add_all(users)

    cards = [
        Card(
            title="Card 1",
            description="Card 1 Desc",
            date=date.today(),
            status="To DO",
            priority="high",
            user=users[0],
        ),
        Card(
            title="Card 2",
            description="Card 2 Desc",
            date=date.today(),
            status="To DO",
            priority="low",
            user=users[1],
        ),
    ]
    db.session.add_all(cards)

    comments = [
        Comment(message="Comment 1", user=users[0], card=cards[0]),
        Comment(message="Comment 2", user=users[0], card=cards[1]),
        Comment(message="Comment 3", user=users[0], card=cards[1]),
        Comment(message="Comment 4", user=users[0], card=cards[1]),
    ]
    db.session.add_all(comments)

    db.session.commit()

    print("Tables seeded")
