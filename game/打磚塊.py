# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 16:03:53 2018

@author: liwei
"""

""" 
 Sample Breakout Game
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
""" 

# --- 引用函式

import math
import pygame

# 訂義顏色
黑色 = (0, 0, 0)
白色 = (255, 255, 255)
藍色 = (0, 0, 255)

# 磚塊大小
磚塊寬 = 23
磚塊高 = 15

class 磚塊(pygame.sprite.Sprite):
    """這個函式實作磚塊
    它使用了Pygame裡的"Sprite"類別 """

    def __init__(我, 顏色, x, y):
        """ 建構子. 傳遞變數x,y的位置與顏色. """
        
        # 呼叫父類別 (Sprite) 的建構子
        super().__init__()
        
        # 建立的適當大小的塊的圖像
        # 長度和寬度被傳到第1個參數的列表裡.
        我.image = pygame.Surface([磚塊寬, 磚塊高])
        
        # 幫磚塊上色
        我.image.fill(顏色)
        
        # 取得磚塊的維度
        我.rect = 我.image.get_rect()
        
        # 把方塊移動到左上角的x,y座標.
        # 方塊出現的地方.
        我.rect.x = x
        我.rect.y = y


class 球(pygame.sprite.Sprite):
    """ 這個函式實作球        
        它使用了Pygame裡的"Sprite"類別 """
    
    # 球彈起和下落的速度
    速度 = 9.0
    
    # 球座標(浮點數)
    x = 0.0
    y = 180.0
    
    # 球的方位 (角度)
    方向 = 200

    width = 10
    height = 10
    
    # 建構子. 傳遞磚塊的顏色和x,y座標
    def __init__(我):
        # 呼叫父類別 (Sprite) 的建構子
        super().__init__()
        
        # 建立球的形狀
        我.image = pygame.Surface([我.width, 我.height])
        
        # 球的顏色
        我.image.fill(白色)
        
        # 取得方塊物件並顯示
        我.rect = 我.image.get_rect()
        
        # 獲得螢幕 高與寬 的屬性
        我.視窗高 = pygame.display.get_surface().get_height()
        我.視窗寬 = pygame.display.get_surface().get_width()
    
    def 反彈(我, 差):
        """ 這個函式實作如何把碰到任何平面的球反彈 """
        我.方向 = (180 - 我.方向) % 360
        我.方向 -= 差
    
    def 更新(我):
        """ 更新球的方位"""
        # 把Sine and Cosine 從角度轉換弧度
        方向_radians = math.radians(我.方向)
        
        # 根據速度 方向 去轉換x,y座標
        我.x += 我.速度 * math.sin(方向_radians)
        我.y -= 我.速度 * math.cos(方向_radians)
        
        # 把圖像移動到x,y位置
        我.rect.x = 我.x
        我.rect.y = 我.y
        
        # 會不會反彈到視窗的最頂部?
        if 我.y <= 0:
            我.反彈(0)
            我.y = 1
            
        # 會不會反彈到視窗的最左邊?
        if 我.x <= 0:
            我.方向 = (360 - 我.方向) % 360
            我.x = 1
            
        # 會不會反彈到視窗的最右邊?
        if 我.x > 我.視窗寬 - 我.width:
            我.方向 = (360 - 我.方向) % 360
            我.x = 我.視窗寬 - 我.width - 1
        
        # 會不會掉到視窗的最底部?
        if 我.y > 600:
            return True
        else:
            return False

class 玩家(pygame.sprite.Sprite):
    """ 這個類別實作底下給玩家控制的控制條 """
    
    def __init__(我):
        """ 玩家建構子 """
        # 呼叫父類別建構子
        super().__init__()
        
        我.width = 75
        我.height = 15
        我.image = pygame.Surface([我.width, 我.height])
        我.image.fill((白色))
        
        # 傳遞左上角的位置.
        我.rect = 我.image.get_rect()
        我.視窗高 = pygame.display.get_surface().get_height()
        我.視窗寬 = pygame.display.get_surface().get_width()

        我.rect.x = 0
        我.rect.y = 我.視窗高-我.height
    
    def 更新(我):
        """ 更新玩家控制條位置 """
        # 取得滑鼠位置
        pos = pygame.mouse.get_pos()
        # 設定當滑鼠在左側時的位置
        我.rect.x = pos[0]
        # 確保我們不推槳玩家 
        # 關閉屏幕右側
        if 我.rect.x > 我.視窗寬 - 我.width:
            我.rect.x = 我.視窗寬 - 我.width

# 呼叫這個函式讓Pygame library 自己能夠初始化
pygame.init()

# 產生一個 800x600 視窗大小
螢幕 = pygame.display.set_mode([800, 600])

# 設定視窗名稱
pygame.display.set_caption('Breakout')

# 啟用以下功能確保滑鼠不會超出視窗外
pygame.mouse.set_visible(0)

# 這是我們使用在視窗上繪製文字的字體(大小 36)
font = pygame.font.Font(None, 36)         #font不能用中文字

# 建立一個我們可以在上面輸出圖像文字的介面
background = pygame.Surface(螢幕.get_size())   #background不能用中文字

# 創建精靈(電腦圖形學)列表
多磚塊 = pygame.sprite.Group()
多球 = pygame.sprite.Group()
全部的精靈 = pygame.sprite.Group()

# 創建玩家控制棒
使用者 = 玩家()
全部的精靈.add(使用者)

# 建立球
ball = 球()
全部的精靈.add(ball)
多球.add(ball)

# 磚塊頂端 (y 方向)
top = 80

#產生磚塊的數
blockcount = 32

# --- 建立多磚塊

# 5列磚塊
for row in range(5):
    # 32欄的磚塊
    for column in range(0, blockcount):
        # 建立方塊 (顏色,x座標,y座標)
        block = 磚塊(藍色, column * (磚塊寬 + 2) + 1, top)
        多磚塊.add(block)
        全部的精靈.add(block)
    # 移動下一個行的頂部向下
    top += 磚塊高 + 2

# 時脈限制速度
時脈 = pygame.time.Clock()

# 遊戲結束了嗎?
遊戲結束 = False

# 離開程式?
離開程式 = False

# 程式主要迴圈
while 離開程式 != True:

    # 視窗刷新速率限制在30禎
    時脈.tick(30)

    # 先將視窗初始化成黑色
    螢幕.fill(黑色)
    
    # 處理在遊戲中的事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            離開程式 = True
    
    # 只要遊戲沒有結束就更新球和玩家的位置

    if not 遊戲結束:
        # 更新球和玩家的位置
        使用者.更新()
        遊戲結束 = ball.更新()
    
    # 以上完成時印出遊戲結束
    if 遊戲結束:
        text = font.render("Game Over", True, 白色)     #Game Over為法換成中文 會有□□□□
        textpos = text.get_rect(centerx=background.get_width()/2)
        textpos.top = 300
        螢幕.blit(text, textpos)
    
    # 判斷球有沒有打到玩家控制棒
    if pygame.sprite.spritecollide(使用者, 多球, False):
        # 這裡的判斷反彈左或右 
        # 取決於打打到控制棒的位置
        差 = (使用者.rect.x + 使用者.width/2) - (ball.rect.x+ball.width/2)
        
        # 設定球的y座標 
        # 當球打到控制棒時
        ball.rect.y = 螢幕.get_height() - 使用者.rect.height - ball.rect.height - 1
        ball.反彈(差)
    
    # 檢查球是否打到磚塊
    dead多磚塊 = pygame.sprite.spritecollide(ball, 多磚塊, True)
    
    # 當球打到磚塊時，反彈
    if len(dead多磚塊) > 0:
        ball.反彈(0)
        
        # 全部磚塊都打掉時遊戲結束
        if len(多磚塊) == 0:
            遊戲結束 = True
    
    # 畫出任何東西
    全部的精靈.draw(螢幕)

    # 刷新螢幕並顯示畫好的圖示
    pygame.display.flip()

pygame.quit()