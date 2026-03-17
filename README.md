# eSports CRUD API

API for registering esports proplayers and coaches, more specifically from the FPS Valorant. The initial focus was to be exclusively dedicated to players who are Free Agents — without a contract and looking for a team. For this reason, there is no reference to teams or organizations in the code.

## Technologies
- Python
- FastAPI
- SQLAlchemy
- SQLite

## How to run

1. Clone the repository
```bash
git clone https://github.com/Luarbtw/crud-esports.git
cd valorant-crud
```

2. Create the virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the server
```bash
uvicorn main:app --reload
```

5. Access the documentation
http://localhost:8000/docs

## Author
Gustavo Farias — linkedin.com/in/gustavo-farias-712674302/