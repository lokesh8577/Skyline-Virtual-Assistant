import random
def game():
    print("you are playing a game....")
    score=random.randint(1,100)
    with open("/Users/sonu/Documents/python/file i/p/high_score.txt") as f:
        hiscore=f.read()
        if(hiscore!=''):
            hiscore=int(hiscore)
        else:
            hiscore=0    

    print(f"your score is {score}")
    if(score>hiscore):
        with open("/Users/sonu/Documents/python/file i/p/high_score.txt",'w') as f:
            f.write(str(score))
            
    return score

f =open("/Users/sonu/Documents/python/file i/p/high_score.txt",'w')

game()