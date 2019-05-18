import random


class Decoder:
    def __init__(self, length=128, mode=None):
        self.mode = mode
        self.length = length
        if mode is None:
            self._random_mode()

    def _random_mode(self):
        tmp = [i for i in range(self.length)]
        self.mode = random.sample(tmp, len(tmp))

    def decode(self, cipher):
        tmp = {}
        for i, c in zip(self.mode, cipher):
            tmp[i] = c

        plain = ''
        for i in sorted(tmp.keys()):
            plain = plain + tmp[i]

        return plain


if __name__ == '__main__':
    decoder = Decoder(5)
    print(decoder.mode)
    plain = decoder.decode('abcde')
    print(plain)
