**维吉尼亚密码破解**
____
####这一部分是实现维吉尼亚密码的几个函数
```py
import numpy


def find_key_len(cipher, n=26):  # 查找密钥长度的函数 n为密钥长度上限
	for i in range(1, n):  # 假定密钥长度在1，25位之间
		string_cipher = cipher
		ic = []  # 存储无偏估计值
		for j in range(0, i):
			string_copy = string_cipher[j::i]  # 本次查找的分组
			s_lenth = len(string_copy)
			ic_value = 0
			for k in range(0, 26):  # 计算IC无偏估计值
				alpha_count = string_copy.count(chr(k + 97))
				ic_value += (alpha_count * (alpha_count - 1)) / (s_lenth * (s_lenth - 1))
			ic.append(ic_value)
		print(f'密钥长度为{i:02d}时,对应的IC值为：', end=' ')
		for j in range(len(ic)):
			print(f'  {ic[j]:.3f}', end='')
		print(f'\n本组ic值的平均值为{numpy.mean(ic):.5f}, 本组ic值的方差为{numpy.var(ic):.5f}')

def ic_calculate(cipher, n):  # 计算重合指数 参数为密文和密钥长度
	probility = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067, 0.075,
	             0.019, 0.001, 0.06, 0.063, 0.091, 0.028, 0.01, 0.023, 0.001, 0.02, 0.001]
	possible_key_index = []
	for i in range(0, n):
		temp_cipher = cipher[i::n]
		m_lenth = len(temp_cipher)  # 每个分组的长度
		x = []  # 存储拟重合指数
		for j in range(0, 26):
			s = ''
			x_value = 0
			s = shift(temp_cipher, j)
			for ij in range(0, 26):  # 计算拟重合指数
				x_value += float(probility[ij]) * (float(s.count(chr(97 + ij))) / m_lenth)
			x.append(x_value)
		print('重合指数为：', end='')
		for j in range(len(x)):
			print(f'  {x[j]:.3f}', end='')
		max_index = x.index(max(x, key=abs))
		possible_key_index.append(max_index)
		print(f'\n最大值在列表中出现的位置为{max_index:02d}, 它的值为{x[max_index]:.3f}')  # 最大位置就是破解是应该进行移位的数目
	print(f'推荐使用的一组移位密钥为{possible_key_index}')


def cipher_break(cipher, *key):  # 输入密文和密钥进行破解 密钥的输入格式for example: 6，18，12,... 为重合指数最大值的出现位置
	key_len = len(key)
	print('破解的结果为： ')
	for i in range(len(cipher)):
		if ord(cipher[i]) + key[i % key_len] <= 122:
			print(chr(ord(cipher[i]) + key[i % key_len]), end='')
		else:
			print(chr(ord(cipher[i]) + key[i % key_len] - 26), end='')


def key_conversion(*key):  # 由key得到传统密钥几个字母
	l = len(key)
	print('\n使用字母加密的密钥为： ')
	for i in range(l):
		if key[i] == 0:
			print(f'{chr(123 - key[i] - 26)}', end='')
		else:
			print(f'{chr(123 - key[i])}', end='')


def alpha_copy(s):  # 只保留文本中的小写字母 如果是大写就变成小写
	re_s = ''
	for i in range(len(s)):
		if 97 <= ord(s[i]) <= 122:
			re_s += s[i]
		elif ord('A') <= ord(s[i]) <= ord('Z'):
			re_s += str(chr(ord(s[i]) + 32))
		else:
			continue
	return re_s

def is_alpha(char):  # 判断输入是不是字母
	if ord('A') <= ord(char) <= ord('Z') or ord('a') <= ord(char) <= ord('z'):
		return True
	else:
		return False


def shift(a_string, n):  # 参数为字符串和移动的位数
	str_len = len(a_string)
	s = ''
	for i in range(0, str_len):  # 先移位
		if (ord(a_string[i]) + n) <= 122:
			s += str(chr(ord(a_string[i]) + n))
		else:
			s += str(chr(ord(a_string[i]) + n - 26))
	return s
```

**************************************************************
####这一部分是一个使用实例
```py
from dcmm1 import vigenere_break_tools as vg



ciphertext1 = 'krkpekmcwxtvknugcmkxfwmgmjvpttuflihcumgxafsdajfupgzzmjlkyykxdvccyqiwdncebwhyjmgkazybtdfsitncwdnolqiacmchnhwcgxfzlwtxzlvgqecllhimbnudynagrttgiiycmvyyimjzqaxvkcgkgrawxupmjwqemiptzrtmqdciakjudnnuadfrimbbuvyaeqwshtpuyqhxvyaeffldmtvrjkpllsxtrlnvkiajfukycvgjgibubldppkfpmkkuplafslaqycaigushmqxcityrwukqdftkgrlstncudnnuzteqjrxyafshaqljsljfunhwiqtehncpkgxspkfvbstarlsgkxfibffldmerptrqlygxpfrwxtvbdgqkztmtfsqegumcfararhwerchvygczyzjaacgntgvfktmjvlpmkflpecjqtfdcclbncqwhycccbgeanyciclxncrwxofqieqmcshhdccughsxxvzdnhwtycmcbcrttvmurqlphxnwddkopqtehzapgpfrlkkkcpgadmgxdlrchvygczkerwxyfpawefsawukmefgkmpwqicnhwlnihvycsxckf'
ciphertext2 = 'cbkznkiyjsrofgnqadnzuqigscvxizgsjwucusrdkxuahgzrhywtvdjeiuwsrrtnpszbvpzncngztbvsrnzuqigscvfjwqgjwcytwdazuqigscvfjwqgjwjhkfdylmcbmhonbmbvdnvbmwbnacjaphhonbmbvdnvbmwbnaublsbdnjjneoroyfmxfhixpzpcozzuqigscvxcvhdmfgxmgovzsqmvzyvwyzmsczoajsejifoakdcrehwhgdehvmtnmvvmesvzifutzfjzoalwqztunwvdvmfhesvzifutzfjzoalwqztunpsnoyfleoxdetbwfsoyfjmfhjuxuagnarsfqydoyfjzsrzeujmfhjuubihrjdfinwsnepcawdnkbobvnmzucmghijjmbscjejnapddehlmqddmfxncqbfpxwfejifpqzhikiyaiozimubwuzufazsdjwdiudzmztivcmgp'
if __name__ == '__main__':
	#vg.find_key_len(ciphertext1)  # 尝试密钥长度 结果越接近0.065越可能   函数的第二个参数为尝试的密钥长度上限，默认取26
	#vg.find_key_len(ciphertext2)
	#vg.ic_calculate(ciphertext1, 5)  # 密文重合指数,7 是可能的密钥长度
	#vg.cipher_break(ciphertext1, 24, 9, 2, 11, 7)
	#vg.key_conversion(24, 9, 2, 11, 7)
	vg.ic_calculate(ciphertext2, 7)
	vg.cipher_break(ciphertext2, 6, 18, 12, 1, 5, 9, 25)
	vg.key_conversion(6, 18, 12, 1, 5, 9, 25)
```
**************************************
有关图形界面的代码放在**qt_vigenere.py**文件内
 
