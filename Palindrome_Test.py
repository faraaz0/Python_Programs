'''

A string is said to be palindrome if reverse of the string is same as string.
For example, “radar” is main string and it's reverse string is 'radar',So main string is equle to reverse string. So 'radar' is palindome string.
'radix' is main string and it's reverse string is'xidar'.So main string is not equle reverse string.So 'radix' is not palindrome string.

'''

# 1. By using loop.
    str1=input('enter the string')                           # string input
    str2=str1[::-1]                                          # reverse string
    if str2==str1:
        print('string is palindome.')
    else:
        print('string i not palindome.')





# 2.By using function.
    def palindome_check(str):
        out=str[::-1]
        return out


    str=input('enter the string')
    out=palindome_check(str)
    if str==out:
        print('string is palindome.')
    else:
        print('string is not palindome.')


