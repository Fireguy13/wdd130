#import guesser
# class Equipment:
#     def __init__(self):
#         self.parachute="   _____ \n"+"  /_____\ \n"+"  \     / \n"+"   \   / "
#         self.skydiver="     0 \n"+"    /|\ \n"+"    / \ "
#         self.word="yolo"

#     def blast_parachute(self):
        #  if word==False:
        #      parachute=parachute[10:]
        #      print(parachute)
        #      print(skydiver)
        #  else:
        #      break

def main():       
    parachute="   _____ \n"+"  /_____\ \n"+"  \     / \n"+"   \   / "
    skydiver="     0 \n"+"    /|\ \n"+"    / \ "
    print(parachute)
    print(skydiver)
    word="word"
    break_parachute(parachute,skydiver,word)


def break_parachute(parachute,skydiver,word):
    n=0
    letters=[]
    while n !=5:
        n+=1
        safe(letters,word)
        print()
        print()
        pp=input("Type [only] a letter ")
        if pp in letters:
            while pp in letters:
                print(parachute)
                print(skydiver)
                print()
                pp=input("Type [only] a letter ")
            print()
        if pp not in word:
            parachute=parachute[10:]
            print(parachute)
            if n!=3:
                print(skydiver)

        if n==4:
            skydiver=skydiver.replace("     0 \n","     X \n")
            print(skydiver)
            print()
            safe(letters,word)
            break
        n+=1
        if pp in word:
            letters.append(pp)
            print(parachute)
            print(skydiver)
            if len(word)== len(letters):
                safe(letters,word)
                break


def safe(letters,word):
    for letter in word:
        if letter.lower()in letters:
            print(letter,end=" ")
        else:
            print("_",end=" ")

main()




# letters=[]
# word="holamundo"
# for i in word:
#     letters.append(i)
# hidden_word="_"*len(word)
# print(hidden_word)
# for letter in letters:
#     print(f"{letter}",end="")

# for letter in word:
#     if letter.lower()in letters:
#         print(letter,end=" ")
#     else:
#         print("_",end=" ")

            # safe(letters,word)
            # print()
            # print()

