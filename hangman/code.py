score = 0
def openFile(category):
    line = open(category+".txt").read().splitlines()
    for i in line:
        i = i.strip().split(',')
        word = i[0]
        hint = i[1]
        hangman(word,hint)
def hangman(word,hint):
    global score
    guess = 10
    word_len = len(word)
    word2guess = ""
    for i in range(len(word)):
        if(word[i].isalpha()):
            word2guess = word2guess + '_'
        else:
            word2guess = word2guess + word[i]
    print(word2guess)
    print("Hint: " + hint)
    while True:
        if(guess<=0):
            print("GAMEOVER")
            exit()
        if('_' not in word2guess):
            a = input("press any button to continue")
            break
        letter = input("input alphabet : ").strip().lower()
        if(letter in word and letter not in word2guess):
            score = score + 10
            for i in range (word_len):
                if(word[i] == letter):
                    word2guess = word2guess[:i] + letter + word2guess[i + 1:]
            print(word2guess + "\tscore " + str(score) + ", remaining wrong guess "+ str(guess))
        else:
            guess = guess - 1
            print(word2guess + "\tscore " + str(score) + ", remaining wrong guess "+
                  str(guess) + ", wrong guessed: " + letter)
print("Select Category From Below List:")
categoryList = ("animal","color")
for name in categoryList:
    print(name)
category = input().strip().lower()
openFile(category)        
    

