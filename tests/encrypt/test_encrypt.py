from challenges.challenge_encrypt_message import encrypt_message
import pytest


invalid_type_input_message = 12345678
invalid_type_key = "wrong"
invalid_key = 9

input_message = "12345678"
input_decres = "87654321"
key_even = 3
key_odd = 4

output_even = "321_87654"
output_odd = "8765_4321"
output_inverted = "87654321"
output_crescent = "12345678"


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(invalid_type_input_message, invalid_type_key)

    assert encrypt_message(input_message, key_even) == output_even

    assert encrypt_message(input_message, key_odd) == output_odd

    assert encrypt_message(input_message, invalid_key) == output_inverted

    assert encrypt_message(input_decres, invalid_key) == output_crescent
