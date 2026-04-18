class Sword:
    def __init__(self, name, damage, weight):
        self.name = name
        self.damage = damage
        self.weight = weight

    def swing(self):
        return f"{self.name} swings dealing {self.damage} damage!"

    def __str__(self):
        return f"{self.name} | Damage: {self.damage} | Weight: {self.weight}kg"
