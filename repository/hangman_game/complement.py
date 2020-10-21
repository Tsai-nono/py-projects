"""
File: complement.py
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    Function: Input DNA sequence, output corresponding DNA sequence.
    Principle: Compare the input DNA sequence one by one, corresponding to the DNA element.
    """

    dna_1 = input("Please give me a DNA strand and I'll find the complement: ").upper()
    print('The complement of ' + dna_1.upper() + ' is ' + build_complement(dna_1))


def build_complement(dna):
    '''
    Function: Import DNA sequence, output corresponding DNA sequence.
    :param dna: str, input DNA sequence.
    :return: str, output the corresponding DNA sequence.
    '''

    new_dna = ''
    for base in dna:
        if base == 'A':
            new_dna += 'T'
        elif base == 'C':
            new_dna += 'G'
        elif base == 'T':
            new_dna += 'A'
        elif base == 'G':
            new_dna += 'C'
    return new_dna


###### DO NOT EDIT CODE BELOW THIS LINE ######
if __name__ == '__main__':
    main()
