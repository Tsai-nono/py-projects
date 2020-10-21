"""
File: similarity.py
----------------------------
This program compares short dna sequence, s2,
with sub sequences of a long dna sequence, s1
The way of approaching this task is the same as
what people are doing in the bio industry.
"""


def main():
    """
    Function:   Input the long_DNA chain and short_DNA sequence,
                and find the DNA sequence with the highest similarity.
    Principle:  align the short_DNA sequences one by one,
                compare the similarity of each segment in the long_DNA chain,
                and take the highest similarity value.
    """

    while True:
         long_sequence = input('Please give me a DNA sequence to search: ')
         if long_sequence.isalpha():
             break
         else:
            print('<Error: No words other than letters.>')

    while True:
         short_sequence = input('What DNA sequence would you like to match? ')
         if short_sequence.isalpha():
             break
         else:
            print('<Error: No words other than letters.>')

    if len(short_sequence) > len(long_sequence):
        print('<Error: Search is longer than sample.>')
    else:
        print('The best match is ' + similar_dna(long_sequence, short_sequence))


def similar_dna(long_sequence, short_sequence):
    '''
    Function: Import the long_DNA chain and short_DNA sequence, and find the DNA sequence with the highest similarity.
    :param long_sequence: str,long_DNA
    :param short_sequence: str,short_DNA
    :return: str,Export the DNA sequence with the highest similarity (similarity)
    '''

    data = long_sequence.upper()
    keyword = short_sequence.upper()
    keyword_len = len(keyword)
    similar_ans = ''
    max_same_value = 0

    for i in range(len(data)-keyword_len+1):
        dna_check = data[i: i+keyword_len]

        same_value = 0
        for j in range(keyword_len):
            if dna_check[j] == keyword[j]:
                same_value += 1

        if same_value > max_same_value:
            max_same_value = same_value
            similar_ans = dna_check

    return similar_ans + ' , (simlilar=' + str(max_same_value / keyword_len *100) + '%)'


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
