from challenges.challenge_encrypt_message import encrypt_message
import pytest


valid_input_message = "12345678"
invalid_type_input_message = 12345678
key_even = 3
key_odd = 4
invalid_key = 9
invalid_type_key = "wrong"

output_even = "321_87654"
output_odd = "8765_4321"
output_inverted = "87654321"


def test_encrypt_message():
    with pytest.raises(TypeError):
        encrypt_message(invalid_type_input_message, invalid_type_key)

    assert encrypt_message(valid_input_message, key_even) == output_even

    assert encrypt_message(valid_input_message, key_odd) == output_odd

    assert encrypt_message(valid_input_message, invalid_key) == output_inverted
