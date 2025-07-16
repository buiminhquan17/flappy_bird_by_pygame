import pygame


# Define constant for the screen width and height
SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 600
BLACK_COLOR: list[int] = [0, 0, 0]


class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super(Player, self).__init__()
        self.__surface = pygame.Surface([65, 180])
        self.__surface.fill([255, 255, 255])
        self.__rectangle = self.__surface.get_rect()

    def get_surface(self) -> pygame.Surface:
        return self.__surface

    def get_rectangle(self) -> pygame.Rect:
        return self.__rectangle

    def out_of_screen(self, dx: int, dy: int) -> bool:
        new_rect = self.__rectangle.move(dx, dy)
        return not (
            0 <= new_rect.left <= SCREEN_WIDTH - self.__rectangle.width
            and 0 <= new_rect.top <= SCREEN_HEIGHT - self.__rectangle.height
        )

    def update_position(self, key_pressed) -> None:
        if key_pressed[pygame.K_w] and not self.out_of_screen(0, -5):
            self.__rectangle.move_ip(0, -5)
        if key_pressed[pygame.K_s] and not self.out_of_screen(0, 5):
            self.__rectangle.move_ip(0, 5)
        if key_pressed[pygame.K_d] and not self.out_of_screen(5, 0):
            self.__rectangle.move_ip(5, 0)
        if key_pressed[pygame.K_a] and not self.out_of_screen(-5, 0):
            self.__rectangle.move_ip(-5, 0)


def main() -> None:
    # Initialize pygame
    pygame.init()

    # Create the screen object
    # The size determinied by the constant SCREEN_WIDTH and SCREEN_HEIGHT
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    # Initialize Player object
    player: Player = Player()

    running: bool = True

    # The game loop
    while running:
        # Look at every event in the queue
        for event in pygame.event.get():
            # Press the Escape key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            # Click the close button
            if event.type == pygame.QUIT:
                running = False

        player.update_position(pygame.key.get_pressed())

        # Fill the screen with black color
        screen.fill(BLACK_COLOR)

        # Draw the player
        screen.blit(player.get_surface(), player.get_rectangle())

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
