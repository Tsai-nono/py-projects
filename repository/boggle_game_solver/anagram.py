"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
from boggle_dictionary import Dictionary_Dict

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    formal()


def formal():
    # 讀字典(obj)
    diction = read_dictionary(FILE)

    while True:
        print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
        keyword = input('Find anagrams for:')

        if keyword == EXIT:
            break
        else:
            # 主要程式區
            word_list = find_anagrams(keyword, diction)
            print(f'{len(word_list)} anagrams:  {word_list}')
            # 參照區


def read_dictionary(file):
    """
    This function reads file "dictionary.txt" stored in FILE
    and appends words in each line into a Python list
    :return: (obj)
    """
    # 呼叫Dictionary程式
    diction = Dictionary_Dict(file)
    # 讀取:字典並匯入到dict_map
    diction.diction_dict()
    return diction


def find_anagrams(s, diction):
    """

    :param s:
    :param diction:
    :return:
    """
    ans = []
    permutation(s, '', len(s), ans, diction)
    return ans


def permutation(lst, txt_str, txt_len, ans_list, diction):
    # TODO: 要重寫字串組合的部分，因為會遇到重複字無法排序的問題

    if txt_len == len(txt_str):
        if has_word(txt_str, diction) and txt_str not in ans_list:
            print('Searching')
            print(f'Found:  {txt_str}')
            ans_list.append(txt_str)
        return ans_list
    else:

        for i in range(len(lst)):
            #
            lst_l = lst[:i]
            lst_r = lst[i+1:]
            lst_ele = lst[i]

            # pop
            txt_str += lst_ele
            lst = lst_l + lst_r

            #
            if has_prefix(txt_str, diction):
                permutation(lst, txt_str, txt_len, ans_list, diction)

            # reset pop
            lst = lst_l + lst_ele + lst_r
            txt_str = txt_str[:-1]


def has_word(sub_s, diction):
    """

    :param sub_s:
    :param diction:
    :return:
    """
    if diction.lookup_dict_diciton(sub_s) == 2:
        return True
    else:
        return False


def has_prefix(sub_s, diction):
    """
    :param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
    :return: (bool) If there is any words with prefix stored in sub_s
    """

    if diction.lookup_dict_diciton(sub_s) <= 2:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
