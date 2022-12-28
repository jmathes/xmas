#!/usr/bin/env python
import click
import random
from pprint import pprint
import json

with open("locations.json", "rb") as json_file:
    LOCATIONS = json.load(json_file)

for location in LOCATIONS:
    location["clue"] = location["clue"].replace(" ", "_")

MSG_LEN = max(len(location["clue"]) for location in LOCATIONS)
SEP = "_"
ALPHABET = "".join(chr(n) for n in range(ord("a"), ord("a")+26)) + SEP

def c2n(c: str) -> int:
    assert c in ALPHABET
    if c == SEP:
        return 26
    return ord(c) - ord("a")

def n2c(n: int) -> str:
    assert 0 <= n <= 26
    c = SEP if n == 26 else chr(n + ord("a"))
    assert c in ALPHABET
    return c

def encode_char(c1: str, c2: str) -> str:
    assert len(c1) == 1
    assert len(c2) == 1
    return "".join([
        n2c((c2n(c1) - c2n(c2)) % 27)
    ])

def decode_char(c1: str, c2: str) -> str:
    assert len(c1) == 1
    assert len(c2) == 1
    return "".join([
        n2c((c2n(c1) + c2n(c2)) % 27)
    ])

@click.group()
def cli():
    pass

@cli.command()
@click.argument("msg")
@click.argument("key")
def encode(msg: str, key: str) -> None:
    print(encode_(msg, key))

def encode_(msg: str, key: str) -> str:
    assert len(key) == MSG_LEN
    assert len(msg) <= MSG_LEN
    msg = msg + SEP * (MSG_LEN - len(msg))
    encrypted = "".join(encode_char(c1, c2) for c1, c2 in zip(msg, key))
    return f"{msg} + {key} = {encrypted}"


@cli.command()
@click.argument("encrypted")
@click.argument("key")
def decode(encrypted: str, key: str) -> None:
    print(decode_(encrypted, key))

def decode_(encrypted: str, key: str) -> str:
    assert len(key) == MSG_LEN
    assert len(encrypted) <= MSG_LEN
    decrypted = "".join(decode_char(c1, c2) for c1, c2 in zip(encrypted, key))
    return f"{encrypted} - {key} = {decrypted}"


@cli.command()
def get_key() -> None:
    print(_get_key())

def _get_key() -> str:
    return "".join(random.choice(ALPHABET) for _ in range(MSG_LEN))

"""
First key:

   🔒rdspavnaajq_tlm
 + 🔑abcdefghijklmno
 ___________________
 = 🔍reuse_this_key_
"""


if __name__ == "__main__":
    cli()
