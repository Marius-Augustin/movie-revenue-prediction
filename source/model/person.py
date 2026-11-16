from dataclasses import dataclass

@dataclass
class Person:
  person_id: int
  name: str

  def to_dict(self) -> dict:
    return {
      'id': self.person_id,
      'name': self.name,
    }