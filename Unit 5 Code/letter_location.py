def letter_locations(string, key):
    index = 0
    length = len(string)
    locations = ""
    while index < length:
        if string[index] == key:
            locations += str(index)
        index += 1
    return locations


def main():
    string = "abcababdef"
    key = "a"
    locations = letter_locations(string, key)
    locations = ", ".join(locations)
    print(list_locations)
    print(f"The letter {key} is located at indices {locations}.")


main()
