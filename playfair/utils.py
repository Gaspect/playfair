# curate a string based on  the playfair cipher
from typing import Iterator, Tuple

# curate a string based in requirements of playfar cipher
def curate(item: str) -> str:
    item = item.upper()
    item = item.strip()
    item = item.replace("Ñ", "")
    item = item.replace("J", "I")
    for i in range(0, len(item) - 1, 2):
        if item[i] == item[i + 1]:
            item = item[: i + 1] + "X" + item[i + 1 :]
    return item


# build a keyless generic matrix
def keyless_matrix(key: str) -> str:
    key = curate(key) + "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = ""
    for ch in key:
        if ch not in matrix:
            matrix += ch
    return matrix

def common(key:str, text:str) -> Tuple[str, Iterator[Tuple[int, int, int, int, int, int]]]:
    ctext = curate(text)
    matrix = keyless_matrix(key)
    
    def iterator() -> Iterator[Tuple[int, int, int, int, int, int]]:
        for ci in range(0, len(ctext) - 1, 2):
            i = matrix.index(ctext[ci])
            j = matrix.index(ctext[ci + 1])
            irow = i // 5
            icol = i % 5
            jrow = j // 5
            jcol = j % 5
            yield i, irow, icol, j, jrow, jcol
    
    return matrix, iterator()