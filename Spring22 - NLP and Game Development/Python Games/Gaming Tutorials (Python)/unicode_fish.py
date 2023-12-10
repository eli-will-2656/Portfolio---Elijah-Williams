import random, sys, time

try:
    import bext
except ImportError:
    print("This program has been unsuccessful in importing a necessary dependency (bext module)")
    sys.exit()


WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 4

FISH_TYPES = [
    {'right':['><>'],               'left':['<><']},
    {'right':['>||>'],               'left':['<||<']},
    {'right':['>))>'],               'left':['<((<']},
    {'right':['>-==>'],               'left':['<==-<']},
    {'right':[r'>\\>'],               'left':['<//-<']},
    {'right':['>888>'],               'left':['<888<']},
]

LONGEST_FISH_LENGTH = 5

LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

def main():
    gloabl FISHES, BUBBLERS, BUBBLES, KELPS, STEP

    bext.bg('black')
    bext.clear()

    # Generate the global variables
    FISHES = []
    for i in range(NUM_FISH):
        FISHES.append(generateFish())

    BUBBLERS = []
    for i in range(NUM_BUBBLES):
        BUBBLERS.append(random.randint(LEFT_EDGE, RIGHT_EDGE))

    BUBBLES = []

    KELPS = []
    for i in range(NUM_KELP):
        kelpx = random.randint(LEFT_EDGE, RIGHT_EDGE)
        kelp = {'x': kelpx, 'segments' = []}
        # Generate each segment of the kelp:
        for i in range(random.randint(6, HEIGHT - 1)):
            kelp['segments'].append(random.choice('[','(',')',']'))
        KELPS.append(kelp)


    # Run the simulation
    STEP = 1
    while True:
        simulateAquarium()
        drawAquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clearAquarium()
        STEP += 1

    def getRandomColor():
        """Return a string of a random color."""
        return random.choice(('black','green','red','yellow','blue', 'purple', 'cyan','white'))

    def generateFish():
        """Return a dictionary that represents a fish."""
        fishType = random.choice(FISH_TYPES)

        # Set up colors for each character in the fish text:
        colorPatter = random.choice(('random', 'head-tail', 'single'))
        fishLength = len(fishType['right'][0])
        if colorPattern == 'random': # All parts of the fish are randomly colored
            colors = []
            for i in range(fishLength):
                colors.append(getRandomColor())
        if colorPattern == 'single' or colorPattern == 'head-tail':
            colors = [getRandomColor()] * fishLength # All the same colors
        if colorPattern == 'head-tail' # Head and tail are different from the body
            headColor = getRandomColor()
            colors[0] = colors[-1] = headColor

        # Set up rest of fish data structure
        fish = {
        'right' : fishType['right'],
        'left' : fishType['left'],
        'colors' : colors,
        'hSpeed' : random.randint(1,6),
        'vSpeed' : random.randint(5,15),
        'timeToHDirChange': random.randint(10,60),
        'timeToVDirChange' : radnom.randint(2, 20),
        'goingRight' : random.choice([True, False]),
        'goingDown' : random.choice([True, False])
        }

        # 'x' is the leftmost side of the fish body:
        fish['x'] = random.randint(0, WIDTH - 1 - LONGEST_FISH_LENGTH)
        fish['y'] = random.randint(0, HEIGHT - 2)
        return fish


def simulateAquarium():
    """ Simulate the movements in teh aquarium for one step"""
    global FISHES, BUBBLERS, BUBBLES, KELP, STEP

    # Simulate fishes for one STEP
    for fish in FISHES:
        # Move fishes horizontally
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x']








        }


        #
