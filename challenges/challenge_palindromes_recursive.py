def is_palindrome_recursive(word, low_index, high_index):
    if word == "":
        return False

    while low_index <= high_index:
        if word[low_index] == word[high_index]:
            low_index += 1
            high_index -= 1
            is_palindrome_recursive(word, low_index, high_index)
        else:
            return False
    return True
