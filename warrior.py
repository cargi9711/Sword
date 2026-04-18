from sword import Sword

class Warrior:
    def __init__(self, name, sword: Sword):
        self.name = name
        self.sword = sword

    def attack(self):
        return f"{self.name} attacks! {self.sword.swing()}"
