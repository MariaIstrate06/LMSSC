from urllib.request import urlopen
import html2text
import re

# TASK 1: Scraping some websites to get text and
# store it into file 'corpus.txt'. implement a
# tokenizer which splits the corpus on whitespace
# and separate punctuation characters.


url = "https://ro.wikipedia.org/wiki/E-mail"
page = urlopen(url)

file = open("corpus.txt", 'w', encoding='utf-8')
word_file = open("words.txt", 'w', encoding='utf-8')

html_text = page.read()
html = html_text.decode("utf-8")
rendered_content = html2text.html2text(html)

# Rendering the content of the HTML page

file.write(rendered_content)
file.close()

corpus = open("corpus.txt", 'r', encoding='utf-8')
string = corpus.read()

words = string.split()

# getting rid of unnecessary tokens

count = 0
for i in words:
    count += 1
    if re.match('\[([^)]+)\]', i) or i == '*' or i == '**^**':
        pass
    else:
        if i[len(i) - 1] == '.':
            word_file.write(i[:len(i) - 1] + '\n' + '.' + '\n')
        else:
            word_file.write(i + '\n')
word_file.close()

single_tokens = {}

# Task 2: recognizing e-mail addresses and urls

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
url_regex = r"\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*" \
            r"\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"

single_token_dict = single_tokens.fromkeys(range(3), [])
word_file = open("words.txt", 'r', encoding='utf-8')
for line in word_file.readlines():
    if re.match(email_regex, line):
        single_token_dict[0].append(line)  # EMAIL
        print(f'Email: {line}')
    elif re.match(url_regex, line[line.find('https://'):]):
        single_token_dict[1].append(line[line.find('https://'):])  # URLS
        print(f'URL: {line[line.find("https://"):]}')

# TASK 3: getting rid of the splitting between
# addressing abbreviations and getting them
# to be recognized as a single token

task3_file = open("task3/input_task_3.txt", 'r', encoding='utf-8')
test3 = task3_file.read()
output3 = open("task3/output_task_3.txt", 'w', encoding='utf-8')

test3_words = test3.split()

for word in test3_words:
    if word == 'D-l' or word == 'D-na' or word == 'd-l' or word == 'd-na':
        output3.write(word + ' ')
    else:
        output3.write(word + '\n')

# TASK 4: Conceptually, splitting on white space can also split what should be regarded as a single token.
# This occurs most commonly with compound names (San Francisco, Los Angeles) but also with borrowed foreign
# phrases (a priori). ---------
#
# Other cases with internal spaces that we might wish to regard as a single token include
# phone numbers ((800) 234-2333. Other characters may also be considered for exceptions from splitting
# (in all cases?), such as for phone numbers: 0232 – 201090 or 0232/20-10-90 or 0232-20-10-90).
# Adjust your tokenizer to treat also these cases. ++++++++

task4_file = open("task4/input_task_4.txt", 'r', encoding='utf-8')
test4 = task4_file.read()
output4 = open("task4/output_task_4.txt", 'w', encoding='utf-8')

test4_words = test4.split()

phone_regex = r'\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$'
for word in test4_words:
    if re.match(phone_regex, word):
        print(word)
        output4.write(f'Phone number: {word}' + '\n')

# Task 5:
task5_file = open("task5/input_task_5.txt", 'r', encoding='utf-8')
test5 = task5_file.read()
output5 = open("task5/output_task_5.txt", 'w', encoding='utf-8')

test5_words = test5.split()

for word in test5_words:
    if word.find('-') != -1:
        if 'A' <= word.split('-')[0] <= 'Z' and 'A' <= word.split('-')[1] <= 'Z':
            output5.write(word + '\n')
        else:
            output5.write(word.split('-')[0] + '\n' + word.split('-')[1] + '\n')
    else:
        output5.write(word + '\n')

