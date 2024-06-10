import pygame
import random

pygame.init()

# 游戏框架
W = 400      # 窗口宽度
H = 400      # 窗口高度
S = 20       # 方块大小
BG_COLOR = (200, 200, 200)
BLOCK_COLOR = (0, 0, 0)
TIME_DELAY = 100

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("贪吃蛇游戏")

font = pygame.font.Font(None, 36)

# 贪吃蛇初始化
snake_bodies = [(60, 20), (40, 20), (20, 20)]
(head_x, head_y) = snake_bodies[0]
dx, dy = S, 0

food_position = (random.randint(1, (W-S)//S)*S, random.randint(1, (H-S)//S)*S)


def draw_block(position):
    """绘制方块"""
    rect = (position[0], position[1], S, S)
    pygame.draw.rect(screen, BLOCK_COLOR, rect)


def move(snake_bodies, dx, dy):
    """移动贪吃蛇"""
    new_head = (snake_bodies[0][0] + dx, snake_bodies[0][1] + dy)

    if new_head == food_position:
        # 吃到食物
        snake_bodies.insert(0, new_head)
        generate_food()
    else:
        # 没有吃到食物
        snake_bodies.insert(0, new_head)
        snake_bodies.pop()

    return snake_bodies

def generate_food():
    """生成随机食物"""
    global food_position
    food_position = (random.randint(1, (W-S)//S)*S, random.randint(1, (H-S)//S)*S)

# 游戏主循环
while True:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -S
            elif event.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, S
            elif event.key == pygame.K_LEFT and dx == 0:
                dx, dy = -S, 0
            elif event.key == pygame.K_RIGHT and dx == 0:
                dx, dy = S, 0

    screen.fill(BG_COLOR)

    # 绘制贪吃蛇和食物
    for body in snake_bodies:
        draw_block(body)

    draw_block(food_position)

    # 移动贪吃蛇
    snake_bodies = move(snake_bodies, dx, dy)

    # 判断是否死亡
    (head_x, head_y) = snake_bodies[0]
    if head_x < 0 or head_x > W-S or head_y < 0 or head_y > H-S or (head_x, head_y) in snake_bodies[1:]:
        # 显示游戏结束信息，然后退出游戏
        text = font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])
        pygame.display.flip()
        pygame.time.delay(5000)
        pygame.quit()
        quit()

    pygame.display.flip()
    pygame.time.delay(TIME_DELAY)
