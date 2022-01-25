import random
num = random.randint(1, 100)
while True:
  guess = int(input("Guess A Number Between 1 and 100: "))
  if guess > num:
    print("Your Number Is Too High. Try Again!")
  elif guess < num:
    print("Your number Is Too Low. Try Again!")
  else:
    print(f"Correct! The Number Was {str(num)}.")
    break
