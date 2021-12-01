import requests
import re
import csv
import matplotlib.pyplot as plt


def task1(text, save=False):
    """Parse https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references
    find all ftp links. Change flag save to True if you want to save a file with links"""
    pattern = r'ftp\.[^;\s]*'
    ftps = re.findall(pattern, text)
    if save:
        with open('ftps.csv', 'w') as f:
            links = csv.writer(f, delimiter=',')
            links.writerow(ftps)
    else:
        print(f'We found but not saved ftp links, we will return number of them: {len(ftps)}')


def task2(ad_240):
    """It finds all numbers from a story"""
    pattern = r'\d+'
    numbers_240 = re.findall(pattern, ad_240)
    return numbers_240


def task3(ad_240):
    """It finds all words with [Aa] letter (case insensitive)"""
    pattern = r'[a-zA-Z]*[aA]{1}[a-zA-Z]*'
    words_with_a = re.findall(pattern, ad_240)
    return words_with_a


def task4(ad_240):
    """Finds all sentences end with "!" """
    pattern = r'[A-Z]{1}[a-z\s]*!|"[A-Za-z\s]*!"'
    exclamations_sentences = re.findall(pattern, ad_240)
    return exclamations_sentences


def task5(ad_240):
    """Draws histogram for length of all unique words (numbers included)"""
    pattern = r"[a-zA-Z]+['.]\w+|[a-zA-Z]+|\d+"
    all_words = re.findall(pattern, ad_240)
    unique_words = []
    helper_set = set()
    words_length_distribution = {}
    for i in all_words:
        if i not in unique_words and i.lower() not in helper_set:
            unique_words.append(i)
            helper_set.add(i.lower())
            word_length = len(i)
            if not words_length_distribution.get(word_length):
                words_length_distribution[word_length] = 1
            else:
                words_length_distribution[word_length] += 1

    plt.bar(list(words_length_distribution.keys()), words_length_distribution.values(), color='black')
    plt.xlabel("number of letters")
    plt.ylabel("frequency in a text")
    plt.title('Words length distribution in a 2430 A.D. story')
    plt.show()
    return unique_words


def combine_text(ad_240, save_csv=False):
    if save_csv:
        with open('ad_240_numbers.csv', 'w') as text:
            processed_files = csv.writer(text, delimiter=',')
            processed_files.writerow(task2(ad_240))
        with open('ad_240_Aa.csv', 'w') as text:
            processed_files = csv.writer(text, delimiter=',')
            processed_files.writerow(task3(ad_240))
        with open('ad_240_excl.csv', 'w') as text:
            processed_files = csv.writer(text, delimiter=',', quotechar='|')
            processed_files.writerow(task4(ad_240))
        with open('ad_240_unique.csv', 'w') as text:
            processed_files = csv.writer(text, delimiter=',')
            processed_files.writerow(task5(ad_240))
    else:
        print('numbers: ')
        print(task2(ad_240))
        print('\n')
        print('words with A/a: ')
        print(task3(ad_240))
        print('\n')
        print('exclamations sentences: ')
        print(task4(ad_240))
        print('\n')
        print('unique words: ')
        print(task5(ad_240))


def main():
    text = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/references').text
    ad_240 = requests.get('https://raw.githubusercontent.com/Serfentum/bf_course/master/15.re/2430AD').text
    task1(text, save=False)
    print('\n2400 A.D. analysis: ')
    combine_text(ad_240, save_csv=False)


if __name__ == '__main__':
    main()
