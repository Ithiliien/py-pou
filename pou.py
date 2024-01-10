import random
def minmax(value):
  if value < 0:
    return 0
  elif value > 0:
    return 100
  else:
    return value
class Pou:
  # inciciar
  def __init__(self, name):
    self.name = name
    self.age = 0
    self.hunger = random.randint(0,50)
    self.energy = random.randint(50,100)
    self.happiness = random.randint(0,10)
    self.health = 100  # Inicializamos la salud en 100
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
    self.hunger = minmax(self.hunger+random.randint(5,10))
    self.energy = minmax(self.energy+random.randint(10,20))
    self.happiness =minmax(self.happiness+random.randint(5,10))
    self.health = minmax(self.health+random.randint(0,5))
    self._check_status()

  def eat(self):
    self.hunger = minmax(self.hunger+random.randint(5,10))
    self.energy = minmax(self.energyrandom.randint(10,20))
    self.happiness =minmax(self.happiness+random.randint(5,10))
    self.health = minmax(self.health+random.randint(0,5))
    self._check_status()

  def sleep(self):
    self.energy += 3
    self.health += 2
    self.hunger -= minmax(self.hunger+random.randint(5,10))
    self._check_status()

  def _check_status(self):
    # Limitamos los valores entre 0 y 100
    self.hunger = max(0, min(self.hunger, 100))
    self.energy = max(0, min(self.energy, 100))
    self.happiness = max(0, min(self.happiness, 100))
    self.health = max(0, min(self.health, 100))
  
  def pet(self):
    self.health += 3
    self.happiness += 1
    self._check_status()
    
    if self.health <= 0:
      self.alive = False
      print(f"{self.name} has passed away.")
      exit()  # Salir del juego si la mascota muere

toto = Pou("Toto")

while toto.alive:
  toto.status()
  option = input("What do you want to do? (play, eat, sleep,pet exit): ")

  if option == "play":
    toto.play()
    toto.status()
  elif option == "eat":
    toto.eat()
    toto.status()
  elif option == "sleep":
    toto.sleep()
    toto.status()
  elif option == "pet":
    toto.pet()
    toto.status()
  else:
    break
