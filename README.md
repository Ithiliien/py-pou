# Game Pou

# Diseña el juego llamado Pou

- https://play.google.com/store/apps/details?id=me.pou.app&hl=es&gl=US
- https://manytools.org/hacker-tools/convert-images-to-ascii-art/go/


- play, eat, sleep, exit (5pts)
- more methods, while loop (4pts)
- better interface (1pts)

- Pou with Object Oriented programming
- Pou with Functional programming

```python
import random

class Pou:
  # inciciar
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.hunger = 0
    self.energy = 0
    self.happiness = 0
    self.health = 0
    self.alive = True

  def status(self):
    print("Name:", self.name)
    print("Age:", self.age)
    print("Hunger:", self.hunger)
    print("Energy:", self.energy)
    print("Happiness:", self.happiness)
    print("Health:", self.health)

  def __str__(self):
    return f"Name: {self.name}\nAge: {self.age}\nHunger: {self.hunger}\nEnergy: {self.energy}\nHappiness: {self.happiness}\nHealth: {self.health}"

  def play(self):
    # self.hunger += 1
    # self.energy += 1
    # self.happiness += 1
    # self.health += 1

  def eat(self):
    pass

  # add more methods

toto = Pou("Toto")

while True:
  option = input("What do you want to do? (play, eat, sleep, exit): ")

  if option == "play":
    toto.play()
  # add more methods
  else:
    break

```
