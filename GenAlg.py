# Import library to be able to use draw tools
import random
import pygame
import math
from pygame.math import Vector2


# Increase or decrease by 100 with 1 or 2
NUM_OF_DOTS = 2000

# Increase or decrease by 1 with 3 or 4
VELS_TO_MUTATE = 5

# Increase or decrease by 1 with 5 or 6
LENGTH_PER_MUTATION = 3

# Increase or decrease by 5 with 7 or 8
VARIABILITY = 50

# Increase or decrease by 5 with 9 or 0
TIME_DENOMINATOR = 115

goal = Vector2(300, 0)
seed_boi = 0

VARIABILITY_new = 30
times_with_no_change = 0
prev_best_fitness = 9999
scatter_rate = 0
done = False


def get_seed():
    global seed_boi
    random.seed(seed_boi)
    seed_boi += 1


def make_box(scr, xt, yt, xb, yb):
    bx = Box(scr, xt, yt, xb, yb)
    boxes.append(bx)


def check_box_collisions(box):
    return dot.pos.x >= box.x_top and dot.pos.y >= box.y_top and dot.pos.x <= box.x_bot and dot.pos.y <= box.y_bot


def draw_boxes():
    for box in boxes:
        pygame.draw.rect(screen, BLUE, [box.x_top, box.y_top, box.x_bot - box.x_top, box.y_bot - box.y_top], 2)


class Box:
    def __init__(self, scr, xt, yt, xb, yb):
        self.x_top = xt
        self.y_top = yt
        self.x_bot = xb
        self.y_bot = yb
        pygame.draw.rect(scr, BLUE, [xt, yt, xb - xt, yb - yt], 2)


class Dot:
    def __init__(self, vels=None, new=False, mutate=False):
        self.pos = Vector2(300, 580)
        self.frame = 0
        self.time_to_explore = 60
        self.new = new
        self.dead = False
        self.fitness = 9999999
        self.vel_change_x = 0
        self.vel_change_y = 0
        self.is_best = not mutate
        if self.is_best:
            self.color = [255, 0, 0]
            self.radius = 5
        else:
            self.color = BLACK
            self.radius = 2
        self.velocity = Vector2(random.randint(-100, 100) / 100, random.randint(-100, 100) / 100)
        self.velocities = [self.velocity]
        self.new_vels = []
        self.hit_checkpoint = False
        if vels is not None:
            self.velocities = vels
            if mutate:
                self.mutate()
            self.velocity = self.velocities[0]

    def update(self):
        if self.new and len(self.velocities) > self.frame+scatter_rate:
            self.velocity = self.velocities[self.frame]
            self.new_vels.append(self.velocity)
            self.frame += 1
            if self.pos.distance_to(goal) < 50:
                self.time_to_explore = 1
        else:
            self.velocity = self.change_direction()
            self.new_vels.append(self.velocity)
        self.pos += self.velocity
        if self.pos.distance_to(goal)+time/TIME_DENOMINATOR < self.fitness:
            self.fitness = self.pos.distance_to(goal)+time/TIME_DENOMINATOR

    def draw(self):
        pygame.draw.circle(screen, self.color, [math.floor(self.pos.x), math.floor(self.pos.y)], self.radius)

    def kill(self):
        self.dead = True

    def mutate(self):
        """ Creates one mutation, 40 vels long.
        tmp_vecs = []
        get_seed()
        rand1 = random.randint(1, len(self.velocities)-40)
        get_seed()
        for n in range(0, rand1-1):
            tmp_vecs.append(self.velocities[n])
        for n in range(rand1, rand1 + 40):
            tmp_vecs.append(self.random_vector())
        for n in range(rand1 + 40, len(self.velocities)):
            tmp_vecs.append(self.velocities[n])
            """

        """ Mutates every tenth velocity by 4 velocities """
        tmp_vecs = []
        for n in range(0, len(self.velocities)):
            tmp_vecs.append(self.velocities[n])

        for i in range(VELS_TO_MUTATE):
            get_seed()
            rand1 = random.randint(1, len(self.velocities) - LENGTH_PER_MUTATION)
            for n in range(LENGTH_PER_MUTATION):
                tmp_vecs[rand1 + n] = self.random_vector()
        self.velocities = tmp_vecs

    def change_direction(self):
        return Vector2(random.randint(math.floor(100*self.velocity.x)-VARIABILITY, math.floor(100*self.velocity.x)+VARIABILITY) / 100,
        random.randint(math.floor(100*self.velocity.y)-VARIABILITY, math.floor(100*self.velocity.y)+VARIABILITY) / 100)

    def random_vector(self):
        get_seed()
        return Vector2(random.randint(-200, 200) / 100, random.randint(-200, 200) / 100)


# this is used to load the console
pygame.init()

# setting the size of the frame or specifying a region of an area
boxes = []
size = [600, 600]
screen = pygame.display.set_mode(size)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = [0, 0, 255]
make_box(screen, 0, 250, 400, 270)
make_box(screen, 150, 120, 600, 140)
make_box(screen, 200, 450, 600, 470)
make_box(screen, 380, 270, 400, 400)
dots = []
best_ever = Dot()
for i in range(0, NUM_OF_DOTS):
    dots.append(Dot())
