import sys
from time import sleep

import pygame
from picture import Picture
from button import Button
from picture import Picture

class Cover:
        """管理游戏覆盖物的类"""

        def __init__(self, setting, screen):  # 游戏参数设置和游戏主界面
                self.setting = setting
                self.screen = screen
                self.winButton = Button(self.screen, 'Congratution')

                self.covers = []  # 存储未被点击过的方块的覆盖物的位置
                self.sign_covers=[]
                for i in range(20):
                        for j in range(20):
                                self.covers.append([i, j])  # 刚开始时整个界面都是被覆盖的

        def delete(self, x, y):  # 传入单机鼠标的位置，判断是否合法，如果是，删除当前方块
                x = x // 25
                y = y // 25
                if [x, y] in self.covers:
                        self.covers.remove([x, y])


        def sign(self,x,y):
            x = x // 25
            y = y // 25
            self.sign_covers.append([x,y])


        picture=Picture()

        def show(self):  # 将所有未被点击过的方块展现出来
                for cur in self.covers:
                    if cur in self.sign_covers:
                        self.screen.blit(self.picture.sign, (cur[0] * 25, cur[1] * 25))
                    else:
                        self.screen.blit(self.picture.fugai, (cur[0]*25, cur[1]*25))
                        #pygame.draw.rect(self.screen, self.setting.screen_color, ((cur[0] * 25, cur[1] * 25), (24, 24)))

                if len(self.covers) <= 40:
                        self.winButton.display()
                        pygame.display.update()
                        sleep(3)
                        sys.exit()
