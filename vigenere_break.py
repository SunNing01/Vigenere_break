from dcmm1 import vigenere_break_tools as vg

'''
在这里更改密文
对于不同的函数要记得更改参数
下方为两个密文实例
'''

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
