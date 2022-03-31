from .utils import common

def decipher(key: str, ectext: str) -> str:
    matrix, indexes = common(key, ectext)
    etext = ""
    for i, irow, icol, j, jrow, jcol in indexes:
        if abs(j - i) % 5 == 0:
            etext += (
                matrix[i-5 if i-5 >= 0 else 20 + icol]  
                + matrix[j-5 if j-5 >= 0 else 20 + jcol]
            )
             
        elif i // 5 == j // 5:
            etext += (
                    matrix[i-1 if (i-1) // 5 == irow else irow * 5 + 4]
                    + matrix[j-1 if (j-1) // 5 == jrow else jrow * 5 + 4]
                )
        else:
            cipheri = jcol + irow * 5
            cipherj = icol + jrow * 5
            etext += matrix[cipheri] + matrix[cipherj]
    return etext
