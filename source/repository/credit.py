from source.database.mariadb import MariaDB
from source.model import Credit

class CreditRepository:
  def __init__(self, db: MariaDB):
    self.db = db

  def insert(self, credit: Credit):
    conn = self.db.get_connection()
    cursor = conn.cursor()
    
    query = """
      INSERT INTO credits (movie_id, person_id, role)
      VALUES (%(movie_id)s, %(person_id)s, %(role)s)
    """
    
    try:
      cursor.execute(query, credit.to_dict())
      conn.commit()
    except Exception as err:
      conn.rollback()
      raise err
    finally:
      cursor.close()
      conn.close()

  





