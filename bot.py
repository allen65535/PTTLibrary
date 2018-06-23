import sys
import time
import json
import getpass
import codecs
import re
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# 如果你想要自動登入，建立 account.json
# 然後裡面填上 {"ID":"YourID", "Password":"YourPW"}

BoardList = ['Wanted', 'Gossiping', 'Test', 'NBA', 'Baseball', 'LOL', 'C_Chat']

PTTBot = None
ResPath = './OldBug/'

def CheckAnsInArticle(board, postIndex, answer, skipNumberOfPushes = 0):
    ErrCode, Post = PTTBot.getPost(board, PostIndex=postIndex)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('使用文章編號取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))

    pushList = Post.getPushList()
    # skip pushCheckedCount pushes
    for Push in pushList[skipNumberOfPushes:]: 
        author = Push.getAuthor()
        content = Push.getContent()
        found = re.search('\*(.+)', content)
        if found != None:
            guess = found.group(1)
            if guess == answer:
                print(author + ':' + guess + ' 正確答案!!')
                break
            else:
                print(author + ':' + guess + ' 錯誤...')
    return author, guess, len(pushList)

# 聯想tempo遊戲流程規劃
def thinkTempo():
    # var init
    HINT_TIME = 30

    # init題目
    questions = ['把握', '心電圖', '得罪']

    # 接受報名
    answerPlayers = []
    hintPlayers = []
    PostIndex = 500  # 文章號碼
    Board = 'test'

    gamePrepared = False
    pushCheckedCount = 0
    
    # 持續檢查報名狀況
    while(not gamePrepared):
        ErrCode, Post = PTTBot.getPost(Board, PostIndex=PostIndex)
        if ErrCode != PTT.ErrorCode.Success:
            PTTBot.Log('使用文章編號取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))

        # skip pushCheckedCount pushes
        for Push in Post.getPushList()[pushCheckedCount:]: 
            author = Push.getAuthor()
            content = Push.getContent()
            # if 有報名指令  answerPlayers.push(author)...
        
        # wait 10 sec
        # if time is due or there are enougth players
        #  =>  gamePrepared = True
    

    #開始遊戲
    # 推文 遊戲開始!
    for question in questions:
        for hintPlayer in hintPlayers:
            # 寄送 question 給 hintPlayer
        # wait 30 secs

        # 推文 ══════════╡ 提示開始 ╞══════════
        # wait HINT_TIME
        # 推文 ══════════╡ 提示結束 ╞══════════
            roundComplete = False
            # while(not roundComplete):
                # 取得新的推文
                # if 推文為答題者第一次回答 and 正確  
                #   roundComplete = True
                #   推文  =========答體者: 答案 答對! [比數]
            
def DetectAndEditPost():
    Board = 'TEST'  # 看板
    PostIndex = 500  # 文章號碼
    ErrCode, Post = PTTBot.getPost(Board, PostIndex=PostIndex)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('使用文章編號取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))

    editMsg = ""
    for Push in Post.getPushList():
        print(Push.getAuthor() + ':' + Push.getContent())
        if '[指令]' in Push.getContent():
            editMsg = Push.getAuthor() + '使用了指令' + Push.getContent().replace('[指令]', '')

    PTTBot.gotoBoard(Board)
    PTTBot.gotoArticle(PostIndex)
    PTTBot.editArticle(editMsg)

if __name__ == '__main__':
    print('Welcome to PTT Library v ' + PTT.Version + ' Demo')

    if len(sys.argv) == 2:
        if sys.argv[1] == '-ci':
            print('CI test run success!!')
            sys.exit()

    try:
        with open('Account.json') as AccountFile:
            Account = json.load(AccountFile)
            ID = Account['ID']
            Password = Account['Password']
    except FileNotFoundError:
        ID = input('請輸入帳號: ')
        Password = getpass.getpass('請輸入密碼: ')
    
    PTTBot = PTT.Library(ID, Password)

    ErrCode = PTTBot.login()
    PTTBot.Log(ErrCode)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('登入失敗')
        PTTBot.Log(ErrCode)
        sys.exit()
    
    PTTBot.Log('登入成功? 進行動作...')
    try:
        author, guess, length = CheckAnsInArticle('turtlesoup', 27233, '玩具', 0)
        PTTBot.Log(author + ':' + guess + '--' + str(length))
        pass
    except Exception as e:
        print(e)
        PTTBot.Log('接到例外 啟動緊急應變措施')
    # 請養成登出好習慣
    PTTBot.logout()