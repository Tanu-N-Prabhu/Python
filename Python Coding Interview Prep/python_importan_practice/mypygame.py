import pygame


def main():
    print('Starting Game')
    print('Initialising pygame')
    # Required by every pygame application
    pygame.init()
    print('Initialising HelloWorldGame')
    bg = (255, 255, 255)
    display_width = 800
    display_height = 600
    display_surface = pygame.display.set_mode((display_width, display_height))
    x = (display_width * 0.05)
    y = (display_height * 0.05)
    display_surface.fill(bg)
    pygame.display.set_caption('Hello World')
    print('Update display')
    pygame.display.update()
    print('Starting main Game Playing Loop')
    clock = pygame.time.Clock()
    x_change = 0
    speed = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Received Quit Event:', event)
                running = False
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0
                x += x_change
                image_surface = pygame.image.load('/home/dhirajpatra/Pictures/tree.jpg').convert()
                display_surface.blit(image_surface, (x, y))
                pygame.display.update()
                clock.tick(60)

    print('Game Over')
    pygame.quit()


if __name__ == '__main__':
    main()
