# Importing Library
import re
import sys
import pandas as pd

# UserName
name = input('What is your name?\n')
print(f'Welcome {name}!!!')

# Functions (Making repetitive processes shorter)
def arr_list(options):
    for index, option in enumerate(options):
        print(f'{index + 1}. {option.title().center(4)}')

def error(choice):
    success = False
    while True:
        try:
            #choice = input('Please make a choice. Integer values only')
            choice = int(choice)
            if choice is int:
                success = True
        except ValueError:
            while choice.isdecimal() == False:
                choice = input('Numbers only\n')
            choice = int(choice)
            if choice.isdecimal() == True:
                success = True
        except Exception:
            print('Please retry')
        if success == True:
            break
        return choice

def txt_pro(pre_text):
    lower_text = pre_text.lower()
    rem_punc_text = re.sub(r'[^\w\s]', '', lower_text)
    text = re.sub(r'[^\x00-\x7F]', '', rem_punc_text)
    return text

def str2list(txt):
    text_list = txt.split()
    return text_list

# MILESTONE 1 (INPUT SYSTEM)
# Input Options
src_opt = ['Enter manually', 'Read from file', 'exit']
arr_list(src_opt)

# Validating User's Choice
opt = input('Please make a choice. Integer values only\n')
opt = error(opt)
# try:
#     opt = input('How would you like to provide text\n')
#     opt = int(opt)
# except ValueError:
#     while opt.isdecimal() == False:
#         print('Invalid choice')
#         opt = input('Please input numerical values\n')
#     opt = int(opt)

# Actions Based On User's Choice
if opt == 1:
        text = input('Please input text\n')
        #Cleaning Text
        clean_text = re.sub(r'\s+', ' ', text).strip()
elif opt == 2:
    while True:
        try:
            text = input('Please enter file path\n')
            with open(text, 'r') as t_file:
                file_contents = t_file.read()
            break
        except FileNotFoundError:
            print('Invalid file path!!!')
        except Exception:
            print('An unexpected error occured!!!Please try again')
    # Cleaning Text(removing white spaces at the beginning and end)
    clean_text = re.sub(r'\s+', ' ', file_contents).strip()
elif opt == 3:
    print('Thanks for using the program')
    sys.exit()
else:
    print('Only two options are currently available')
    arr_list(src_opt)

# MILESTONE 2 (TEXT PREPROCESSING)
# Make all text lowercase because Python is case sensitive
# Wrapping all text preprocessing process in a function
# Function will make text lowercase, remove punctuations, symbols and accented letters
cleaned_text = txt_pro(clean_text)

# MILESTONE 3 (ANALYSIS)
# List out the analysis options that are available and ask for input
analysis_list = ['Print cleaned text', 'Save cleaned text','Word Count', 'Unique Words', 'exit']
arr_list(analysis_list)

aly_opt = input('What would you like to do??\n')
aly_opt = error(aly_opt)

if aly_opt == 1:
    #Printing cleaned FIle
    print(cleaned_text)
elif aly_opt == 2:
    #Saving cleaned file
    new_text = input('Enter file name\n')
    new_text = new_text.lower().strip()
    new_text = f'{new_text}.txt'
    with open(new_text, 'w') as s_file:
        s_file.write(cleaned_text)
elif aly_opt == 3:
    word_list = str2list(cleaned_text)
    total_words = len(word_list)
    print(total_words)
elif aly_opt == 4:
    word_list = pd.Series(str2list(cleaned_text))
    unique_words = word_list.unique()
    num_unique = len(unique_words)
    print(unique_words, num_unique)
elif aly_opt == 5:
    sys.exit()
else:
    print('There are only five options currently')