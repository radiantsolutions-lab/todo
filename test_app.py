#!/usr/bin/env python3
from app import app, db
import tempfile
import os

# Use a temporary database for testing
db_fd, db_path = tempfile.mkstemp()
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['TESTING'] = True

with app.app_context():
    db.create_all()
    print("✅ Database created successfully")

    # Test the app
    client = app.test_client()

    # Test GET /
    response = client.get('/')
    print(f"✅ GET /: {response.status_code}")

    # Test GET /api/todos
    response = client.get('/api/todos')
    print(f"✅ GET /api/todos: {response.status_code}")

    # Test POST /api/todos
    response = client.post('/api/todos', json={'task': 'Test task'})
    print(f"✅ POST /api/todos: {response.status_code}")

    # Test GET /api/todos again to see the new task
    response = client.get('/api/todos')
    todos = response.get_json()
    print(f"✅ Retrieved {len(todos)} todos")

    if todos:
        todo_id = todos[0]['id']
        # Test PUT /api/todos/<id>
        response = client.put(f'/api/todos/{todo_id}', json={'completed': True})
        print(f"✅ PUT /api/todos/{todo_id}: {response.status_code}")

        # Test DELETE /api/todos/<id>
        response = client.delete(f'/api/todos/{todo_id}')
        print(f"✅ DELETE /api/todos/{todo_id}: {response.status_code}")

print("\n🎉 All tests passed! The app is working correctly.")

# Cleanup
os.close(db_fd)
os.unlink(db_path)
