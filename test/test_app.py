import pytest
from src import create_app, db
from src.models import Todo

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

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
    # Créer quelques tâches de test
    client.post('/todos', json={'title': 'Todo 1'})
    client.post('/todos', json={'title': 'Todo 2'})

    response = client.get('/todos')
    assert response.status_code == 200
    todos = response.get_json()
    assert len(todos) == 2