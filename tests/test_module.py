from dataclasses import dataclass
import pytest


@dataclass(frozen=True)
class Example:
    key: str
    curated_key: str
    keyless_matrix: str
    plain_text: str
    curated_plain_text: str
    encrypted_text: str
    decrypted_text: str


@pytest.fixture
def examples() -> list[Example]:
    return [
        Example(
            key="Radio",
            curated_key="RADIO",
            keyless_matrix="RADIOBCEFGHKLMNPQSTUVWXYZ",
            plain_text="Puesta",
            curated_plain_text="PUESTA",
            encrypted_text="QPLXQI",
            decrypted_text= "PUESTA"
        )
    ]

def test_curation(examples: list[Example]):
    from playfair.utils import curate

    for example in examples:
        assert curate(example.key) == example.curated_key
        assert curate(example.plain_text) == example.curated_plain_text


def test_general_keyless_matrix_generation(examples: list[Example]):
    from playfair.utils import keyless_matrix

    for example in examples:
        assert keyless_matrix(example.key) == example.keyless_matrix

def test_cipher_process(examples: list[Example]):
    from playfair.cipher import cipher

    for example in examples:
        assert cipher(example.key, example.plain_text) == example.encrypted_text


def test_decipher_process(examples: list[Example]):
    from playfair.decipher import decipher

    for example in examples:
        assert decipher(example.key, example.encrypted_text) == example.decrypted_text
