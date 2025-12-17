from dataclasses import dataclass

@dataclass
class Interazione:
    id_gene1: str
    id_gene2: str
    tipo: str
    correlazione: float

    def __str__(self):
        return f"{self.id_gene1} {self.id_gene2} {self.tipo} {self.correlazione}"
    def __eq__(self, other):
        return self.id_gene1 == other.id_gene1 and self.id_gene2 == other.id_gene2
    def __hash__(self):
        return hash((self.id_gene1, self.id_gene2))