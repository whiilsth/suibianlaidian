
from plane_sprites import *


class PlaneGame(object):

    def __init__(self):
        print("游戏初始化")
        # 1. 创建游戏的窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)  # size返回元组
        # 2.创建游戏的时钟
        self.clock = pygame.time.Clock()
        # 3.调用私有方法，精灵和精灵组
        self.__create_sprites()
        # 4.设置定时器事件 - 创建敌机
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 500)

    def __create_sprites(self):
        # 创建背景精灵和精灵组
        bg1 = Background()
        bg2 = Background(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)
        # 敌机精灵组
        self.enemy_group = pygame.sprite.Group()
        # 创建英雄精灵和精灵组，英雄定义属性
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)
        bg3 = Expiode()
        self.expiode_u = pygame.sprite.Group(bg3)

    def start_game(self):
        print("游戏开始")
        while True:
            # 1.刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 2.事件监听
            self.__event_handler()
            # 3.碰撞检测
            self.__check_collide()
            # 4.更新/绘制图像
            self.__update_sprites()
            # 5.更新显示
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            #  判断监听
            if event.type == pygame.QUIT:
                PlaneGame.__gam_over()
            elif event.type == CREATE_ENEMY_EVENT:
                print("敌机出场")
                # 创建敌机精灵
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)  # add向精灵组添加精灵
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")

        # 使用键盘提供的方法获取键盘 - 按键元组
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键索引值
        if keys_pressed[pygame.K_RIGHT]:
            # print("向右移动")
            self.hero.speed = 3
        elif keys_pressed[pygame.K_UP]:
            print("222")
            self.hero.speed_i = -3
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.speed_i = 3
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -3
        else:
            self.hero.speed = 0
            self.hero.speed_i = 0

    def __check_collide(self):
        # 1.子弹摧毁敌机
        enemies_i = pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        if enemies_i:
            pass
        # 2.敌机撞毁英雄
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        # 判断列表时候有内容
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            # 结束游戏
            PlaneGame.__gam_over()

    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        self.expiode_u.update()
        self.expiode_u.draw(self.screen)

    @staticmethod
    def __gam_over():
        print("游戏1结束")
        pygame.quit()
        exit()


if __name__ == "__main__":
    game = PlaneGame()
    game.start_game()
