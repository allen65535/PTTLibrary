# -*- coding: big5 -*-
import sys
import time
import json
import getpass
import codecs
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# ��������ýs��峹���禡
def DetectAndEditPost(CommandMsg, ReturnMsg):
    Check = 0
    while True:
        if Check == 1:
            break # ���}while�j��
        CorrectMsg = ""
        
        # ���o�峹�ʧ@��b�j��̡A�O���F���sŪ���Ҧ�����A�HŪ��s����
        ErrCode, Post = PTTBot.getPost(Board, PostIndex=PostIndex)
        if ErrCode != PTT.ErrorCode.Success:
            PTTBot.Log('�ϥΤ峹�s�����o�峹�ԲӸ�T���� ���~�X: ' + str(ErrCode))
        
        # �ˬd�C�@�����A�Y�S������h���|�i�J���j��
        for Push in Post.getPushList():
            if CommandMsg in Push.getContent():
                print(Push.getAuthor() + ':' + Push.getContent())
                
                CorrectMsg = Push.getAuthor() + '�ϥΤF���O' \
                + Push.getContent().replace('[���O]', '') + '\r' + ReturnMsg
                PTTBot.editArticle(CorrectMsg) # �s��峹
                
                Check = 1
                break # ���}for�j��
            else:
                pass

# �n�J
try:
    with open('Account.json') as AccountFile:
        Account = json.load(AccountFile)
        ID = Account['ID']
        Password = Account['Password']
except FileNotFoundError:
    ID = input('�п�J�b��: ')
    Password = getpass.getpass('�п�J�K�X: ')
PTTBot = PTT.Library(ID, Password, kickOtherLogin=False, _LogLevel=PTT.LogLevel.DEBUG)

# ����d��
# PTTBot.push(Board, PTT.PushType.Arrow, 'PTT Library Push API 4', PostIndex=470)
# PTTBot.push(Board, PTT.PushType.Arrow, 'PTT Library Push API 4', '#1RF7DoYg')

try:
    # �e�m�]�w
    Board = 'TEST'  # �ݪO
    PostIndex = 624  # �峹���X
    PTTBot.gotoBoard(Board)
    PTTBot.gotoArticle(PostIndex)
    
    PTTBot.push(Board, PTT.PushType.Arrow, '�C���}�l�I', PostIndex=PostIndex)
    
    # �D�n�C�����e
    DetectAndEditPost('[�լd][����]', \
    '[����]���`�a�B�N�A���A�S���ݨ����W������~�˩Φ��C' + '\r' +\
    '�A�b�������o�{�F�@�i[�ȱ�]�C')
    
    DetectAndEditPost('[�լd][�ȱ�]', \
    '�A�P�򪺪F�観[�O�I�c]�B[�q��]�B[�j��]�C' + '\r' +\
    '�A�i��|�Q�����ʧ@��[���}]�B[�L��]�B[��UXX]�C')
    
    DetectAndEditPost('[�լd][�O�I�c]', \
    '[�O�I�c]�W����3��ƪ�[�K�X��]�C')
    
    DetectAndEditPost('[�լd][�q��]', \
    '�Aı�o�A�ݭn�λ������~�ॴ�}[�q��]�C')
    
    DetectAndEditPost('[�լd][�j��]', \
    '���W���@�T�e�G' + '\r' +\
    'https://imgur.com/a/1EslXrB')
    
    DetectAndEditPost('[�K�X��][423]', \
    '�A���}�F[�O�I�c]�A�b�̭����F[�q����������]')
    
    DetectAndEditPost('[�q��][�q����������]', \
    '[�q��]�ù��X�{�F�o�ӵe���G' + '\r' +\
    'https://imgur.com/a/oTmyA19')
    
    DetectAndEditPost('[�q��][�L��]', \
    '�A�b[�q��]�̭����F�����_�l�C')
    
    DetectAndEditPost('[����][��U����]', \
    '�A��{�X������O�@�Ӿ����H�A�A�������_�l��U�F����[����]�C' + '\r' +\
    '�A�b����[����]�̭����F[�P�������_�l]�C')
    
    DetectAndEditPost('[�ۤv][�P�������_�l]', \
    '�A�^�Q�_�ۤv���]�O�@�Ӿ����H�A�A��[�P�������_�l]��U�F[�ۤv]��[����]�C' + '\r' +\
    '�A�b[�ۤv]��[����]�̭����F�K��C')
    
    DetectAndEditPost('[�j��][���}]', \
    '�A���K�񥴯}�F�j���A' + '\r' +\
    '���~�������H���ߧA�q�L�F���աC')
    
except Exception as e:
    print(e)
    PTTBot.Log('����ҥ~ �Ұʺ�����ܱ��I')

# �n�X
PTTBot.logout()