highest_fitness = 10000
highest_fitness_dot = 0


def get_fitness(dot):
    return dot.fitness


# can use this line to display the title, but not needed for our scope
pygame.display.set_caption("First Prototype")

# this loop is used to keep the window opened until user closes out of window
done = False
clock = pygame.time.Clock()
time = 1

while not done:
    clock.tick(300)
    time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                NUM_OF_DOTS += 100
            elif event.key == pygame.K_2:
                if NUM_OF_DOTS > 200:
                    NUM_OF_DOTS -= 100
            elif event.key == pygame.K_3:
                VELS_TO_MUTATE += 1
            elif event.key == pygame.K_4:
                if VELS_TO_MUTATE > 0:
                    VELS_TO_MUTATE -= 1
            elif event.key == pygame.K_5:
                LENGTH_PER_MUTATION += 1
            elif event.key == pygame.K_6:
                if LENGTH_PER_MUTATION > 0:
                    LENGTH_PER_MUTATION -= 1
            elif event.key == pygame.K_7:
                VARIABILITY += 5
            elif event.key == pygame.K_8:
                if VARIABILITY > 0:
                    VARIABILITY -= 5
            elif event.key == pygame.K_9:
                TIME_DENOMINATOR += 5
                best_ever.fitness = 9999
            elif event.key == pygame.K_0:
                if TIME_DENOMINATOR > 0:
                    TIME_DENOMINATOR -= 5
                    best_ever.fitness = 9999

    dead_dots = [dot for dot in dots if dot.dead]
    if len(dead_dots) == len(dots) or time > 30000:
        dots.sort(key=get_fitness)
        if best_ever.fitness - prev_best_fitness < 1:
            times_with_no_change += 1
            if times_with_no_change > 2:
                if scatter_rate < 45:
                    scatter_rate += 15
        else:
            times_with_no_change = 0
            scatter_rate = 0
        if dots[0].pos.distance_to(goal) <= 10:
            scatter_rate = 0
        if dots[0].fitness < best_ever.fitness:
            prev_best_fitness = best_ever.fitness
            best_ever = dots[0]
        print(dots[0].fitness, end=" ")
        print(best_ever.fitness)
        highest_fitness_dot = []
        highest_fitness_dot.append(best_ever)
        highest_fitness_dot.append(dots[0])
        highest_fitness_dot.append(dots[1])
        highest_fitness_dot.append(dots[2])
        highest_fitness_dot.append(dots[3])
        highest_fitness_dot.append(dots[150])
        dots = []
        random.seed(1)
        for i in range(0, NUM_OF_DOTS):
            ran = random.randint(0, 100)
            if ran >= 60:
                dots.append(Dot(best_ever.new_vels, True, True))
            if ran < 60 and ran >= 40:
                dots.append(Dot(highest_fitness_dot[0].new_vels, True, True))
            if ran < 40 and ran >= 25:
                dots.append(Dot(highest_fitness_dot[1].new_vels, True, True))
            if ran < 25 and ran >= 10:
                dots.append(Dot(highest_fitness_dot[2].new_vels, True, True))
            if ran < 10 and ran >= 0:
                dots.append(Dot(highest_fitness_dot[3].new_vels, True, True))
        highest_fitness = 10000
        highest_fitness_dot = 0
        time = 1
        dots.append(Dot(best_ever.new_vels, new=True, mutate=False))

    # this line is used to clear the window and set background color (later background will be a portion
    # of a location on a map)
    screen.fill(WHITE)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render(str(NUM_OF_DOTS)+" "+str(VELS_TO_MUTATE)+" "+str(LENGTH_PER_MUTATION)+" "+str(VARIABILITY)+" "+str(TIME_DENOMINATOR), False, (0, 0, 0))
    screen.blit(textsurface, (0, 0))
    goal_dot = pygame.draw.circle(screen, BLUE, [300, 0], 10)
    # rect = pygame.draw.rect(screen, BLUE, [0, 250, 400, 20], 2)
    # rect = pygame.draw.rect(screen, BLUE, [200, 450, 400, 20], 2)
    draw_boxes()

    # draw circle
    for dot in dots:
        if dot.pos.x >= 595 or dot.pos.y >= 595 or dot.pos.x <= 5 or dot.pos.y <= 5:
            dot.kill()
        if dot.pos.x >= 400 and dot.pos.y >= 400 and dot.pos.x <= 420 and dot.pos.y <= 450 and dot.hit_checkpoint is False:
            dot.hit_checkpoint = True
            dot.fitness -= 100
        for box in boxes:
            if check_box_collisions(box):
                dot.kill()
        if not dot.dead:
            dot.update()
            dot.draw()
        else:
            dot.draw()

    # this line is used to display the drawings on the screen
    pygame.display.update()

# this line exits the program
pygame.quit()