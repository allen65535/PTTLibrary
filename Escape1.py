# -*- coding: big5 -*-
import sys
import time
import json
import getpass
import codecs
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# 偵測推文並編輯文章的函式
def DetectAndEditPost(CommandMsg, ReturnMsg):
    Check = 0
    while True:
        if Check == 1:
            break # 離開while迴圈
        CorrectMsg = ""
        
        # 取得文章動作放在迴圈裡，是為了重新讀取所有推文，以讀到新推文
        ErrCode, Post = PTTBot.getPost(Board, PostIndex=PostIndex)
        if ErrCode != PTT.ErrorCode.Success:
            PTTBot.Log('使用文章編號取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))
        
        # 檢查每一行推文，若沒有推文則不會進入此迴圈
        for Push in Post.getPushList():
            if CommandMsg in Push.getContent():
                print(Push.getAuthor() + ':' + Push.getContent())
                
                CorrectMsg = Push.getAuthor() + '使用了指令' \
                + Push.getContent().replace('[指令]', '') + '\r' + ReturnMsg
                PTTBot.editArticle(CorrectMsg) # 編輯文章
                
                Check = 1
                break # 離開for迴圈
            else:
                pass

# 登入
try:
    with open('Account.json') as AccountFile:
        Account = json.load(AccountFile)
        ID = Account['ID']
        Password = Account['Password']
except FileNotFoundError:
    ID = input('請輸入帳號: ')
    Password = getpass.getpass('請輸入密碼: ')
PTTBot = PTT.Library(ID, Password, kickOtherLogin=False, _LogLevel=PTT.LogLevel.DEBUG)

# 推文範例
# PTTBot.push(Board, PTT.PushType.Arrow, 'PTT Library Push API 4', PostIndex=470)
# PTTBot.push(Board, PTT.PushType.Arrow, 'PTT Library Push API 4', '#1RF7DoYg')

try:
    # 前置設定
    Board = 'TEST'  # 看板
    PostIndex = 624  # 文章號碼
    PTTBot.gotoBoard(Board)
    PTTBot.gotoArticle(PostIndex)
    
    PTTBot.push(Board, PTT.PushType.Arrow, '遊戲開始！', PostIndex=PostIndex)
    
    # 主要遊戲內容
    DetectAndEditPost('[調查][屍體]', \
    '[屍體]異常地冰冷，但你沒有看到屍體上有任何外傷或血跡。' + '\r' +\
    '你在屍體旁邊發現了一張[紙條]。')
    
    DetectAndEditPost('[調查][紙條]', \
    '你周圍的東西有[保險箱]、[電視]、[大門]。' + '\r' +\
    '你可能會想做的動作有[打破]、[摔爛]、[拆下XX]。')
    
    DetectAndEditPost('[調查][保險箱]', \
    '[保險箱]上面有3位數的[密碼鎖]。')
    
    DetectAndEditPost('[調查][電視]', \
    '你覺得你需要用遙控器才能打開[電視]。')
    
    DetectAndEditPost('[調查][大門]', \
    '門上有一幅畫：' + '\r' +\
    'https://imgur.com/a/1EslXrB')
    
    DetectAndEditPost('[密碼鎖][423]', \
    '你打開了[保險箱]，在裡面找到了[電視的遙控器]')
    
    DetectAndEditPost('[電視][電視的遙控器]', \
    '[電視]螢幕出現了這個畫面：' + '\r' +\
    'https://imgur.com/a/oTmyA19')
    
    DetectAndEditPost('[電視][摔爛]', \
    '你在[電視]裡面找到了螺絲起子。')
    
    DetectAndEditPost('[屍體][拆下左手]', \
    '你辨認出屍體其實是一個機器人，你用螺絲起子拆下了它的[左手]。' + '\r' +\
    '你在它的[左手]裡面找到了[星型螺絲起子]。')
    
    DetectAndEditPost('[自己][星型螺絲起子]', \
    '你回想起自己其實也是一個機器人，你用[星型螺絲起子]拆下了[自己]的[左手]。' + '\r' +\
    '你在[自己]的[左手]裡面找到了鐵鎚。')
    
    DetectAndEditPost('[大門][打破]', \
    '你用鐵鎚打破了大門，' + '\r' +\
    '門外的機器人恭喜你通過了測試。')
    
except Exception as e:
    print(e)
    PTTBot.Log('接到例外 啟動緊急應變措施')

# 登出
PTTBot.logout()
