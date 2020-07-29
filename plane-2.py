import pygame
from pygame.locals import *
import random


class Plane:
    def __init__(self):
        # 飞机初始位置
        self.x = 135
        self.y = 440
        # 飞机的图片对象
        self.image_path = "./files/alien1.gif"
        self.image = pygame.image.load(self.image_path)
        self.bullets = []    # 存放子弹列表

    def show(self, screen):
        # 显示玩家图片
        screen.blit(self.image, (self.x, self.y))

        # 保存越界的子弹
        deleted_bullets = []
        # 筛选出越界的子弹
        for item in self.bullets:
            if item.b_judge():
                deleted_bullets.append(item)
        # 从bullets中去除越界的子弹
        for item in deleted_bullets:
            self.bullets.remove(item)
        # 显示飞机射击子弹
        for bullet in self.bullets:
            bullet.show(screen)
            bullet.move()

    def move_left(self, step):
        if self.x > 0:
            self.x -= step

    def move_right(self, step):
        if self.x < 270:
            self.x += step

    def shoot(self):
        bullet = Bullet(self.x, self.y)
        self.bullets.append(bullet)

    def key_control(self):
        # 获取键盘事件,按一下键盘按键执行一次操作
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                print("quit!")
                pygame.quit()
                exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    print("left")
                    self.move_left(10)
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    print("right")
                    self.move_right(10)
                elif event.key == pygame.K_SPACE:
                    print("shooting")
                    self.shoot()
        """
        # 按住键盘按键不松则执行连续操作
        key_list = pygame.key.get_pressed()
        if key_list[pygame.K_a] or key_list[pygame.K_LEFT]:
            print("left...")
            self.move_left(10)
        elif key_list[pygame.K_d] or key_list[pygame.K_RIGHT]:
            print("right...")
            self.move_right(10)
        elif key_list[pygame.K_SPACE]:
            print("发射...")
        """


class Bullet:
    def __init__(self, b_x, b_y):
        self.x = b_x + 34
        self.y = b_y - 20
        self.image = pygame.image.load('./files/shot.gif')

    def move(self):
        self.y -= 100

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))
        pass

    def b_judge(self):
        """
        判断子弹是否越界
        :return: bool
        """
        return self.y < 0


class EnemyPlane:
    def __init__(self):
        # 飞机初始位置
        self.x = 0
        self.y = 0
        # 设置一个方向值，0往右，1往左
        self.direction = 0
        # 飞机的图片对象
        self.image_path = "./files/alien2.gif"
        self.image = pygame.image.load(self.image_path)
        self.bullets = []  # 存放子弹列表

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

        # 保存越界的子弹
        deleted_bullets = []
        # 筛选出越界的子弹
        for item in self.bullets:
            if item.b_judge():
                deleted_bullets.append(item)
        # 从bullets中去除越界的子弹
        for item in deleted_bullets:
            self.bullets.remove(item)
        # 显示敌机射击子弹
        for bullet in self.bullets:
            bullet.show(screen)
            bullet.move()

    def shoot(self):
        bullet = EnemyBullet(self.x, self.y)
        self.bullets.append(bullet)

    def move(self):
        if self.direction:
            self.x -= 5
            if self.x < -5:
                self.direction = 0
            # print(self.x)
        if not self.direction:
            self.x += 5
            if self.x > 290:
                self.direction = 1
            # print(self.x)

    def control(self, screen):
        self.show(screen)
        rand = random.randint(1, 30)
        # 控制敌机发射子弹频率
        if rand == 6:
            self.shoot()
        # 控制敌机移动速度
        if rand % 1 == 0:
            self.move()
            # time.sleep(0.5)

    pass


class EnemyBullet:
    def __init__(self, b_x, b_y):
        self.x = b_x + 23
        self.y = b_y + 53
        self.image = pygame.image.load('./files/bomb.gif')

    def move(self):
        # 敌机子弹下降速度
        # rand = random.randint(1, 50)
        # if rand == 6:
        self.y += 2

    def show(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def b_judge(self):
        """
        判断敌机子弹是否越界
        :return: bool
        """
        return self.y > 500


def init_display():
    # 设置窗口标题
    pygame.display.set_caption("飞机大战")
    # 设置背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./files/house_lo.mp3")
    pygame.mixer.music.set_volume(0.2)  # 设置音量
    pygame.mixer.music.play(-1)  # -1表示无限循环播放


def main():
    # 创建窗口界面
    screen = pygame.display.set_mode((350, 500))
    # 设置背景图像
    background = pygame.image.load("./files/background.gif")
    # 设置初始化游戏界面
    init_display()

    # 创建玩家飞机对象
    plane = Plane()
    # 创建敌机对象
    enemy_plane = EnemyPlane()

    while True:
        # 显示游戏界面
        screen.blit(background, (0, 0))
        # 显示玩家飞机
        plane.show(screen)
        # 显示敌机，敌机移动和射击
        enemy_plane.control(screen)
        # 处理键盘事件
        plane.key_control()
        # 更新显示内容
        pygame.display.update()
        pygame.time.Clock().tick(20)


if __name__ == '__main__':
    main()
