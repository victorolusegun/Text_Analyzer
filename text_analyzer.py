#UserName
name = input('What is your name?\n')
print(f'Welcome {name}!!!')
#Input Options
src_opt = ['Enter manually', 'Read from file']
for index, item in enumerate(src_opt):
    print(f'{index + 1}. {item}')

try:
    opt = input('How would you like to provide text\n')
    opt = int(opt)
except ValueError:
    while opt.isdecimal() == False:
        print('Invalid choice')
        opt = input('Please input numerical values\n')
    opt = int(opt)

if opt == 2:
    try:
        text = input('Please enter file path\n')
    except FileNotFoundError:
        print('Invalid file path!!!')
        text = input('Please enter valid file path')
    with open(text, 'r') as t_file:
        file_contents = t_file.read()
        print(file_contents)
elif opt == 1:
    text = input('Please input text\n')
else:
    print('Only two options are currently available')