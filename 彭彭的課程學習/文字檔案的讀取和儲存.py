# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 09:53:59 2018

@author: Home love

檔案物件=open(檔案路徑,mode=開啟模式)
讀取模式 - r
寫入模式 - w
讀寫模式 - r+

#讀取全部文字
檔案物件.read()

for 變數 in 檔案物件:
     從檔案依序讀取每行文字到變數中

#讀取JSON格式
import json
讀取到的資料=json.load(檔案物件)

json.dump(要寫入的資料,檔案物件)

檔案物件.write(字串)
檔案物件.write("這是範例文字\n")

檔案物件.close()
with open(檔案路徑,mode=開啟模式)as 檔案物件:
     讀取或寫入檔案的模式
#以上區塊會自動且安全的關閉檔案
"""

file=open("data.txt",mode="w") #開啟
file.write("hello file\nWhat the fuck") #寫入
file.close() #關閉

#############################################################################
file=open("chinese.txt",mode="w",encoding='utf-8') #開啟
file.write("你好啊\n旅行者") #寫入
file.close() #關閉

#############################################################################
#最佳實務做法
with open('jaychou.doc',mode='w',encoding='utf-8')as file:
     file.write('素胚勾勒出青花筆鋒濃轉淡\n瓶身描繪的牡丹一如妳初妝\n冉冉檀香透過窗心事我了然\n宣紙上走筆至此擱一半\n\n釉色渲染仕女圖韻味被私藏\n而妳嫣然的一笑如含苞待放\n妳的美一縷飄散 去到我去不了的地方\n\n天青色等煙雨 而我在等妳\n炊煙裊裊昇起 隔江千萬里\n在瓶底書漢隸仿前朝的飄逸\n就當我為遇見妳伏筆\n\n天青色等煙雨 而我在等妳\n月色被打撈起 暈開了結局\n如傳世的青花瓷自顧自美麗 \n妳眼帶笑意\n\n色白花青的錦鯉躍然於碗底\n臨摹宋體落款時卻惦記著妳\n妳隱藏在窯燒裡千年的秘密\n極細膩猶如繡花針落地\n\n簾外芭蕉惹驟雨門環惹銅綠\n而我路過那江南小鎮惹了妳\n在潑墨山水畫裡 妳從墨色深處被隱去\n\n天青色等煙雨 而我在等妳\n炊煙裊裊昇起 隔江千萬里\n在瓶底書漢隸仿前朝的飄逸\n就當我為遇見妳伏筆\n\n天青色等煙雨 而我在等妳\n月色被打撈起 暈開了結局\n如傳世的青花瓷自顧自美麗\n妳眼帶笑意\n\n天青色等煙雨 而我在等妳\n炊煙裊裊昇起 隔江千萬里\n在瓶底書漢隸仿前朝的飄逸\n就當我為遇見妳伏筆\n\n天青色等煙雨 而我在等妳\n月色被打撈起 暈開了結局\n如傳世的青花瓷自顧自美麗\n妳眼帶笑意')

#讀取檔案
with open('jaychou.doc',mode='r',encoding='utf-8')as file:
     data=file.read()
print(data)

#############################################################################
#算術總和
with open('data.doc',mode='w',encoding='utf-8')as file:
     file.write('5\n3\n4\n8')
     
#讀取檔案,把檔案中的數字資料,一行一行的讀取出來,並計算總合     
sum=0
with open('data.doc',mode='r',encoding='utf-8')as file:
     for line in file:
          sum+=int(line)
print(sum)

"""

## Write File
path = "htmlTest"  # 你檔案想要存放的檔名，如果沒給路徑、直接寫檔名，將存在與你現在所執行的python檔同一個資料夾中
file = open(path, 'w', encoding='utf8')  
# 第一個參數(path): 如果該路徑下，有相同檔名的檔案，將會直接複寫且不可回復。若沒有，系統則會自動幫你開一個新檔案
# 第二個參數('w'): 一般來說，我只用到'w'以及'r'，分別是'寫'與'讀'的意思，其他二進位檔案的讀寫方式，各位有興趣可以自行去研究。如果要讀檔案，直接把'w'改成'r'即可。
# 第三個參數(encoding='utf8'): 指的是開啟這個檔案所使用的編碼，因為windows如果是中文版的，預設打開編碼是cp950(滿討厭的)，所以在寫入檔案的時候，最好用utf8編碼，裡面的字才不會跑掉。
file.write(re.text)
file.close()  # 寫完要關掉檔案，才會成功存檔。
## Read File 如果你已經把上面程式碼成功執行，則可以往下試著把它讀出來
path = "htmlTest"  
file = open(path, 'r', encoding='utf8')  
# 三種讀取方式，每次打開檔案請擇一使用，若重複使用會出現問題。
# 一、一次全部讀出來
context = file.read()
# 二、一次讀一行出來
file.readline() ##讀第一行
file.readline() ##讀第二行
file.readline() ##讀第三行
# 三、透過迴圈方式一次讀一行出來
for line in file:
    print(line)
file.close()

"""