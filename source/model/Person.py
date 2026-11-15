from dataclasses import dataclass

@dataclass
class Person:
  person_id: int
  name: str
  role: str

  def to_dict(self) -> dict:
    return {
      'id': self.person_id,
      'name': name,
      'role': role,
    }
