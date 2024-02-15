from flask import Blueprint

from init import db

cards_bp = Blueprint("cards", __name__, url_prefix="/cards")
from models.card import Card, cards_schema


@cards_bp.route("/")
def get_all_cards():
    stmt = db.select(Card).order_by(Card.date.desc())
    cards = db.session.scalars(stmt)
    return cards_schema.dumps(cards)
