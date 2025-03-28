import pytest
from src.app import app as flask_app, db

@pytest.fixture
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with flask_app.app_context():
        db.create_all()
    yield flask_app
    with flask_app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

def test_create_todo(client):
    response = client.post('/todos', json={
        'title': 'Test Todo',
        'description': 'Test Description'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['title'] == 'Test Todo'
    assert data['completed'] == False

def test_get_todos(client):
    client.post('/todos', json={'title': 'Todo 1'})
    client.post('/todos', json={'title': 'Todo 2'})

    response = client.get('/todos')
    assert response.status_code == 200
    todos = response.get_json()
    assert len(todos) == 2