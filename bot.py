import sys
import time
import json
import getpass
import codecs
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# 如果你想要自動登入，建立 account.json
# 然後裡面填上 {"ID":"YourID", "Password":"YourPW"}

BoardList = ['Wanted', 'Gossiping', 'Test', 'NBA', 'Baseball', 'LOL', 'C_Chat']

PTTBot = None
ResPath = './OldBug/'

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
        sys.exit()
    
    PTTBot.Log('登入成功? 進行動作...')
    try:
        DetectAndEditPost()
        pass
    except Exception as e:
        print(e)
        PTTBot.Log('接到例外 啟動緊急應變措施')
    # 請養成登出好習慣
    PTTBot.logout()