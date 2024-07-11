import pytest
import uuid

from src.models.repositories.links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
id = str(uuid.uuid4())

@pytest.mark.skip(reason='interacao com o banco')
def test_create_link():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links_info = {
        "id": id,
        "trip_id": trip_id,
        "link": "https://example.com",
        "title": "Example Website"
    }
    
    links_repository.create_link(links_info)

@pytest.mark.skip(reason='interacao com o banco')
def test_get_trip_by_id():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    link = links_repository.get_links_by_id('f97cee89-eb4f-49c3-b2be-e5f87ab634a7')
    print(link)
    
    assert isinstance(link, tuple)
    assert isinstance(link[0], str)
    