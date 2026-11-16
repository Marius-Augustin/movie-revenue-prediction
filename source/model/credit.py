from dataclasses import dataclass

@dataclass
class Credit:
  movie_id: int
  person_id: int
  role: str

  def to_dict(self):
    return {
      'movie_id': self.movie_id,
      'person_id': self.person_id,
      'role': self.role,
    }