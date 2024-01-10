import random

def minmax(value):
  if value < 0:
    return 0
  elif value > 0:
    return 100
  else:
    return value

state ={
  "name": "Toto",
   "age": 0,
   "hunger": random.randint(0,50),
   "energy": random.randint(50,100),
   "happiness": 100,
   "health": 100,
   "alive": True
  }
def status():
     print("Name:" ,  state["name"])
     print("Age:" ,  state["age"])
     print("Hunger:" ,  state["hunger"])
     print("Energy:" ,  state["energy"])
     print("Happiness:" ,  state["happiness"])
     print("Health" ,  state["health"])
  
def play(state):
     new_state= dict(state)
     new_state["hunger"]= minmax(state["hunger"]+ random.randint(5,10))
     new_state["energy"]= minmax(state["energy"]- random.randint(10,20))
     new_state["happiness"]= minmax(state["happiness"]+ random.randint(5,10))
     new_state["health"]= minmax(state["health"]+ random.randint(0,5))
     return new_state
  

def eat(state):
     new_state= dict(state)
     new_state["hunger"]= minmax(state["hunger"]- random.randint(5,10))
     new_state["energy"]= minmax(state["energy"]+ random.randint(10,20))
     new_state["happiness"]= minmax(state["happiness"]+ random.randint(5,10))
     new_state["health"]= minmax(state["health"]+ random.randint(0,5))
     return new_state
  
def sleep(state):
     new_state= dict(state)
     new_state["hunger"]= minmax(state["hunger"]+ random.randint(5,10))
     new_state["energy"]= minmax(state["energy"]+ random.randint(10,20))
     new_state["happiness"]= minmax(state["happiness"]+ random.randint(5,10))
     new_state["health"]= minmax(state["health"]+ random.randint(0,5))
     return new_state
  

def pet(state):
     new_state= dict(state)
     new_state["hunger"]= minmax(state["hunger"]+ random.randint(5,10))
     new_state["energy"]= minmax(state["energy"]- random.randint(10,20))
     new_state["happiness"]= minmax(state["happiness"]+ random.randint(5,10))
     new_state["health"]= minmax(state["health"]+ random.randint(0,5))
     return new_state
  

def _check_status(state):
    # Limitamos los valores entre 0 y 100
    self.hunger = max(0, min(self.hunger, 100))
    self.energy = max(0, min(self.energy, 100))
    self.happiness = max(0, min(self.happiness, 100))
    self.health = max(0, min(self.health, 100))
    if self.health <= 0:
      self.alive = False
      print(f"{self.name} has passed away.")
      exit()  # Salir del juego si la mascota muere

 
while True:
        status()
        option = input("What do you want to do? (play, eat, sleep, pet, exit): ")

        if option == "play":
            state = play(state)
        elif option == "eat":
            state= eat(state)
        elif option == "sleep":
            state = sleep(state)
        elif option == "pet":
            state = pet(state)
        elif option == "exit":
            break
        else:
            print("Invalid option. Please choose again.")



