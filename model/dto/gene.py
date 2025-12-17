from dataclasses import dataclass

@dataclass
class Gene:
    id: str
    funzione: str
    essenziale:str
    cromosoma: int

    def __str__(self):
        return f"{self.id} in {self.cromosoma}"
    def __hash__(self):
        return hash(self.id)