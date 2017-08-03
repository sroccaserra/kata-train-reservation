from flask import Blueprint, jsonify, request

from infrastructure.bootstrap import get_ticket_office

main = Blueprint('main', __name__)


@main.route('/reserve')
def reserve():
    train_id = request.args.get('train_id', '')
    seat_count = int(request.args.get('seat_count', 0))
    ticket_office = get_ticket_office()
    reservation = ticket_office.reserve(train_id, seat_count)
    return jsonify(reservation)
