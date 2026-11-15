import mysql.connector
import mysql.connector.pooling

from source.config import Config

class MariaDB:
  def __init__(self, config: Config):
    self.pool = mysql.connector.pooling.MySQLConnectionPool(
      pool_size=5,
      host=config.DB_HOST,
      database=config.DB_DATABASE,
      user=config.DB_USER,
      password=config.DB_PASS,
    )

  def get_connection(self):
    return self.pool.get_connection()