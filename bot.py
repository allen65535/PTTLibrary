import sys
import time
import json
import getpass
import codecs
import re
from tinydb import TinyDB, Query
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# 如果你想要自動登入，建立 account.json
# 然後裡面填上 {"ID":"YourID", "Password":"YourPW"}

BoardList = ['Wanted', 'Gossiping', 'Test', 'NBA', 'Baseball', 'LOL', 'C_Chat']

PTTBot = None
ResPath = './OldBug/'

def Push(board, postIndex, msg):
    HOST_PUSH_PREFIX = '======='

    ErrCode = PTTBot.push(board, PTT.PushType.Push, HOST_PUSH_PREFIX + msg, PostIndex=postIndex)
    if ErrCode == PTT.ErrorCode.Success:
        PTTBot.Log('使用文章編號: 推文成功')
    elif ErrCode == PTT.ErrorCode.ErrorInput:
        PTTBot.Log('使用文章編號: 參數錯誤')
        return False
    elif ErrCode == PTT.ErrorCode.NoPermission:
        PTTBot.Log('使用文章編號: 無發文權限')
        return False
    else:
        PTTBot.Log('使用文章編號: 推文失敗')
        return False

def writeJsonFile(dictObj):
    with open('data.json', 'w') as outputFile:
        json.dump(dictObj, outputFile)

def getPostPushList(board, postIndex, skipNumberOfPushes = 0):
    PTTBot.Log('取得推文清單, 於:' + board + ', index:' + str(postIndex))
    ErrCode, Post = PTTBot.getPost(board, PostIndex=postIndex)
    if ErrCode != PTT.ErrorCode.Success:
        PTTBot.Log('使用文章編號取得文章詳細資訊失敗 錯誤碼: ' + str(ErrCode))

    pushList = Post.getPushList()
    return pushList[skipNumberOfPushes:]

def CheckCommandInPustList(command, pushList):
    PTTBot.Log('檢查指令:' + command)
    count = 0
    for Push in pushList:
        author = Push.getAuthor()
        content = Push.getContent()
        found = re.search(command, content)
        if found != None:
            return found, author, count
        count += 1
    return None, None, len(pushList)

def CheckCommandInArticle(board, postIndex, command, skipNumberOfPushes = 0):
    PTTBot.Log('開始檢查文章指令')
    pushList = getPostPushList(board, postIndex, skipNumberOfPushes)
    PTTBot.Log('取得推文列表')
    return CheckCommandInPustList(command, pushList)

def CheckAnsInArticle(board, postIndex, answer, skipNumberOfPushes = 0):
    pushList = getPostPushList(board, postIndex, skipNumberOfPushes)
    # skip pushCheckedCount pushes
    for Push in pushList: 
        author = Push.getAuthor()
        content = Push.getContent()
        found = re.search(r'\*(.+)', content)
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
    HINT_PLAYER_NUMBER = 2
    GUESS_PLAYER_NUMBER = 4

    PATTERN_REG_HINT = r'\[報名提示\]'
    PATTERN_REG_GUESS = r'\[報名猜題\]'

    # init題目
    questions = ['把握', '心電圖', '得罪']

    # 接受報名
    guessPlayers = []
    hintPlayers = []
    guessPlayerNameMap = {}
    hintPlayerNameMap = {}
    postIndex = 278  # 文章號碼
    board = 'test'

    gamePrepared = False
    pushHasCheckedHintRegister = 0
    pushHasCheckedGuessRegister = 0
    
    # 持續檢查報名狀況
    while(not gamePrepared):
        PTTBot.Log('檢查報名')
        # 檢查提示報名
        found, author, checkedIndex = CheckCommandInArticle(board, postIndex, PATTERN_REG_HINT, pushHasCheckedHintRegister)
        PTTBot.Log('檢查報名提示完成')
        if found != None:
            PTTBot.Log(author + '報名了提示')
            if (author not in hintPlayers):
                hintPlayers.append(author)
                Push(board, postIndex, author + '報名了提示成功')
        else:
            PTTBot.Log('未發現報名提示推文')
        pushHasCheckedHintRegister += checkedIndex

        # 檢查猜題報名
        found, author, checkedIndex = CheckCommandInArticle(board, postIndex, PATTERN_REG_GUESS, pushHasCheckedGuessRegister)
        if found != None:
            PTTBot.Log(author + '報名了猜題')
            if (author not in guessPlayers):
                guessPlayers.append(author)
                Push(board, postIndex, author + '報名了猜題成功')
            else:
                PTTBot.Log('未發現報名猜題推文')
        pushHasCheckedGuessRegister += checkedIndex
        
        
        time.sleep(10)

        if len(hintPlayers) == HINT_PLAYER_NUMBER and len(guessPlayers) == GUESS_PLAYER_NUMBER:
            gamePrepared = True
    
    PTTBot.Log('遊戲報名準備完成')

    #開始遊戲
    # 推文 遊戲開始!
    # for question in questions:
    #     for hintPlayer in hintPlayers:
            # 寄送 question 給 hintPlayer
        # wait 30 secs

        # 推文 ══════════╡ 提示開始 ╞══════════
        # wait HINT_TIME
        # 推文 ══════════╡ 提示結束 ╞══════════
            # roundComplete = False
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
        # author, guess, length = CheckAnsInArticle('turtlesoup', 27233, '玩具', 0)
        # PTTBot.Log(author + ':' + guess + '--' + str(length))
        thinkTempo()
        pass
    except Exception as e:
        print(e)
        PTTBot.Log('接到例外 啟動緊急應變措施')
    # 請養成登出好習慣
    PTTBot.logout()