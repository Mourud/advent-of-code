import sys
import time
from aoc_input_fetcher import fetch_input
import pygame
# area = [11, 7]
area = [101, 103]

def main():
    data = fetch_input(__file__)
    # data = f"p=0,4 v=3,-3\np=6,3 v=-1,-3\np=10,3 v=-1,2\np=2,0 v=2,-1\np=0,0 v=1,3\np=3,0 v=-2,-2\np=7,6 v=-1,-3\np=3,0 v=-1,-2\np=9,3 v=2,3\np=7,3 v=-1,2\np=2,4 v=2,-3\np=9,5 v=-3,-3"
    data = parse_data(data)

    area = [103,101]
    # area = [7, 11]
    print(part1(data))
    print(part2(data))


def parse_data(data):
    robots = []
    for line in data.splitlines():
        pos, vel = line.split(" ")
        pos = pos.split("p=")[1]
        pos = pos.split(",")
        pos = [int(p) for p in pos]
        vel = vel.split("v=")[1]
        vel = vel.split(",")
        vel = [int(v) for v in vel]
        robots.append([pos, vel])
    return robots


def part1(data):
    for t in range(100):
        for robot in data:
            robot[:] = update(robot)
    for robot in data:
        add_into_q(robot[0])
    total = 1
    for row in quarters:
        for num_of_robots in row:
            total *= num_of_robots
    return total


quarters = [[0, 0], [0, 0]]


def add_into_q(pos):
    i = 0
    j = 0
    i_mid = (area[0]) // 2
    j_mid = (area[1]) // 2
    if pos[0] != i_mid and pos[1] != j_mid:
        if pos[0] > i_mid:
            i = 1
        if pos[1] > j_mid:
            j = 1
        quarters[i][j] += 1


def update(robot):
    pos, vel = robot
    for i in range(2):
        pos[i] += vel[i]
        pos[i] %= area[i]
    return [pos, vel]

def part2(data):

    # Initialize pygame
    pygame.init()

    # Parameters
    pixel_size = 10  # Size of each pixel
    screen_width, screen_height = area[0] * pixel_size, area[1] * pixel_size
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Christmas Tree")

    # Variables for controlling frames
    running = True
    paused = False
    current_frame = 67
    dir = 103
    max_frames = 103*101  # Define the maximum number of frames
    frames = []  # To store pre-computed displays
    font = pygame.font.SysFont("Arial", 24)  # Built-in font with size 24


    # Precompute frames and store them in the `frames` list
    for t in range(max_frames +1):
        display = [[0 for _ in range(area[0])] for _ in range(area[1])]
        for robot in data:
            robot[:] = update(robot)
            x, y = robot[0]
            display[y][x] += 1
        frames.append(display)
    timer = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:  # Go to previous frame
                    current_frame = max(0, current_frame - dir)
                if event.key == pygame.K_RIGHT:  # Go to next frame
                    current_frame = min(max_frames - 1, current_frame + dir)
                if event.key == pygame.K_SPACE:  # Pause/unpause
                    paused = not paused
        
        text_surface = font.render(f"Time: {current_frame}", True, (255, 255, 255))
        if not paused:
            current_frame = (current_frame + dir) % max_frames


        # Clear the screen
        screen.fill((0, 0, 0))

        # Get the current frame display
        display = frames[current_frame]
        # Draw the display
        for y in range(area[1]):
            for x in range(area[0]):
                intensity = int((display[y][x] / 5) * 255)  # Scale 0-5 to 0-255
                color = (intensity, intensity, intensity)  # Grayscale color
                pygame.draw.rect(screen, color, (x * pixel_size, y * pixel_size, pixel_size, pixel_size))

        screen.blit(text_surface, (10, 10))  # Top-left corner
        # Update the screen
        pygame.display.flip()

        pygame.time.delay(100)  # Small delay to control the speed of movement

    # Quit pygame
    pygame.quit()

    
def render_in_place(lines):
    # Move the cursor up for each line to be re-rendered
    sys.stdout.write("\033[F" * len(lines))  # Move up `len(lines)` lines
    for line in lines:
        sys.stdout.write(f"\r{line}\n")  # Write the new line and move to the next
    sys.stdout.flush()


    
main()
