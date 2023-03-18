import pygame

import bullets
import config
import controller
import player

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()


class Game:
    def __init__(self):
        self.joystick = pygame.joystick.Joystick(0)
        self.run = True
        self.screen = config.screen
        self.clock = pygame.time.Clock()
        self.playerGroup = pygame.sprite.Group()
        self.bullet_group = pygame.sprite.Group()
        self.player = player.Player(350, 350, config.player_speed, config.player_spritesheet,
                                    config.playerspritestart[0], config.playerspritestart[1])
        self.joy_axis = 0
        self.axis_value = 0
        self.player_joy = 0
        self.bullet = bullets.Bullet(config.bullet_sprite, self.player, self.player.rect.x,
                                     self.player.rect.y, 0, 0, 10, self.player.frame, self.axis_value, self.joy_axis)
        self.wall = pygame.image.load(config.wall_img)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                exit()

            if event.type == pygame.JOYAXISMOTION:
                self.joy_axis = event.axis
                self.axis_value = event.value
                self.player_joy = event.joy
                controller.Controller.move_player(self.player, self.player_joy, self.joy_axis, self.axis_value, 0, 1, 0,
                                                  config.player_speed)

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 10 and event.joy == 0:

                    self.bullet = bullets.Bullet(config.bullet_sprite, self.player, self.player.rect.x,
                                                 self.player.rect.y, 0, 0, 10, self.player.frame, self.axis_value, self.joy_axis)
                    self.bullet_group.add(self.bullet)

    def run_game(self):
        while self.run:
            self.dt = clock.tick() / 100
            self.now = pygame.time.get_ticks()
            self.sprite_update = pygame.time.get_ticks()
            self.cool_down = pygame.time.get_ticks()
            self.screen.fill("black")

            self.check_events()

            self.bullet_group.draw(self.screen)

            self.bullet_group.update()
            self.player.sprite_check(self.now)
            self.player.p_move(self.dt)
            self.playerGroup.add(self.player)
            self.playerGroup.draw(self.screen)
            self.playerGroup.update()
            self.screen.blit(self.wall, (0,0))
            self.player.collision()

            clock.tick(60)

            pygame.display.flip()


