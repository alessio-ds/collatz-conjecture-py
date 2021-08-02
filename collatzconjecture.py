print('This program tests the Collatz Conjecture:\nIf the number is odd, you multiply it by 3 and add 1.\nIf its even, you divide by 2.\nAt the end, you will always end up with the number "1".\n')
a=input('Pick any positive integer you want: ')
print('\n')
a=int(a)

cont=0
while a!=1:
    if a%2==1:
        print('(',a,'* 3 ) + 1 =',((a*3)+1))
        a=int((a*3)+1)
    else:
        print(a,'/ 2 =',(a/2))
        a=a/2
    #print(a)
    cont+=1

print('\nTotal jumps:',cont)
