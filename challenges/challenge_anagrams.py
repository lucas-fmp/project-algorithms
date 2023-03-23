# O algoritmo de ordenação Merge Sort utilizado foi baseado no
# utilizado no conteúdo da Trybe sobre Algoritmos de ordenação


def merge(letters_list, start, mid, end):
    left = letters_list[start:mid]
    right = letters_list[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            letters_list[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            letters_list[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            letters_list[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            letters_list[general_index] = right[right_index]
            right_index = right_index + 1


def merge_sort(letters_list, start=0, end=None):
    if end is None:
        end = len(letters_list)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(letters_list, start, mid)
        merge_sort(letters_list, mid, end)
        merge(letters_list, start, mid, end)


def is_anagram(first_string, second_string):
    first_string_list = list(first_string.lower())
    second_string_list = list(second_string.lower())

    merge_sort(first_string_list)
    merge_sort(second_string_list)

    first_string = "".join(first_string_list)
    second_string = "".join(second_string_list)

    if first_string == second_string and first_string != "":
        return (first_string, second_string, True)

    return (first_string, second_string, False)
