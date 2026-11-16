from dataclasses import dataclass

@dataclass
class Movie:
  movie_id: int
  title: str
  budget: int
  revenue: int
  franchise_id: int  
  release_date: str
  language: str
  runtime: int 
  primary_genre: str
  production_company: str

  def to_dict(self) -> dict:
    return {
      'id': self.movie_id,
      'title': self.title,
      'budget': self.budget,
      'revenue': self.revenue,
      'franchise_id': self.franchise_id,
      'release_date': self.release_date,
      'language': self.language,
      'runtime': self.runtime,
      'primary_genre': self.primary_genre,
      'production_company': self.production_company,
    }