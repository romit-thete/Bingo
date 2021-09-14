import random, time, sys
numbers = list(range(1,91))
random.shuffle(numbers)
# print(numbers.pop())
print("Starting the game")

for i in range(3):
    sys.stdout.write('.')
    sys.stdout.flush()
    time.sleep(1)
print("\nWelcome to Tambola!")
time.sleep(1)
print("Hope you have a good time and a good Win!!")
a=[]

while numbers:
    x=input("Press Enter key for a new number\n")
    if x =="":
        print(numbers.pop())
    elif x.lower()=='exit' or x.lower()=='quit':
        break
