# Todo App - Railway PostgreSQL Deployment Test

A modern, sleek todo application built with Flask and PostgreSQL, designed for testing Railway deployments.

## Features

- ✅ Single-page application with modern UI
- ✅ PostgreSQL database integration
- ✅ Task creation, completion, and deletion
- ✅ Responsive design inspired by Railway's aesthetic
- ✅ RESTful API endpoints
- ✅ Railway-ready deployment configuration

## Tech Stack

- **Backend**: Flask + SQLAlchemy
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Deployment**: Railway

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up PostgreSQL database and update `DATABASE_URL` in your environment

3. Run the application:
   ```bash
   python app.py
   ```

4. Open http://localhost:5000 in your browser

## Railway Deployment

1. **Connect Repository**: Connect your GitHub repository to Railway
2. **Database Setup**: Railway will automatically provision a PostgreSQL database
3. **Environment Variables**: Railway automatically provides `DATABASE_URL` environment variable
4. **Deployment**: Railway will automatically detect the `railway.json` config and deploy using Nixpacks
5. **Access**: Your app will be available at the Railway-provided URL

### Railway Configuration Files

- `railway.json`: Railway deployment configuration
- `start.py`: Production startup script that uses Railway's `PORT` environment variable
- `requirements.txt`: Python dependencies (PostgreSQL adapter added automatically by Railway)

### Database Migration

The app automatically creates database tables on first run using SQLAlchemy's `db.create_all()`.

## API Endpoints

- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/<id>` - Update a todo (mark complete/incomplete)
- `DELETE /api/todos/<id>` - Delete a todo

## Database Schema

```sql
CREATE TABLE todo (
    id SERIAL PRIMARY KEY,
    task VARCHAR(200) NOT NULL,
    completed BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
