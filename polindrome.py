polind=(input('Insert word for check for polindrome:\n'))

def polindrome(n):
    return n==n[::-1]

yes_no=polindrome(polind)

if yes_no == True:
    print('It is a polindrome')
else:
    print('It is not a polindrme')