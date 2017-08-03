import requests
from flask import g

from domain.ticket_office import TicketOffice
from infrastructure.service_providers.booking_reference_service import BookingReferenceService
from infrastructure.service_providers.train_data_service import TrainDataService


def get_ticket_office():
    if not hasattr(g, 'ticket_office'):
        g.ticket_office = bootstrap_ticket_office()
    return g.ticket_office


def bootstrap_ticket_office():
    booking_reference_service = BookingReferenceService()
    train_data_service = TrainDataService(requests)
    return TicketOffice(train_data_service, booking_reference_service)
