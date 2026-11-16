import mysql.connector

from source.database import MariaDB
from source.model import Person

class PersonRepository:
  def __init__(self, db: MariaDB):
    self.db = db

  def insert(self, person: Person):
    conn = self.db.get_connection()
    cursor = conn.cursor()
    
    query = """
      INSERT INTO people (id, name)
      VALUES (%(id)s, %(name)s)
    """
    
    try:
      cursor.execute(query, person.to_dict())
      print(query)
      print(person.to_dict())
      conn.commit()
    except mysql.connector.Error as err:
      conn.rollback()
      if err.errno == 1062:
        print(f"duplicate skipped: person '{person.name}' already exists.")
      else:
        raise err
    finally:
      cursor.close()
      conn.close()