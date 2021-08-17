import getpass

class Geheim():
    def __init__(self, input, mode):
        self.input = input
        self.output = ''
        if mode == 'e':
            self.encode()
        elif mode == 'd':
            self.decode()
        print(self.output)
    def encode(self):
        key = getpass.getpass('Please enter the secret key: ')
        repeat = (len(self.input)//len(key))+1
        newkey = key * repeat
        codenums = [(ord(i)+ord(j)-len(key)) for i,j in zip(self.input, newkey)]
        self.output = ''.join(f'{i:08b}' for i in codenums)

    def decode(self):
        separated = [self.input[0 + i:8 + i] for i in range(0, len(self.input), 8)]
        codenums = [int(i,2) for i in separated]
        key = getpass.getpass('Please enter the secret key: ')
        keynums = [ord(i) for i in key]
        repeat = (len(codenums) // len(keynums)) + 1
        newkey = key * repeat
        #newkeynums = [ord(i) for i in newkey]
        textnums = [i+len(key)-ord(j) for i,j in zip(codenums, newkey)]
        self.output = ''.join(chr(i) for i in textnums)

if __name__ == '__main__':
    meintext = Geheim('Hallo! Treffpunkt: 18:00 Uhr im Park vor dem Rathaus.','e')

    klar = Geheim(meintext.output, 'd')

print(globals())
