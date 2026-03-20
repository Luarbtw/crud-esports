# eSports CRUD API

API for registering esports proplayers and coaches, more specifically from the FPS Valorant. The initial focus was to be exclusively dedicated to players who are Free Agents — without a contract and looking for a team. For this reason, there is no reference to teams or organizations in the code.

## Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite

## Endpoints

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/players` | List all players |
| GET | `/players/{id}` | Get player by ID |
| POST | `/players` | Register new player |
| PATCH | `/players/{id}` | Update player data |
| DELETE | `/players/{id}` | Remove player |

| Method | Route | Description |
|--------|-------|-------------|
| GET | `/coaches` | List all coaches |
| GET | `/coaches/{id}` | Get coach by ID |
| POST | `/coaches` | Register new coach |
| PATCH | `/coaches/{id}` | Update coach data |
| DELETE | `/coaches/{id}` | Remove coach |

## How to run

1. Clone the repository
```bash
git clone https://github.com/Luarbtw/crud-esports.git
cd crud-esports
```

2. Create the virtual environment

**Linux/macOS**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```
or

```bash
py -m venv venv
venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn main:app --reload
```

## Frontend

A frontend interface is available in the `frontend/` folder. Open `index.html` with the Live Server extension on VSCode.

> Frontend design created with AI (Claude).

5. Access the documentation
http://localhost:8000/docs

## Author

Gustavo Farias — [linkedin.com/in/gustavo-farias-712674302](https://linkedin.com/in/gustavo-farias-712674302)


