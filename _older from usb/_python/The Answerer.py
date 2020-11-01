from random import choice
print('Ask a closed question (question in which the answer can only be yes or no) and I will tell you the answer!')
while True:
    Question = input()
    print('Interesting question...')
    if Question == 'is Joel gay':
        Answer = 'no'
    elif Question == 'is Joel clever':
        Answer = 'yes'
    elif Question == 'does Joel smell':
        Answer = 'no'
    else:
        Answer = choice(['yes', 'no'])
    print('The answer is', Answer, end='!')
    print( )
    print('Ask another question!')
