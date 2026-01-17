import dataclasses


@dataclasses.dataclass
class State:
    id: str
    name: str
    capital: str
    lat: float
    lng: float
    area: int
    population: int
    neighbors: str

    def __str__(self):
        return f"{self.id}"
    def __hash__(self):
        return hash(self.id)