import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BORDER_COLOR = (250, 250, 250)  # Light gray for brick borders
BRICK_COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (75, 0, 130)]

# Paddle settings
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 15
paddle_speed = 10

# Ball settings
BALL_RADIUS = 10

# Brick settings
BRICK_ROWS = 15
BRICK_COLS = 11
BRICK_WIDTH = WIDTH // BRICK_COLS
BRICK_HEIGHT = 20

# Font settings
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 36)

def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        brick_row = []
        for col in range(BRICK_COLS):
            brick_x = col * BRICK_WIDTH
            brick_y = row * BRICK_HEIGHT
            brick_row.append(pygame.Rect(brick_x, brick_y, BRICK_WIDTH, BRICK_HEIGHT))
        bricks.append(brick_row)
    return bricks

def draw_bricks(bricks):
    for row_idx, row in enumerate(bricks):
        for brick in row:
            if brick:
                # Draw the brick's main fill color
                pygame.draw.rect(screen, BRICK_COLORS[row_idx % len(BRICK_COLORS)], brick)
                # Draw the border
                pygame.draw.rect(screen, BORDER_COLOR, brick, 2)

def game_over_screen(score):
    screen.fill(BLACK)
    game_over_text = font.render("Game Over", True, WHITE)
    restart_text = small_font.render("Press SPACE to Restart", True, WHITE)
    score_text = small_font.render(f"Score: {score}", True, WHITE)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 3))
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 3 + 150))
    screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()

def main():
    # Game variables
    paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
    paddle_y = HEIGHT - 50
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_speed_x, ball_speed_y = 4, -4  # Initialize ball speed here
    bricks = create_bricks()
    score = 0
    running = True
    game_over = False

    while running:
        if game_over:
            game_over_screen(score)

            # Wait for space key to restart
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # Reset game variables
                    paddle_x = WIDTH // 2 - PADDLE_WIDTH // 2
                    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
                    ball_speed_x, ball_speed_y = 4, -4  # Reinitialize ball speed
                    bricks = create_bricks()
                    score = 0
                    game_over = False
        else:
            screen.fill(BLACK)

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Paddle movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle_x > 0:
                paddle_x -= paddle_speed
            if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH:
                paddle_x += paddle_speed

            # Ball movement
            ball_x += ball_speed_x
            ball_y += ball_speed_y

            # Ball collision with walls
            if ball_x <= 0 or ball_x >= WIDTH - BALL_RADIUS:
                ball_speed_x *= -1
            if ball_y <= 0:
                ball_speed_y *= -1

            # Ball collision with paddle
            paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
            if paddle_rect.collidepoint(ball_x, ball_y + BALL_RADIUS):
                ball_speed_y *= -1

            # Ball collision with bricks
            for row in bricks:
                for brick in row:
                    if brick and brick.collidepoint(ball_x, ball_y):
                        ball_speed_y *= -1
                        row[row.index(brick)] = None
                        score += 10  # Increase score by 10 for each brick hit
                        break

            # Draw bricks, paddle, and ball
            draw_bricks(bricks)
            pygame.draw.rect(screen, WHITE, paddle_rect)
            pygame.draw.circle(screen, WHITE, (ball_x, ball_y), BALL_RADIUS)

            # Display score
            score_text = score_font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

            # Game over condition
            if ball_y > HEIGHT:
                game_over = True

            pygame.display.flip()
            pygame.time.Clock().tick(60)

if __name__ == "__main__":
    main()
    pygame.quit()
