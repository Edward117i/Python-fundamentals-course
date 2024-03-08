import random

option = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:
  print('*' * 10)
  print(f'Round {rounds}')
  print('*' * 10)

  print(f'Computer wins: {computer_wins}')
  print(f'User wins: {user_wins}')
  
  user_option = input("piedra, papel o tijera => ")
  user_input = user_option.lower()
  
  if not user_input in option:
    print('Esa opcion no es valida')
    continue
  rounds +=1
  computer_option = random.choice(option)

  print('User opton =>' , user_option)
  print('Computer option =>', computer_option)

  if user_input == computer_option:
    print("Empate!")
  elif user_input == "piedra":
    if computer_option == "tijera":
      print("piedra gana a tijera")
      print("user gano!")
      user_wins += 1
    else:
      print("papel gana a piedra")
      print("computer gano!")
      computer_wins += 1
  elif(user_input == "papel"):
    if computer_option == "piedra":
      print("papel gana a piedra")
      print("user gano!")
      user_wins += 1
    else:
      print("tijera gana a papel")
      print("computer gano!")
      computer_wins += 1
  elif(user_input == "tijera"):
    if computer_option == "papel":
      print("tijera gana a papel")
      print("user gano!")
      user_wins += 1
    else:
      print("piedra gana a tijera")
      print("computer gano!")
      computer_wins += 1
      
  if computer_wins == 3:
    print(f'El ganador es la computadora')
    break

  if user_wins == 3:
    print(f'El ganador es el usuario')
    break
  
  