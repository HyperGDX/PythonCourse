magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()} is a magician.")

for value in range(1, 5):
    print(value)  #从1输出到5停止，因为到5停止，所以5不输出

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []
for value in range(1, 11):
    squares.append(value ** 2)
print(squares)

digits = list(range(1, 100))
print(digits)
print(min(digits),max(digits),sum(digits),sum(digits)/len(digits))

squares = [value ** 2 for value in range(1, 11)]
print(squares)

num = list(range(1, 10 ** 6))
#for n in num:
#   print(n)
print(sum(num))

players = ["charles", "martina", "florence", "eli"]
print(players[0:3])
print(players[1:4])
print(players[:3])
print(players[0:])
print(players[-3:])

for player in players[:3]:
    print(player.title(), end="")
print("")
    
#复制列表
my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print(my_foods)
print(friend_foods)

my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)

friend_foods = my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)