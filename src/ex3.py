def count_words(filename):
    small_words = []
    large_words = []

    with open(filename, "r") as file:
        words = file.read().split()
        for word in words:
            if len(word) < 3:
                small_words.append(word)
            else:
                large_words.append(word)

    with open("small-words.txt", "w") as small_file:
        small_file.write("\n".join(small_words))

    with open("large-words.txt", "w") as large_file:
        large_file.write("\n".join(large_words))

    unique_words = set(words)
    return len(unique_words)


def ex3():
    total_words = count_words("files/words.txt")
    print(f"Total words: {total_words}.")


ex3()
