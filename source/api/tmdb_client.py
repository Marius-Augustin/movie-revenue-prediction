import requests
from source.config import Config

class TMDBClient:
  def __init__(self, config: Config):
    self.headers = {
      'accept': 'application/json',
      'Authorization': f'Bearer {config.TMDB_API_KEY}'
    }
    self.TMDB_BASE_URL = config.TMDB_BASE_URL

  def _get(self, endpoint: str, params: dict = None) -> dict:
    url = f'{self.TMDB_BASE_URL}/{endpoint}'
    try:
      response = requests.get(url, headers=self.headers, params=params)
      return response.json()
    except Exception as e:
      raise e

  def discover(self, year: int, page: int) -> dict:
    params = {
      'sort_by': 'popularity.desc',
      'primary_release_year': year,
      'page': page,
    }

    return self._get(endpoint='discover/movie', params=params)

  def get_movie_details(self, movie_id: int) -> dict:
    return self._get(endpoint=f'movie/{movie_id}')

  def get_movie_credits(self, movie_id: int) -> dict:
    return self._get(endpoint=f'movie/{movie_id}/credits')