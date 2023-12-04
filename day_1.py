def calculate_value(string):
    digits = ''.join(s for s in string if s.isdigit())
    value = digits[0] + digits[-1]
    return int(value)


def replace_first_word(string, word_dict):
    for i in range(len(string)):
        if string[i].isdigit():  # if a digit is present before a word is found - no need to replace
            return string

        for key in word_dict.keys():
            if string.startswith(key, i):  # returns first index of found word
                string = string.replace(key, word_dict[key], 1) # replace first occurrence only
                return string
    return string


def replace_last_word(string, word_dict):
    for i in range(len(string) - 1, -1, -1):  # loop from last index to first
        for key in word_dict.keys():
            if string.startswith(key, i):
                string = string.replace(key, word_dict[key])
                return string
    return string


digits_dict = {'one': '1',
               'two': '2',
               'three': '3',
               'four': '4',
               'five': '5',
               'six': '6',
               'seven': '7',
               'eight': '8',
               'nine': '9'}

print("Enter/Paste your content:")
contents = []

while True:
    line = input()
    if line == 'end':
        break
    contents.append(line)

contents = [replace_first_word(content, digits_dict) for content in contents]
contents = [replace_last_word(content, digits_dict) for content in contents]

values = [calculate_value(content) for content in contents]
print(sum(values))
