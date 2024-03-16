#!/usr/bin/python3

banner1 = '''

'''

banner2 = '''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
'''

blacklist = [';', '"', 'os', '_', '\\', '/', '`',
             ' ', '-', '!', '[', ']', '*', 'import',
             'eval', 'banner', 'echo', 'cat', '%',
             '&', '>', '<', '+', '1', '2', '3', '4',
             '5', '6', '7', '8', '9', '0', 'b', 's',
             'lower', 'upper', 'system', '}', '{']

while True:
    ans = input('Break me, shake me!\n\n$ ').strip()

    if any(char in ans for char in blacklist):
        print(f'\n{banner1}\nNaughty naughty..\n')
    else:
        try:
            eval(ans + '()')
            print('WHAT WAS THAT?!\n')
        except:
            print(f"\n{banner2}\nI'm UNBREAKABLE!\n")

# input = print(open('flag.txt','r').read()).hex
# HTB{3v4l_0r_3vuln??}