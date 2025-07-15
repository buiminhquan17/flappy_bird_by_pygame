import pygame


def main() -> None:
    pygame.init()

    SCREEN_WIDTH: int = 500
    SCREEN_HEIGHT: int = 500
    BLACK_COLOR: list[int] = [0, 0, 0]

    # Set up the window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    running: bool = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BLACK_COLOR)

        pygame.draw.circle(screen, [0, 255, 0], [250, 250], 75)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
