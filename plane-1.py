import pygame
from pygame.locals import *


def main():
    # 创建窗口界面
    screen = pygame.display.set_mode((350, 500))
    # 设置背景图像
    background = pygame.image.load("./files/background.gif")
    # 设置窗口标题
    pygame.display.set_caption("飞机大战")
    # 设置背景音乐
    pygame.mixer.init()
    pygame.mixer.music.load("./files/house_lo.mp3")
    pygame.mixer.music.set_volume(0.2)   # 设置音量
    pygame.mixer.music.play(-1)     # -1表示无限循环播放

    # 载入玩家对象图片（飞机）
    plane = pygame.image.load('./files/alien1.gif')
    # 初始化玩家位置
    plane_x, plane_y = 135, 440

    while True:
        # 显示背景图片
        screen.blit(background, (0, 0))
        # 显示玩家图片 ()
        screen.blit(plane, (plane_x, plane_y))

        # 获取键盘事件
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == QUIT:
                print("退出")
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_a or event.key == K_LEFT:
                    print("left")
                    if plane_x > 0:
                        plane_x -= 10
                elif event.key == K_d or event.key == K_RIGHT:
                    print("right")
                    if plane_x < 270:
                        plane_x += 10
                elif event.key == K_SPACE:
                    print("发射")
        # 更新显示内容
        pygame.display.update()


if __name__ == '__main__':
    main()

