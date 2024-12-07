def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print("\nWord Count:")
        print("-------------")
        print("Total Words:", wordcounter(file_contents))
        print("\nCharacter Frequency:")
        print("-----------------------")
        char_freq = char_frequency(file_contents)
        print("Character\tFrequency")
        for char, freq in char_freq.items():
            print(f"{char}\t{freq}")

def wordcounter(text):
    wordstotal = text.split()
    words = 0
    for word in wordstotal:
        words += 1
    return words

def char_frequency(text):
    frequency_dict = {}
    for char in text.lower():
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

main()