# Importing Library
import re

# UserName
name = input('What is your name?\n')
print(f'Welcome {name}!!!')

# Input Options
src_opt = ['Enter manually', 'Read from file']
for index, item in enumerate(src_opt):
    print(f'{index + 1}. {item}')

# Validating User Choice
try:
    opt = input('How would you like to provide text\n')
    opt = int(opt)
except ValueError:
    while opt.isdecimal() == False:
        print('Invalid choice')
        opt = input('Please input numerical values\n')
    opt = int(opt)

# Accepting Text To Be Analyzed and Cleaned
if opt == 2:
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
    # Cleaning Text
    clean_text = re.sub(r'/s+', '', file_contents).strip()
elif opt == 1:
    text = input('Please input text\n')
    #Cleaning Text
    clean_text = re.sub(r'/s+', '', text).strip()
else:
    print('Only two options are currently available')
