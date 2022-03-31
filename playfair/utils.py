# curate a string based on  the playfair cipher
from typing import Callable, Optional, Pro

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


# fix a index based on the max
def fix_index(
    index: int, max: int, rest_handler: Optional[Callable[[int], int]] = None
) -> int:
    if index > max:
        value = index % max
        return rest_handler(value) if rest_handler else value
    return index
