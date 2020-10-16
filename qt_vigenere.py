from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
import numpy
from dcmm1.vigenere_break_tools import shift, alpha_copy, is_alpha


class VigeneBreakTool():
	def __init__(self):
		# 应用框
		self.window = QMainWindow()
		self.window.resize(670, 570)
		self.window.move(450, 310)
		self.window.setWindowTitle('维吉尼亚密码破译 by sn')
		#  文本框
		self.textEdit0 = QPlainTextEdit(self.window)
		self.textEdit0.setPlaceholderText('请输入密文')
		self.textEdit0.move(10, 10)
		self.textEdit0.resize(300, 250)

		self.textEdit1 = QPlainTextEdit(self.window)
		self.textEdit1.setPlaceholderText('请输入密钥长度')
		self.textEdit1.move(330, 10)
		self.textEdit1.resize(300, 50)

		self.textEdit2 = QPlainTextEdit(self.window)
		self.textEdit2.setPlaceholderText('请输入密钥')
		self.textEdit2.move(330, 100)
		self.textEdit2.resize(300, 50)

		self.textEdit3 = QPlainTextEdit(self.window)
		self.textEdit3.setPlaceholderText('解密得到的明文为')
		self.textEdit3.move(10, 280)
		self.textEdit3.resize(300, 250)

		self.button0 = QPushButton('测试密钥长度', self.window)
		self.button0.move(400, 170)

		self.button1 = QPushButton('输出可能的密钥', self.window)
		self.button1.move(400, 220)

		self.button2 = QPushButton('解密', self.window)
		self.button2.move(400, 270)

		self.button0.clicked.connect(self.output_key_len)
		self.button1.clicked.connect(self.output_possible_key)
		self.button2.clicked.connect(self.output_plaintext)

	#  密钥长度分析
	def output_key_len(self):
		cipher_origin = self.textEdit0.toPlainText()
		cipher = alpha_copy(cipher_origin)
		if not cipher:
			QMessageBox.warning(self.window, 'Warning!', '请输入密文！')
		else:
			for i in range(1, 26):  # 假定密钥长度在1，25位之间
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
				QMessageBox.about(self.window, '懒得写了,接近0.065最好       ', f'''密钥长度为{i:02d}时
ic值的平均值为{numpy.mean(ic):.3f}, 
i方差为{numpy.var(ic):.5f}''')

	#  重合指数判断移位密钥
	def output_possible_key(self):
		ekey_len = self.textEdit1.toPlainText()
		cipher_origin = self.textEdit0.toPlainText()
		cipher = alpha_copy(cipher_origin)
		alpha_key = ''
		if ekey_len.isdecimal() and cipher:
			n = int(ekey_len)
			probility = [0.082, 0.015, 0.028, 0.043, 0.127, 0.022, 0.02, 0.061, 0.07, 0.002, 0.008, 0.04, 0.024, 0.067,
			             0.075,
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
			# print(f'\n最大值在列表中出现的位置为{max_index:02d}, 它的值为{x[max_index]:.3f}')  # 最大位置就是破解是应该进行移位的数目
			for _ in range(len(possible_key_index)):
				if possible_key_index[_] == 0:
					alpha_key += str(chr(123 - possible_key_index[i] - 26))
				else:
					alpha_key += str(chr(123 - possible_key_index[_]))
			QMessageBox.about(self.window, '密钥推荐', f'推荐使用的一组移位密钥为{alpha_key}')
		else:
			QMessageBox.warning(self.window, 'Warning!', '''请合法输入密文
或密钥长度！''')

	def output_plaintext(self):
		cipher_origin = self.textEdit0.toPlainText()
		key = self.textEdit2.toPlainText()
		plaintext = ''
		key_place = 0
		if cipher_origin and key:
			key_len = len(key)
			for i in range(len(cipher_origin)):
				if is_alpha(cipher_origin[i]):
					if ord(cipher_origin[i]) - ord(key[key_place%key_len]) + 97 >= 97:
						plaintext += str(chr(ord(cipher_origin[i]) - ord(key[key_place%key_len]) + 97))
					elif ord(cipher_origin[i]) - ord(key[key_place%key_len]) + 97 < 97:
						plaintext += str(chr(ord(cipher_origin[i]) - ord(key[key_place%key_len]) + 97+26))
					key_place += 1
			self.textEdit3.setPlainText(f'明文为：{plaintext}')
		else:
			QMessageBox.warning(self.window, 'Warining！', '''请合法输入密文或密钥!''')

if __name__ == '__main__':

	app = QApplication([])
	vigene_break_tool = VigeneBreakTool()
	vigene_break_tool.window.show()
	app.exec_()
