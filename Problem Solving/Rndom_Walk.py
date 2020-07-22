import random
print("####################   V1    ##################### >> Simple way")
def random_walk_V1(n):  # n = numbers of blocks you detect to walk
    """"V1)) simple  RETURN CORDIANTES AFTER WALK N BLOCKS RANDOMLY"""
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])  # the randomly choice of 4 direction
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1

    return (x, y)  # return the current random location


for z in range(25):
    walk = random_walk_V1(10)
    print(walk, "The Distance from home = ",
          abs(walk[0]) + abs(walk[1]))  # YOU CARE ABOUT THE DISTANCE NOT THE DIRECTION so USE Abs function

print("####################   V2    ##################### >> more Compact way")


def random_walk_V2(n):  # n = numbers of blocks you detect to walk
    """"V2)) simple  RETURN CORDIANTES AFTER WALK N BLOCKS RANDOMLY"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, 1), (1, 0), (1, 0)])
        x += dx
        y += dy
    return (x, y)


for d in range(25):
    walk = random_walk_V2(10)
    print(walk, "The Distance from home = ",
          abs(walk[0]) + abs(walk[1]))  # YOU CARE ABOUT THE DISTANCE NOT THE DIRECTION so USE Abs function

# if you want to calculate the longest or the minimum walked by detect the number of blocks you want to tranport
# you can calculate it mathimatically but there another way by using MONTE CARLO SIMULATION

print(">>>>>>>>>> MONTE CARLO SIMULATION <<<<<<<<<<<<")


def random_walk_V3(n):  # n = numbers of blocks you detect to walk
    """"V3)) simple  RETURN CORDIANTES AFTER WALK N BLOCKS RANDOMLY with mont carlo simulation (( it may be slow because mont carlo take an random samples"""
    x, y = 0, 0
    for i in range(n):
        (dx, dy) = random.choice([(0, 1), (0, 1), (1, 0), (1, 0)])
        x += dx
        y += dy
    return (x, y)

numer_of_walks = 20000

for walk_length in range(1, 31):
    num_transport = 0  # >>> number of walks = 4 or fewer blocks ,from home
    for s in range(numer_of_walks):       #>>Start the mont carlo loop optain number of walks sampeles
        (x, y) = random_walk_V3(walk_length)      #>> Get a random walk from walk_length
        distance = abs(x) + abs(y)           #>> COMPUTE THE DISTANCE FROM HOME
        if distance <= 4:
            num_transport += 1          # increament your transport counter
            #then compute the percenrage of random walk distance from home >???????
    num_transport_percentage = float(num_transport) / numer_of_walks
    print("WALK SIZE = ", walk_length, "percent % of transport =", 100* num_transport_percentage)
