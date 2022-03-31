from .utils import curate, fix_index, keyless_matrix


# cipher using playfair
def cipher(key: str, ptext: str) -> str:
    ctext = curate(ptext)
    matrix = keyless_matrix(key)
    etext = ""
    for ci in range(0, len(ctext) - 1, 2):
        i = matrix.index(ctext[ci])
        j = matrix.index(ctext[ci + 1])
        irow = i // 5
        icol = i % 5
        jrow = j // 5
        jcol = j % 5
        if abs(j - i) % 5 == 0:
            etext += (
                matrix[fix_index(i + 5, icol + 20, lambda r: icol)]
                + matrix[fix_index(j + 5, jcol + 20, lambda r: jcol)]
            )
        elif i // 5 == j // 5:
            etext += (
                matrix[fix_index(i + 1, irow * 5 + 4, lambda r: irow * 5)]
                + matrix[fix_index(j + 1, irow * 5 + 4, lambda r: jrow * 5)]
            )
        else:
            cipheri = jcol + irow * 5
            cipherj = icol + jrow * 5
            etext += matrix[cipheri] + matrix[cipherj]
    return etext
