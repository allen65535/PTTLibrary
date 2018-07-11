# -*- coding: big5 -*-
import sys
import time
import json
import getpass
import codecs
from PTTLibrary import PTT
from PTTLibrary import Big5uao

# �������媺3�ӿﶵ�ýs��峹���禡
def DetectAndEditPost(TrueAnswer, Choice1, Answer1, Choice2, Answer2, Choice3, Answer3, Choice4, Answer4, Choice5, Answer5, Choice6, Answer6, Choice7, Answer7):
	Check = 0
	
	#���P�@�q��r�u�|�X�{�@��
	AlreadyShow1 = 0
	AlreadyShow2 = 0
	AlreadyShow3 = 0
	AlreadyShow4 = 0
	AlreadyShow5 = 0
	AlreadyShow6 = 0
	AlreadyShow7 = 0
	
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
			if Choice1 in Push.getContent():
				if AlreadyShow1 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer1
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow1 = 1
					
					if TrueAnswer == 1:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice2 in Push.getContent():
				if AlreadyShow2 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer2
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow2 = 1
					
					if TrueAnswer == 2:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice3 in Push.getContent():
				if AlreadyShow3 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer3
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow3 = 1
					
					if TrueAnswer == 3:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice4 in Push.getContent():
				if AlreadyShow4 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer4
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow4 = 1
					
					if TrueAnswer == 4:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice5 in Push.getContent():
				if AlreadyShow5 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer5
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow5 = 1
					
					if TrueAnswer == 5:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice6 in Push.getContent():
				if AlreadyShow6 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer6
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow6 = 1
					
					if TrueAnswer == 6:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
					break # ���}for�j��
			
			elif Choice7 in Push.getContent():
				if AlreadyShow7 == 0:
					print(Push.getAuthor() + ':' + Push.getContent())
					CorrectMsg = Push.getAuthor() + '�ϥΤF���O' + Push.getContent().replace('[���O]', '') + '\r' + '\r' + \
					Answer7
					PTTBot.editArticle(CorrectMsg) # �s��峹
					AlreadyShow7 = 1
					
					if TrueAnswer == 7:
						Check = 1 # 1��ܵ���A2��ܵ���
					else: Check = 2
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
	Board = 'TurtleSoup'  # �ݪO
	PostIndex = 27375  # �峹���X
	PTTBot.gotoBoard(Board)
	PTTBot.gotoArticle(PostIndex)
	
	PTTBot.push(Board, PTT.PushType.Arrow, '�C���}�l�I', PostIndex=PostIndex)
	
	# �D�n�C�����e
	
	# �߰ݨt��1
	Option1 = '[��1�y][�߰�]'
	Result1 = \
	'[��1�y] �ڦۤv�]�����۫H�����H�|���H�����A' + '\r' + \
	'���B��G(���)�����H�O���̶}�o�X�Ӫ��A���i������ۤv���D�H�O�H' + '\r' + \
	'�t���G�i�O�ڤp�ɭԴN���g�Q�ڦۤv�i�����r�L�ڡC' + '\r' + \
	'�Ȥ��G�ڤp�ɭԤ]�Q�ڦۤv�i���D�r�L�C' + '\r' + \
	'�u�d�G���B��A���O�A�ðݰ��D�A�ڭ̪��B�ҧ󤣧Q�F�աC'
	Option2 = '[��2�y][�߰�]'
	Result2 = \
	'[��2�y] �ӥB�ڭ̶e�����o�Ӿ����H�K�K���o���Z�i�R�����C >///<' + '\r' + \
	'���B��G�o�Ӿ����H�K�K�O�k���ܡH' + '\r' + \
	'�Ȥ��G�����H���|���ʧO�A�߮v�Ф��n�쩵�ɶ��C' + '\r' + \
	'�k�x�G�P�N�C�߮v�Ф��n�쩵�ɶ��C' + '\r' + \
	'���B��G�i�c�A�ڵ��@�U�n�ۤv�ݾ����H�K�K'
	Option3 = '[��3�y][�߰�]'
	Result3 = \
	'[��3�y] ���O�����H�רs�O�����H�A���]���׵��̤@�ˡA�O�|���H���A' + '\r' + \
	'���B��G�]���׵��̤w�g�O�ܤ[�H�e���q�v�F�A���o�ӨҤl�n�ܡH' + '\r' + \
	'�t���G�u�nGoogle�N�d�o��F�ڡA���B��A�n�h�ǵ��I�ڡC' + '\r' + \
	'�u�d�G���B��A�A�����٨S�Ѩ줣�|��Google�a�A�A�n�h�ǵ��I�ڡC' + '\r' + \
	'���B��G�O�|���|��Google�����D�ܡK�K'
	Option4 = '[��4�y][�߰�]'
	Result4 = \
	'[��4�y] �����H�ä����ڭ̤H�����D�w�[���M�P�������C' + '\r' + \
	'���B��G(���)������A�i�H�_�w�����H�S���D�w�[���M�P���O�H' + '\r' + \
	'�t���G���K�K�o�ӹ��K�K�o���D���I���K�K' + '\r' + \
	'�Ȥ��G�n�l�s�o�Ӱ��D���ܡA�i�H�Ы߮v���w�q�D�w�[���M�P���ܡH' + '\r' + \
	'���B��G(���M�n�ڦۤv�w�q�A��A���K�K)'
	Option5 = '[��5�y][�߰�]'
	Result5 = \
	'[��5�y] �ҥH�@���ץ�̤j�����åǡA�٬O�D�e�������H���i�C' + '\r' + \
	'���B��G����������H�|�O�̤j�����åǩO�H' + '\r' + \
	'�t���G�]�����̩M�����H��ӤH�P�~���A�S����L���äH�o�C' + '\r' + \
	'�u�d�G���B��A�p�G�A�������ܡA�̤j�����åǷ|�O�ڶܡH' + '\r' + \
	'���B��G���n�����ؤ��N�Q���ܡK�K(�ӥB�ڸ�p�S�S���P�~)'
	Option6 = '[�Ҫ�][����]'
	Result6 = \
	'�o���Ҫ��G[����]' + '\r' + \
	'�����H�ߦ^�Ӫ��զ�p�ߡA�����H���e���W��[����]�C' + '\r' + \
	'https://imgur.com/a/JzZhpUq'
	Option7 = '[��4�y][����]'
	Result7 = \
	'���B��G(���)�p�G�����H�O�S���P�����A���L���|�ߤp�ߦ^�a�O�H' + '\r' + \
	'�t���G�o�ӡK�K���u�O�ε{�������H�����P���Ӥw�C' + '\r' + \
	'���B��G�N��O�������A���u�n�����H��ӵ۳o�˪��W�h��ʡA' + '\r' + \
	'�@�@�@�@���N��O�u���I���O�ܡH' + '\r' + \
	'�k�x�G���T�C�ڱq�ӨS���ߤp�ߦ^�a�i�L�A�o�����H�����w����٦��R�ߩO�C' + '\r' + \
	'�u�d�G���B��A�k�x�{�P�F�A���o�n�I' + '\r' + \
	'�Ȥ��G�k�x�j�H�A�����H�쩳���S���P���o�بƱ��A�ä��O���ת����I�C' + '\r' + \
	'�k�x�G�A�Q������H' + '\r' + \
	'�Ȥ��G�ڤ��Q�Q�׾����H�����ߥ@�ɡC�t��ĵ�x�A�ЧA�N�{�����p�@�ҧa�C' + '\r' + \
	'�k�x�G�t��ĵ�x�A�Ч@�ҡC' + '\r' + \
	'�t���G�ڪ��D�F�C' + '\r' + \
	'' + '\r' + \
	'�m�ҡn�m���n�m�}�n�m�l�n' + '\r' + \
	'(�I�����֡G https://youtu.be/hf_D3pK6LVI )' + '\r' + \
	'' + '\r' + \
	'[��6�y] �׵o�{���b���̪��a�̪����A' + '\r' + \
	'[��7�y] �ӥB���̪��a�̴N�u�����̩M�����H��ӤH�����C' + '\r' + \
	'[��8�y] ���̮a���j���O��۪��A�S���Q�~�O�J�I������A' + '\r' + \
	'[��9�y] �{���ݰ_�Ӥ]�S������������C' + '\r' + \
	'[��10�y] �ҥH�غظ�H����ܡA�{���S���O�����H�F�C' + '\r' + \
	'' + '\r' + \
	'�k�x�G���B��߮v�A�ж}�l�߰ݡC'
	DetectAndEditPost(7, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �߰ݨt��2
	Option1 = '[��6�y][�߰�]'
	Result1 = \
	'[��6�y] �׵o�{���b���̪��a�̪����A' + '\r' + \
	'���B��G����S���Q���ʹL���i��ʶܡH' + '\r' + \
	'�t���G�q���M�ʹ��N�ݱo�X�ӡA����S���Q���ʹL��C' + '\r' + \
	'�Ȥ��G�Ф��n�p�ݧڭ̪��k��MŲ�ѤH���n�ܡH' + '\r' + \
	'���B��G�ڥu�O�H�f�ݰݦӤw�K�K'
	Option2 = '[��7�y][�߰�]'
	Result2 = \
	'[��7�y] �ӥB���̪��a�̴N�u�����̩M�����H��ӤH�����C' + '\r' + \
	'���B��G(���)���̪��a�������N�٦��@���p�ߡI' + '\r' + \
	'�Ȥ��G���D�߮v�Q�D�i����O�����p�߶ܡH' + '\r' + \
	'�u�d�G���B��A�p�߬O�L�d���I' + '\r' + \
	'���B��G�ڪ��D�աA�p���n�⮱�Y���o�����C'
	Option3 = '[��8�y][�߰�]'
	Result3 = \
	'[��8�y] ���̮a���j���O��۪��A�S���Q�~�O�J�I������A' + '\r' + \
	'���B��G���⦳�S���i��O�p���O�H�ζ}��u��J�I�������C' + '\r' + \
	'�Ȥ��G���̮a�������q���޳N�����A�Aı�o�H�H�K�K�N�i�H�J�I�ܡH' + '\r' + \
	'���B��G��K�K�����w���̭�n�ѰO����K�K' + '\r' + \
	'�Ȥ��G�ܿ�ѡA����o��ƬO�����H�t�d���A�Aı�o�L�|�ѰO�ܡH'
	Option4 = '[��9�y][�߰�]'
	Result4 = \
	'[��9�y] �{���ݰ_�Ӥ]�S������������C' + '\r' + \
	'���B��G���̪��a�ݰ_�ӨS���ܾ���ڡC' + '\r' + \
	'�u�d�G���B��A���O�L�̮a�w�g��ڭ̪��k�ߨưȩ��پ���F�K�K' + '\r' + \
	'���B��G�٤��O�p�ݧ�DVD���å�C' + '\r' + \
	'�k�x�G�y�I�Ф��n��a�ȨƱa��k�x�W�n�ܡC'
	Option5 = '[��10�y][�߰�]'
	Result5 = \
	'[��10�y] �ҥH�غظ�H����ܡA�{���S���O�����H�F�C' + '\r' + \
	'���B��G(���)�ҥH�{�������H�ƥءK�K�O�X�H�H' + '\r' + \
	'�Ȥ��G�߮v����p�ƾǦѮv�`�а��ܡH' + '\r' + \
	'�u�d�G���B��A�A���ƾǤ���ٮt�A�o�ˤ����C' + '\r' + \
	'�t���G�b���̦��`���e�A���H�N�u��1�H�����C'
	Option6 = '[��10�y][�{���Ӥ�]'
	Result6 = \
	'���B��G(���)�k�x�j�H�A�Ьݲ{���Ӥ��C�аݷӤ������X���ī~�O�H' + '\r' + \
	'�k�x�G��3�ءA�p�ߪ��ĸ�H���Ĥ��@�ˡC���L�A�ܻ������H�]���ۤv���ġH' + '\r' + \
	'���B��G�����ӬO�O�i�����Ϊ��ƾ��ľ��a�C' + '\r' + \
	'�@�@�@�@�k�x�j�H�A�A�аݷӤ������X���U�l�O�H' + '\r' + \
	'�k�x�G��2���A�����H�j���ȼ��A�ҥH���ۤv���U�l�C' + '\r' + \
	'�Ȥ��G�߮v�A�쩳�Q������H' + '\r' + \
	'���B��G�k�x�j�H�A�ڦA�ݳ̫�@�Ӱ��D�C�аݷӤ������X�ӪM�l�O�H' + '\r' + \
	'�k�x�G��2�ӪM�l�K�K�x�H' + '\r' + \
	'���B��G�k�x�j�H�]�`�N��F�a�C�p�ߤ]�\�ݭn�Y�ġA�����H�]�\�ݭn�U�l�A' + '\r' + \
	'�@�@�@�@���p�ߩM�����H�O���i��ϥΪM�l�ܤ����a�I' + '\r' + \
	'�@�@�@�@��2�ӪM�l���s�b�A��ܲ{���i�঳��2�Ӭ��H�I' + '\r' + \
	'�Ȥ��G��K�K���i��K�K' + '\r' + \
	'���B��G�k�x�j�H�A�ڭn�D�����H��{���s�b����2�ӤH�@�ҡC' + '\r' + \
	'�k�x�G�P�N�C�ǳ�����H�W�ҤH�u�A��{���s�b����2�ӤH�@�ҡC' + '\r' + \
	'' + '\r' + \
	'�m�ҡn�m���n�m�}�n�m�l�n' + '\r' + \
	'(�I�����֡G https://youtu.be/hf_D3pK6LVI )' + '\r' + \
	'' + '\r' + \
	'[��11�y] ���n�@���s�ھ����H�A�ڦ��W�r��C' + '\r' + \
	'[��12�y] �ڪ��W�r�s�p�R�A�ܥi�R���W�r�a�I <3' + '\r' + \
	'[��13�y] �Ӥ@�D�H���������@�ѡA�S����L�H�ӧڭ̮a�O�C' + '\r' + \
	'[��14�y] �β�2�ӪM�l�ܤ����A�O�߫}��C' + '\r' + \
	'[��15�y] ���K���@�U�A�Ӥ@�D�H���Ѭ�M�����F�A�n�_�ǳ�C' + '\r' + \
	'' + '\r' + \
	'�k�x�G���B��߮v�A�ж}�l�߰ݡC'
	Option7 = '\�����H/'
	Result7 = '\�����H/'
	DetectAndEditPost(6, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �߰ݤp�R
	Option1 = '[��11�y][�߰�]'
	Result1 = \
	'[��11�y] ���n�@���s�ھ����H�A�ڦ��W�r��C' + '\r' + \
	'���B��G�W�r�A�O�֨����O�H' + '\r' + \
	'�p�R�G�O�Ӥ@�D�H���ڨ�����C' + '\r' + \
	'���B��G�Ӥ@�O�K�K��F�A�O���̪��W�r�C' + '\r' + \
	'�Ȥ��G�߮v�A���M�s���̪��W�r���ѤF�ܡI'
	Option2 = '[��12�y][�߰�]'
	Result2 = \
	'[��12�y] �ڪ��W�r�s�p�R�A�ܥi�R���W�r�a�I <3' + '\r' + \
	'���B��G�p�R�K�K�]���OAI�A�ҥH�s���p�R�ܡH' + '\r' + \
	'�p�R�G�j���O�a�C�ϥ��i�R�N�n�A�ڤ��Ӧb�N�O�C' + '\r' + \
	'���B��G�ڷQ�ݫܤ[�F�A�p�R�A�O�k���ܡH' + '\r' + \
	'�p�R�G�Q���աA�H�a����i�R�A�A���|�h�äH�a�աI'
	Option3 = '[��13�y][�߰�]'
	Result3 = \
	'[��13�y] �Ӥ@�D�H���������@�ѡA�S����L�H�ӧڭ̮a�O�C' + '\r' + \
	'���B��G�A�u���S���O���ܡH' + '\r' + \
	'�Ȥ��G�߮v�A�h�þ����H���O�жܡH' + '\r' + \
	'�k�x�G��ı�o�����H���O�СA���Ӥ�H���n100���a�C' + '\r' + \
	'�p�R�G�Q���աA�H�a����i�R�A�A���|�h�äH�a�աI'
	Option4 = '[��14�y][�߰�]'
	Result4 = \
	'[��14�y] �β�2�ӪM�l�ܤ����A�O�߫}��C' + '\r' + \
	'�k�x�G�߮v�I�Q�i��������A�������@�ˡH' + '\r' + \
	'���B��G(���)�p�R�A�߫}���i��ΪM�l�ܤ��O�H' + '\r' + \
	'�p�R�G������߫}����ΪM�l�ܤ��O�H�D�H�S���Чڳo�ӻ��C' + '\r' + \
	'���B��G(�o�̤@�w�����D�A���{�b�٤����D����}�o�Ӫ��I�K�K)'
	Option5 = '[��15�y][�߰�]'
	Result5 = \
	'[��15�y] ���K���@�U�A�Ӥ@�D�H���Ѭ�M�����F�A�n�_�ǳ�C' + '\r' + \
	'���B��G��M�����A�O�]���s���Ӥ@�����F�A�A��������L���ͩR��H�ܡH' + '\r' + \
	'�p�R�G���K�ӡK�O�K�a�A���O�S�K��K���A�i�O�K�K' + '\r' + \
	'���B��G�O�@�����N�����F�ܡH' + '\r' + \
	'�p�R�G�S���A�@�����N��M�����F�A�o�ڥi�H�D�`�֩w�C'
	Option6 = '[��15�y][��ͳ��i]'
	Result6 = \
	'���B��G(���)�p�R�A�A�D�i�s���Ӥ@�@�����N��M���`�F��ܡH' + '\r' + \
	'�p�R�G�S���ڡC' + '\r' + \
	'���B��G���O�ھ���ͳ��i�һ����A�s���Ӥ@�O�ä�@�q�ɶ���~���`����C' + '\r' + \
	'�p�R�G���K����I' + '\r' + \
	'�k�x�G�߮v�A�o�O���^�ơH���D�p�R�|�����ܡH' + '\r' + \
	'���B��G�ڤ�ı�o�p�R�|�����A���O�j���o�ͤF�p�R�L�k���޿�P�_���ƹ�A' + '\r' + \
	'�@�@�@�@�ҥH�L�ۤv�]ı�o�ܥ٬ޡC' + '\r' + \
	'�k�x�G��K�K���ӫ���O�H' + '\r' + \
	'�Ȥ��G�k�x�j�H�A�е��ڤ@�I�ɶ��A���ڶǳ�U�@���ҤH�C' + '\r' + \
	'���B��G(�{�b�~�n�h���ҤH�ܡH)' + '\r' + \
	'�k�x�G��x�@�Ӥp�ɡA�˹�x�л��֧��ҤH�a�ӡI' + '\r' + \
	'' + '\r' + \
	'�@�@�@�@�@�@���@�@�@�@�@�@���@�@�@�@�@�@��' + '\r' + \
	'' + '\r' + \
	'�Ȥ��G�k�x�j�H�A�ҤH�w�g�a�ӤF�C' + '\r' + \
	'�k�x�G�ҤH�A�л��X�A���m�W�M¾�~�C' + '\r' + \
	'�Ǥ��G�ڥs���Ǥ��s��A�O�s���Ӥ@���P�ơC' + '\r' + \
	'�@�@�@�ڥi�H�վ\�p�R����x�ɮץX�Ӭd�ݡA��M�L�I�쪺�޿���~�C' + '\r' + \
	'�k�x�G�Ӧn�F�A�Ч@�ҧa�C' + '\r' + \
	'' + '\r' + \
	'�m�ҡn�m���n�m�}�n�m�l�n' + '\r' + \
	'(�I�����֡G https://youtu.be/hf_D3pK6LVI )' + '\r' + \
	'' + '\r' + \
	'[��16�y] ��x�ɧڤw�g�ݹL�F�p�R����x�ɮסC' + '\r' + \
	'[��17�y] �p�R���{���B�@�ܥ��`�A�S���o���޿���~�C' + '\r' + \
	'[��18�y] �ҥH�s���Ӥ@�֩w�O�o�ͤF����ơA��M�����F�C' + '\r' + \
	'[��19�y] �ڤ]�����D�O���^�ơC' + '\r' + \
	'[��20�y] �J�M�ڨӧ@�ҤF�A�ڴN���K���@�U�A��ı�o�������ӬO�p�R�S���C' + '\r' + \
	'' + '\r' + \
	'���B��G(���)�ҤH�I�S���H�ݧAı�o����O�֡I' + '\r' + \
	'�Ǥ��G��p��p�A�̫�@�y�O�h�l���A��ڨS���n�F�C' + '\r' + \
	'�k�x�G���B��߮v�A�A�n�߰ݶܡH' + '\r' + \
	'���B��G���A�ڤ��θ߰ݡA���ڷQ�n�K�K' + '\r' + \
	'' + '\r' + \
	'�п�J��ܡG' + '\r' + \
	'[1][�n�D���Ѥ�x�ɮ�]' + '\r' + \
	'[2][�n�D���ѫ���Ӥ�]' + '\r' + \
	'[3][�n�D���ѪM�l�Ӥ�]'
	Option7 = '\�a�F/'
	Result7 = '\�a�F/'
	DetectAndEditPost(6, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �n�D�����Ҿ�
	Option1 = '[1][�n�D���Ѥ�x�ɮ�]'
	Result1 = \
	'���B��G�k�x�A�ڧƱ��ˤ责�Ѥp�R����x�ɮסC' + '\r' + \
	'�Ȥ��G�A�n��x�ɮסH���تF�褣�O�M�~�H�h���ܡA�ݤ������աC' + '\r' + \
	'���B��G���M�ɧڬݤ@���N�n�C(���Y�ݤ�x�ɮ�)�u���ݤ����K�K' + '\r' + \
	'�u�d�G���B��A�O���L�A�ڭ̤]���ڭ̪��M�~�A�N�O���Q�i�G�@�I' + '\r' + \
	'�k�x��A���������C�F�C'
	Option2 = '[3][�n�D���ѪM�l�Ӥ�]'
	Result2 = \
	'���B��G�k�x�A�ڧƱ��ˤ责�ѪM�l���Ӥ��C' + '\r' + \
	'�Ȥ��G�u�O�d�����߮v�b�Q����C���h�I' + '\r' + \
	'' + '\r' + \
	'�o���Ҫ��G[�M�l�Ӥ�]' + '\r' + \
	'https://imgur.com/a/ZcfIBMT' + '\r' + \
	'' + '\r' + \
	'�u�d�G���B��A���ݥX����u���ܡH' + '\r' + \
	'���B��G��A�o�ӪM�l�K�K�Z�n�ݪ��K�K' + '\r' + \
	'�k�x��A���������C�F�C'
	Option3 = '[2][�n�D���ѫ���Ӥ�]'
	Result3 = \
	'���B��G�k�x�A�ڧƱ��ˤ责�ѲM���@�I������Ӥ��C' + '\r' + \
	'�Ȥ��G�n���骺�Ӥ��O�ܡH�b�o�̡C' + '\r' + \
	'' + '\r' + \
	'�o���Ҫ��G[����Ӥ�]' + '\r' + \
	'https://imgur.com/a/KIOMJ9z' + '\r' + \
	'' + '\r' + \
	'�k�x�G�߮v�A���骺�Ӥ��W������ȱo�`�N���F��ܡH' + '\r' + \
	'���B��G�ڲש�o�{�ѨM���ת�����F�I�ȱo�`�N���F��N�O�G' + '\r' + \
	'' + '\r' + \
	'�п�J��ܡG' + '\r' + \
	'[1][���]' + '\r' + \
	'[2][�M�l����m]' + '\r' + \
	'[3][�ߦզ�]'
	Option4 = '\����/'
	Result4 = '\����/'
	Option5 = '\���J�O/'
	Result5 = '\���J�O/'
	Option6 = '\�p�R/'
	Result6 = '\�p�R/'
	Option7 = '\AI/'
	Result7 = '\AI/'
	DetectAndEditPost(3, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �������
	Option1 = '[1][���]'
	Result1 = \
	'�k�x�G�����F�ܡH' + '\r' + \
	'���B��G��K�K�N�O���ӡK�K���ӥ��`�K�K' + '\r' + \
	'�k�x�G�O���̤����`�A�ګ��ݤ��X�ӡH' + '\r' + \
	'���B��G�ڡK�K�����K�K' + '\r' + \
	'�k�x��A���������C�F�C'
	Option2 = '[2][�M�l����m]'
	Result2 = \
	'�k�x�G�M�l����m���F�ܡH' + '\r' + \
	'���B��G��K�K�N�O���ӡK�K���ӥ��`�K�K' + '\r' + \
	'�k�x�G�O���̤����`�A�ګ��ݤ��X�ӡH' + '\r' + \
	'���B��G�ڡK�K�����K�K' + '\r' + \
	'�k�x��A���������C�F�C'
	Option3 = '[3][�ߦզ�]'
	Result3 = \
	'���B��G���ת�����A�N�O�o�@��ߦզ��I' + '\r' + \
	'�Ȥ��G�߮v�A�A�ש�o�ƤF�ܡH' + '\r' + \
	'���B��G�ڬO�{�u���C�ڤw�g���D���������������u�ۤF�I' + '\r' + \
	'(�I�����֡G https://youtu.be/wq1jknZp0ic )' + '\r' + \
	'�k�x�G�߮v�A�A���D�i�O�H' + '\r' + \
	'' + '\r' + \
	'�п�J��ܡG' + '\r' + \
	'[1][�����ܦ��F��]' + '\r' + \
	'[2][���̨��O��]' + '\r' + \
	'[3][���̬O�H�]�O��]'
	Option4 = '\�����H�p�R/'
	Result4 = '\�����H�p�R/'
	Option5 = '\AI�����H/'
	Result5 = '\AI�����H/'
	Option6 = '\�f��/'
	Result6 = '\�f��/'
	Option7 = '\�f������H/'
	Result7 = '\�f������H/'
	DetectAndEditPost(3, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# ��ܥ��׸�ߪ����Y
	Option1 = '[2][���̨��O��]'
	Result1 = \
	'���B��G���̨��O�ߡI' + '\r' + \
	'�Ȥ��G�߮v�A�A�G�M�o�ƤF�a�H' + '\r' + \
	'�k�x�G�߮v�A��ı�o����C' + '\r' + \
	'�k�x��A���������C�F�C'
	Option2 = '[3][���̬O�H�]�O��]'
	Result2 = \
	'���B��G���̬O�H�]�O�ߡI' + '\r' + \
	'�Ȥ��G�߮v�A�A�G�M�o�ƤF�a�H' + '\r' + \
	'�k�x�G�߮v�A��ı�o����C' + '\r' + \
	'�k�x��A���������C�F�C'
	Option3 = '[1][�����ܦ��F��]'
	Result3 = \
	'���B��G�����ܦ��F�ߡI' + '\r' + \
	'�Ȥ��G�߮v�A�A�G�M�o�ƤF�a�H' + '\r' + \
	'���B��G(���)�ڪ��N��O�A�������W�F�ߦզ�����A' + '\r' + \
	'�@�@�@�@�b�p�R�������A�L�N�ܦ��F�ߡI' + '\r' + \
	'�k�x�G���M����������A���߮v�o�ˤ@���A�Nı�o�n���D�z�I' + '\r' + \
	'���B��G���AI�ӻ��A�n���Ѳ{�ꪺ�v���A�O�@��ܧx�����ơC' + '\r' + \
	'�@�@�@�@�@�Ӹ˧ꦨ�ߪ��H���A�bAI�����A�ܦ��i��|�Q�{�w���ߡC' + '\r' + \
	'�@�@�@�@�o�˴N�i�H�������̬O��������������C' + '\r' + \
	'�@�@�@�@��L���W�F�ߦզ��A�����H�����Ӥ@�N���������F�C' + '\r' + \
	'�p�R�G�S���I�N�O�o�ˡI�D�H�ܦ��ߡA�D�H�����F�C' + '\r' + \
	'�@�@�@�p�R�����D�n���y�z�o��ơC' + '\r' + \
	'�Ȥ��G�N��i�H���������������������D�A���S���ˡH' + '\r' + \
	'�@�@�@���åǤ��M�u�������H�Ӥw��C' + '\r' + \
	'���B��G���C�˲M�F�o��ơA�N��ܡK�K' + '\r' + \
	'' + '\r' + \
	'�п�J��ܡG' + '\r' + \
	'[1][���̬O�۱���]' + '\r' + \
	'[2][�p�R�H���L�����O��]' + '\r' + \
	'[3][����]�O��]'
	Option4 = '\123456/'
	Result4 = '\123456/'
	Option5 = '\�Q���X�ӤF/'
	Result5 = '\�Q���X�ӤF/'
	Option6 = '\�n����/'
	Result6 = '\�n����/'
	Option7 = '\�n�q����/'
	Result7 = '\�n�q����/'
	DetectAndEditPost(3, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �ץ󪺯u��
	Option1 = '[1][���̬O�۱���]'
	Result1 = \
	'���B��G���̨��O�۱����C' + '\r' + \
	'�Ȥ��G�A�q���̱o�쪺�o�ӵ��סH' + '\r' + \
	'���B��G�N�O���ӡA��K�K' + '\r' + \
	'�k�x�G�߮v�A��ı�o����C' + '\r' + \
	'�k�x��A���������C�F�C'
	Option2 = '[2][�p�R�H���L�����O��]'
	Result2 = \
	'���B��G�p�R�H���L�����O�ߡC' + '\r' + \
	'�u�d�G���B��I�p�R�~���|���ߩO�I' + '\r' + \
	'���B��G�u�r�A���o�]�O�O�K�K' + '\r' + \
	'�k�x�G�߮v�A��ı�o�A�y�L�ۦ��F�C' + '\r' + \
	'�k�x��A���������C�F�C'
	Option3 = '[3][����]�O��]'
	Result3 = \
	'���B��G�p�G����]�˧ꦨ�F�ߡA���N��ѵ���~�ҵo�{����ӺðݤF�C' + '\r' + \
	'�k�x�G�иԲӻ����C' + '\r' + \
	'���B��G�����A����p�R�@�һ��S����L�H�o��ơC' + '\r' + \
	'�@�@�@�@��ꤣ�O�S����L�H�A�u�O���ӤH�˧ꦨ�ߡA' + '\r' + \
	'�@�@�@�@��p�R�ӻ��L�N����H�F�C' + '\r' + \
	'�k�x�G��Ӧp���C' + '\r' + \
	'���B��G�A�ӡA�p�R�@�һ��ߥΪM�l�ܤ��A�]�i�H�o������C' + '\r' + \
	'�@�@�@�@�ΪM�l�ܤ����A���O�˧ꦨ�F�ߪ��H�C' + '\r' + \
	'�k�x�G��A�n���ܦX�z�C' + '\r' + \
	'�Ǥ��G�k�x�j�H�A�߮v�һ����O���i�઺�A�����ڧ@�ҡC' + '\r' + \
	'���B��G�K�K(�L�Q������H)' + '\r' + \
	'�k�x�G�M�~�H�h���ܷQ���ܡH���N�ЧA�@�ҡC' + '\r' + \
	'' + '\r' + \
	'�m�ҡn�m���n�m�}�n�m�l�n' + '\r' + \
	'(�I�����֡G https://youtu.be/bp3RaRI_sQA )' + '\r' + \
	'' + '\r' + \
	'[��21�y] �Ф��n�p�ݤF�ڭ̤��q���v�����ѧ޳N�C' + '\r' + \
	'[��22�y] �p�R���M�u�O�@�Ӽ˥������H�A���L���v�����ѧ޳N�O�̷s���C' + '\r' + \
	'[��23�y] ���ѤH���M�߫}�A�o�ذ��D�ڭ̦��N�J�A�F�C' + '\r' + \
	'[��24�y] ���M������O���ꦨ�ߪ��H�H�ӥi���F�A' + '\r' + \
	'[��25�y] �A���p������O�����p�տߧa�C' + '\r' + \
	'' + '\r' + \
	'�k�x�G���B��߮v�A�ж}�l�߰ݡC' + '\r' + \
	'���B��G(�o�ӤH�]�\�N�O����A���گ���L���}��ܡH)'
	Option4 = '\����٦�/'
	Result4 = '\����٦�/'
	Option5 = '\����٦������H/'
	Result5 = '\����٦������H/'
	Option6 = '\�ڰڰ�/'
	Result6 = '\�ڰڰ�/'
	Option7 = '\����/'
	Result7 = '\����/'
	DetectAndEditPost(3, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �߰ݦǤ�
	Option1 = '[��21�y][�߰�]'
	Result1 = \
	'[��21�y] �Ф��n�p�ݤF�ڭ̤��q���v�����ѧ޳N�C' + '\r' + \
	'���B��G�A�̥Ϊ��v�����ѧ޳N�A�O�ۤv�}�o���ܡH' + '\r' + \
	'�Ǥ��G�N�O�ڥ��H�}�o����C��M�A�s���Ӥ@�]�����@�I���աC' + '\r' + \
	'�u�d�G���B��A�A�̦b�����O�Y�ح����ܡH' + '\r' + \
	'���B��G�c�K���O��C(�O���Q�쭹�����ڡK�K)'
	Option2 = '[��22�y][�߰�]'
	Result2 = \
	'[��22�y] �p�R���M�u�O�@�Ӽ˥������H�A���L���v�����ѧ޳N�O�̷s���C' + '\r' + \
	'���B��G�A����O�ҬO�̷s���O�H' + '\r' + \
	'�Ǥ��G�A���M��çڪ��M�~�I�A���D�ڬO���ӾǮղ��~���ܡH' + '\r' + \
	'�u�d�G���B��A�f�P����[�F�A�ڨ{�l�j�F�C' + '\r' + \
	'���B��G�p�ԭ@�@�U�A�ֵ����F��C(�p�G�گ���L���}�쪺�ܡK�K)'
	Option3 = '[��23�y][�߰�]'
	Result3 = \
	'[��23�y] ���ѤH���M�߫}�A�o�ذ��D�ڭ̦��N�J�A�F�C' + '\r' + \
	'���B��G�ҥH�A�̯u������s�L�����ѤH���M�߫}�ܡH' + '\r' + \
	'�Ǥ��G�ڭ̷�M��ڴ��չL�A�ҥH�s���Ӥ@�~�|�����ӿߦզ��C' + '\r' + \
	'���B��G(�}�o���٭n�ۤv�ꦨ�߫}�ڡA�u�O���W�F�C)' + '\r' + \
	'�u�d�G���D�B�D��A�ڡD�n�D�j�I'
	Option4 = '[��24�y][�߰�]'
	Result4 = \
	'[��24�y] ���M������O���ꦨ�ߪ��H�H�ӥi���F�A' + '\r' + \
	'���B��G���A�u�O�b�ؤj�ۤv���q���~���ʯ�Ӥw�a�H' + '\r' + \
	'�Ǥ��G�A���M��çڪ��M�~�I�A���D�ڬO���ӾǮղ��~���ܡH' + '\r' + \
	'�p�R�G�߮v���͡A�A���O�b�����G�@�ܡH�s�A�����۫H�ڶܡK�K' + '\r' + \
	'���B��G(�ڥu���۫H�A�S�����H�Ӥw�ڡK�K)'
	Option5 = '[��25�y][�߰�]'
	Result5 = \
	'[��25�y] �A���p������O�����p�տߧa�C' + '\r' + \
	'���B��G�p�տߡH�A�O������ܡH' + '\r' + \
	'�Ǥ��G�ߪ��W�r�ڤ����D�A�ڤS�S���h�L�s���Ӥ@���a�C' + '\r' + \
	'���B��G�S���h�L���̮a�ڡA�u�@���ݭn�h�L�a�ܡH' + '\r' + \
	'�Ǥ��G�ݭn���ɭԡA�s���Ӥ@�|��p�R�a�Ӥ��q�C�ڤ��ݭn�h�L�a�C'
	Option6 = '[��25�y][�{���Ӥ�]'
	Result6 = \
	'���B��G(���)�Ǥ����͡A�A���A�S���h�L���̪��a�H' + '\r' + \
	'�Ǥ��G�S���C' + '\r' + \
	'���B��G�A�]�����D�ߪ��W�r�H' + '\r' + \
	'�Ǥ��G�S���ڡA���S���ˡH' + '\r' + \
	'���B��G���аݡA�A�O��򪾹D�߫}�O�զ⪺�O�H' + '\r' + \
	'�Ǥ��G�o�K�K�c�K�K��F�A�O�s���Ӥ@�i�D�ڪ��I' + '\r' + \
	'���B��G�O�o�˶ܡH��F�A���M��ı�o�A�b�����A���o��Ƥ����n�C' + '\r' + \
	'�Ǥ��G�x�H�����n�ܡH' + '\r' + \
	'���B��G�ڭn�����A���ꦨ�߫}�A�즺�̪��a�����`�F���̡I' + '\r' + \
	'�@�@�@�@�]���A�O���̪��P�ơA�u�n���˷Q�ݤp�R�A���̴N�|���A�i���C' + '\r' + \
	'�@�@�@�@�J�M�w�g��X�A������i��ʤF�A���n���Ҿڤ]��²��C' + '\r' + \
	'�Ǥ��G�A�K�K�A�������Ҿڻ��ڱ��H�H' + '\r' + \
	'���B��G�p�R�]���A�˧ꦨ�ߡA�ҥH����A���H�A' + '\r' + \
	'�@�@�@�@���O�L���U���v���A���Ӧ�����A���ˤl�a�H' + '\r' + \
	'�Ǥ��G�����I�p�R���w�ЪŶ������A�ҥH�S���x�s�v����Ƴ�I' + '\r' + \
	'���B��G����I���K�K���K�K' + '\r' + \
	'' + '\r' + \
	'�п�J��ܡG' + '\r' + \
	'[1][�ҾڬO�p�R����x�ɮ�]' + '\r' + \
	'[2][�ҾڬO�p�R���������]' + '\r' + \
	'[3][�ҾڬO���G�M�W������]'
	Option7 = '\�֯}���F/'
	Result7 = '\�֯}���F/'
	DetectAndEditPost(6, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	# �̫᪺���
	Option1 = '[1][�ҾڬO�p�R����x�ɮ�]'
	Result1 = \
	'���B��G�ҾڴN�O�p�R����x�ɮסI' + '\r' + \
	'�Ȥ��G�߮v���O�ʤ��n�ܡH�N����x�ɮץu���M�~�H�h�ݱo���F�C' + '\r' + \
	'�u�d�G�ӥB�ߤ@�ݱo����x�ɮת��H�A�N�O���䪺������ͳ�C' + '\r' + \
	'���B��G�藍�_�A�ڿ��F�K�K' + '\r' + \
	'�k�x��A���������C�F�C'
	Option2 = '[3][�ҾڬO���G�M�W������]'
	Result2 = \
	'���B��G�ҾڴN�O���G�M�W�������I' + '\r' + \
	'�k�x�G�Ȥ��˹�x�A���G�M�W�������ܡH' + '\r' + \
	'�Ȥ��G�S����A�����ܧڦ��N���F�a�C' + '\r' + \
	'�u�d�G����ꦨ�߫}�ɡA��]���K���W��M�ܦ��ߴx�F�a�A' + '\r' + \
	'�@�@�@�ҥH�S�������C' + '\r' + \
	'�k�x��A���������C�F�C'
	Option3 = '[2][�ҾڬO�p�R���������]'
	Result3 = \
	'���B��G�ҾڴN�O�p�R��������ơI' + '\r' + \
	'�@�@�@�@�N��S���x�s�v����ơA�������`�Ӧ��a�H' + '\r' + \
	'�@�@�@�@�u�nťť�ݮ׵o�e�������ɡA�N���D�A���S���h���̮a�F�I' + '\r' + \
	'�Ǥ��G�A�K�K�A�K�K�o�K�K�i�c�I�I�I' + '\r' + \
	'�k�x�G�kĵ�I���ֶe���ҤH�I���n���L�]�F�I' + '\r' + \
	'' + '\r' + \
	'�@�@�@�@�@�@���@�@�@�@�@�@���@�@�@�@�@�@��' + '\r' + \
	'' + '\r' + \
	'(�I�����֡G https://youtu.be/tyqAgewtlT0 )' + '\r' + \
	'�k�x�G�kĵ�w�g���e���Ǥ��s��F�C' + '\r' + \
	'�Ȥ��G�w�g�T�{�L�����H�������ɮפF�A���T������Ǥ����n���C' + '\r' + \
	'�@�@�@�Ǥ��]�w�g�Z�ӡA���H�ʾ��O���F�ܨ��}�o�����H���\�ҩM�v�Q�C' + '\r' + \
	'�k�x�G�ݨӥi�H��Q�i�U�F�ŧP�F�O�C' + '\r' + \
	'' + '\r' + \
	'�@�@�@�@�L�@�@�@�@�o' + '\r' + \
	'' + '\r' + \
	'�k�x�G�ڲש󦨬��F�Ĥ@���������H�L�o���k�x�C' + '\r' + \
	'���B��G�ڬO�Ĥ@���������H�L�o���߮v�O�C' + '\r' + \
	'�u�d�G�ڬO�Ĥ@���������H�L�o���߮v�U��I' + '\r' + \
	'�Ȥ��G�A�K�K�A�̡K�K�i�c�I�I�I(�\�b)' + '\r' + \
	'�p�R�G�߮v���͡A�D�`�P�§A������o�F�L�o�P�M�C' + '\r' + \
	'�u�d�G���B��A�i�H���p�R�ӧڭ̫߮v�ưȩҤu�@�ܡH' + '\r' + \
	'���B��G�H�a�����q�S�S���˳��A�p�R�٬O�L�̤��q���]���r�C' + '\r' + \
	'�u�d�G���ܤ����ڦ��d����I' + '\r' + \
	'����G�p~~~' + '\r' + \
	'' + '\r' + \
	'�@�@�@�@�f������H' + '\r' + \
	'�@�@�@�@�X�X�p�R�M���󳣳̥i�R�F' + '\r' + \
	'' + '\r' + \
	'�@�@�@�@��'
	Option4 = '\�}���F/'
	Result4 = '\�}���F/'
	Option5 = '\�ֵ����F/'
	Result5 = '\�ֵ����F/'
	Option6 = '\����/'
	Result6 = '\����/'
	Option7 = '\�x��/'
	Result7 = '\�x��/'
	DetectAndEditPost(3, Option1, Result1, Option2, Result2, Option3, Result3, Option4, Result4, Option5, Result5, Option6, Result6, Option7, Result7)
	
	
except Exception as e:
	print(e)
	PTTBot.Log('����ҥ~ �Ұʺ�����ܱ��I')

# �n�X
PTTBot.logout()
