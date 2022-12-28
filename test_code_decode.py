from code_decode import ALPHABET, c2n, n2c, encode_char, decode_char, encode_, decode_


def describe_code_decode():
    def describe_alphabet():
        def has_everything():
            for char in "abcdefghijklmnopqrstuvwxyz_":
                assert char in ALPHABET

        def has_nothing_extra():
            assert 27 == len(ALPHABET)

    def describe_c2n():
        def gives_numbers():
            for char in ALPHABET:
                assert isinstance(c2n(char), int)

        def answers_are_unique():
            assert len(set(map(c2n, ALPHABET))) == len(ALPHABET)

        def reversible():
            for char in ALPHABET:
                assert char == n2c(c2n(char))

    def describe_n2c():
        def gives_chars():
            for n in range(27):
                assert isinstance(n2c(n), str)

        def answers_are_unique():
            assert len(set(map(n2c, range(27)))) == 27

        def reversible():
            for n in range(27):
                assert n == c2n(n2c(n))

    def encode_and_decode():
        for c1 in ALPHABET:
            for c2 in ALPHABET:
                assert c1 == decode_char(encode_char(c1, c2), c2)