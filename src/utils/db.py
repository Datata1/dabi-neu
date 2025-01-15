import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

def get_engine(path: str = "sqlite:///DABI1.db"):
    database_path = path  
    
    engine = create_engine(database_path)
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Verbindung erfolgreich")
    except Exception as e:
        print("Fehler beim Verbinden zur Datenbank:", e)
    
    return engine 

def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()

if __name__ == "__main__":
    engine = get_engine()
    session = get_session(engine)
