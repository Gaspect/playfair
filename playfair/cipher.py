from .utils import common


# cipher using playfair
def cipher(key: str, ptext: str) -> str:
    matrix, indexes = common(key, ptext)
    etext = ""
    for i, irow, icol, j, jrow, jcol in indexes:
        if abs(j - i) % 5 == 0:
            etext+=(
                matrix[i + 5 if i + 5 <= icol + 20 else icol]
                + matrix[j + 5  if j + 5 <= jcol +20 else jcol]
            )
        elif i // 5 == j // 5:
            etext += (
                matrix[i+1 if i+1 <= irow*5+4 else irow*5]
                + matrix[j+1 if j+1 <= jrow*5+4 else jrow*5]
            )
        else:
            cipheri = jcol + irow * 5
            cipherj = icol + jrow * 5
            etext += matrix[cipheri] + matrix[cipherj]
    return etext
