import pytest
from app import app



@pytest.fixture

def test_app():
    ''' test application test'''
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    with app.test_client() as client:
        yield client
