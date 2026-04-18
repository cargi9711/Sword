from sword import Sword
from warrior import Warrior

sword = Sword("Excalibur", 100, 5)
warrior = Warrior("Arthur", sword)

print(sword)
print(warrior.attack())
