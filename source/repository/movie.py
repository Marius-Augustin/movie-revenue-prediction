import mysql.connector

from source.database.mariadb import MariaDB
from source.model import Movie

class MovieRepository():
  def __init__(self, db: MariaDB):
    self.db = db

  def insert(self, movie: Movie):
    conn = self.db.get_connection()
    cursor = conn.cursor()
    
    query = """
      INSERT INTO movies (
        id, title, budget, revenue,
        franchise_id, release_date, language,
        runtime, primary_genre, production_company
      ) VALUES (
        %(id)s, %(title)s, %(budget)s, %(revenue)s,
        %(franchise_id)s, %(release_date)s, %(language)s,
        %(runtime)s, %(primary_genre)s, %(production_company)s
      )
    """
    
    try:
      cursor.execute(query, movie.to_dict())
      conn.commit()
    except mysql.connector.Error as err:
      conn.rollback()
      if err.errno == 1062:
        print(f"duplicate skipped: movie '{movie.title}' already exists.")
      else:
        raise err
    finally:
      cursor.close()
      conn.close()