print('Welcome to CHOOSE YOUR OWN ADVENTURE!')
name = input('What is your name? ')
age = int(input('What is your age? '))

print('Hello', name, 'you are', age, 'years old')

if age >= 18:
    print('You are old enough to play!')
    
    wants_to_play = input('Do you want to play? ').lower()
    if wants_to_play == "yes":
        print('Lets play!')
        
        left_or_right = input('First choice... Left or Right (left/right)? ')
        if left_or_right = "left".lower():
            ans = input('Nice, you follow the path and reach a lake....Do you swim across or go around? (across/around)? ')
            
            if ans == 'around':
            
            elif ans == 'across':
            
            else:
                print('You lost.')


        else:
            print('You fell down and lost...')


    else:
        print('Cya....')    



else:
    print('Sorry, you are not old enough to play.')
