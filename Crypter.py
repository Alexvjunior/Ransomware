def change_files(filename, cryptorFn, block_size=16):
    with open(filename, 'r+b') as _file:
        raw = _file.read(block_size)
        while raw:
            cipher = cryptorFn(raw)

            if len(raw) != len(cipher):
                raise ValueError(f'O valor cifrado {len(cipher)} tem tamanho diferente do valor plano {len(raw)}')

            _file.seek(- len(raw), 1)
            _file.write(cipher)
            raw = _file.read(block_size)