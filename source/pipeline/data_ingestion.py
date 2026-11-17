from source.model import Movie, Person, Credit
from source.database import MariaDB
from source.api import TMDBClient

class DataIngestor:
  START_YEAR = 2010
  BLACKLIST = [
    2020,
    2021,
  ]
  PAGE_COUNT = 15
  API_DELAY = 0.5

  def __init__(self, db: MariaDB, api: TMDBClient):
    self.db = db
    self.api = api

  def _get_movie_ids(self, year: int, page: int):
    movie_ids = []

    response = self.api.discover(year, page)  
    for movie in response.get('results', []):
      movie_ids.append(movie.get('id'))

    return movie_ids

  def _parse_movie_response(self, movie_id: int) -> Movie:
    pass