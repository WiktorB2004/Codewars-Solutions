import re
def revrot(str, sz):
    if sz <= 0 or len(str) == 0 or sz > len(str):
        return ''
    chunks = re.findall(f'{"."*sz}', str)
    res = []
    for chunk in chunks:
        chunk_sum = sum([int(char) for char in chunk])
        if (chunk_sum ** 2) % 2 == 0:
            res.append(chunk[::-1])
        else:
            res.append(chunk[1:] + chunk[0])     
    return ''.join(res)