import random
import hangman_art as art
from hangman_words import word_list


def game(**kargs):
    print(art.logo)
    
    stages=art.stages
    life=len(stages)-1
    idx=random.randint(0,len(word_list))
    word=word_list[idx]
    print(word)
    postnMap={}
    
    for idx,letter in enumerate(word):
        
        if letter not in postnMap:
            postnMap[letter]=list()
            
        postnMap[letter].append(idx)
        
        
    
    
    
    correctGuess=['_']*len(word)
    
    
    
    while(True):
        print()
        guess=str(input('Guess a letter: '))
        
        
        if guess in postnMap:
            
            print('Hurray you guessed correctly keep going')
            
            allpos=postnMap[guess]
            
            for pos in allpos:
                correctGuess[pos]=guess
                
        else:
            life-=1
            print('Ohhhh No you lose a life')
            
        
        print(stages[life])
        
        if life == 0:
            print('You are dead')
            break
                
        allDone=True
        
        for ch in correctGuess:
            if ch == '_':
                allDone=False
            
            print(ch,end=' ')
            
        if allDone == True:
            print('You have won')
            break
            

                    
game()
    
            
            
           
                    
        

    
    
    
    


