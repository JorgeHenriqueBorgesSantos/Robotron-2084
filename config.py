import pygame

pygame.display.init()

# Game display
game_name = "Robotronic 2084"
screen_height = 800
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(game_name)
sprite_sheet = "assets/sprites/Robotron-Sprites.jpg"
sprite_sheet_size = [308, 203]
icon_scale = 3
icon_image_load = pygame.image.load(sprite_sheet)
icon_image_load = pygame.transform.scale(icon_image_load, [308 * icon_scale, 203 * icon_scale])
icon = pygame.surface.Surface((25, 25))
icon.blit(icon_image_load, (0, 0), (173*icon_scale, 82*icon_scale, 25, 25))
pygame.display.set_icon(icon)

# Player
player_spritesheet = "assets/sprites/Robotron-Sprites.jpg"
scale = 2.6
player_frame_width = 14 * scale
playerspritestart = (92 * scale, 80 * scale)
playerspriteend = (14 * scale, 15 * scale)
player_left = (92 * scale, 132 * scale)
player_right = (130 * scale, 172 * scale)
player_down = (170 * scale, 198 * scale)
player_up = (208 * scale, 248 * scale)
player_speed = 25
player_img_cooldown = 80
player_facing_down = 172 * scale
player_facing_right = 130 * scale
player_facing_left = 92 * scale
player_facing_up = 208 * scale

# Bullet
bullet_sprite = "assets/sprites/bullet_sprite.png"

# Wall
wall_img = "assets/sprites/walls.png"
wall_upper_lim = 60
wall_bottom_lim = 725
wall_left_lim = 7
wall_right_lim = 760


