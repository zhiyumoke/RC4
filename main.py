import numpy as np
import input_init as ii
import re


class RC4:
    def __init__(self):
        # define Variables
        self.plain_length = 0
        self.plain = []
        self.S = np.empty(shape=256, dtype=int)
        self.T = np.empty(shape=256, dtype=int)
        self.cipher = np.empty(shape=256, dtype=int)
        self.stream = []

        plain_str = list(input("请输入明文,最多32个字符："))
        for i in plain_str:
            if ord(i) < 128:  # ASCII表内的数据
                ch_ascii = '{:08b}'.format(ord(i))
                for j in ch_ascii:
                    if j == '0':
                        self.plain.append(0)
                    elif j == '1':
                        self.plain.append(1)
                    else:
                        print("error")
                self.plain_length += 8

            else:  # 即中文字符
                b_stream = ''
                i_by = bytes(i, encoding="utf-8")
                for i_bin in i_by:
                    i_b = bin(i_bin).replace('0b', '')
                    b_stream += i_b
                for j in b_stream:
                    if j == '0':
                        self.plain.append(0)
                    elif j == '1':
                        self.plain.append(1)
                    else:
                        print("error")
                self.plain_length += 24
        if 256 - len(plain_str):
            tem_str = []
            for i in range(256 - len(plain_str)):
                tem_str.append(0)
            self.plain = self.plain + tem_str
            self.plain = np.array(self.plain)
        else:
            print("Wrong Length!")

    def ksa(self):
        key_len, key = ii.str_con()
        if key_len == 256:
            self.T = key
        elif 0 < key_len < 255:
            for i in range(256):
                self.S[i] = i
                self.T[i] = key[i % key_len]
        else:
            print("error")
        j = 0
        for i in range(256):
            j = (j + self.S[i] + self.T[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]

    def prga(self):
        i = 0
        j = 0
        for m in range(32):
            i = (i + 1) % 256
            j = (j + self.S[i]) % 256
            self.S[i], self.S[j] = self.S[j], self.S[i]
            t = (self.S[i] + self.S[j]) % 256
            k = self.S[t]
            tem_stream = ii.key_stream(k)
            self.stream = self.stream + tem_stream
        self.stream = np.array(self.stream)
        print("密钥流")
        for i in range(64):
            ii.two2chr(self.stream[i * 4:(i + 1) * 4])
        print(end="\n")

    def encode(self):
        self.ksa()
        self.prga()
        for i in range(256):
            self.cipher[i] = self.stream[i] ^ self.plain[i]
        print("密文")
        for i in range(int(self.plain_length / 4)):
            ii.two2chr(self.cipher[i * 4:(i + 1) * 4])
        print(end="\n")

    def decode(self):
        new_plain_bit = np.empty(self.plain_length, dtype=int)
        new_plain = ''
        for i in range(self.plain_length):
            new_plain_bit[i] = self.cipher[i] ^ self.stream[i]
        for i in range(self.plain_length):
            if new_plain_bit[i] == 0:
                new_plain = new_plain + '0'
            elif new_plain_bit[i] == 1:
                new_plain = new_plain + '1'
            else:
                print("Error")
        plain_list = re.findall(r'.{8}', new_plain)
        nums = ''
        for ch in plain_list:
            nums += (hex(int(ch, 2)).replace('0x', ''))
        plain = bytes.fromhex(nums)
        print('解密结果：', str(plain, 'utf-8'))


crypto = RC4()
crypto.encode()
crypto.decode()
