
def main():
    import sys

    try:#Making sure all of the arguments passed in a reasonable
       handSims = int(sys.argv[1])
       standValue=int(sys.argv[2])
       if sys.argv[3][0].lower()== "s":
           stand_on_soft=True
       elif sys.argv[3][0].lower()== "h":
           stand_on_soft=False
       else:
           raise ValueError
    except ValueError:
        print("The sys arguments are as follows:  [1]=number of simmulated hands(int)  [2]=Value on which the dealer will stand(int) and [3]=whether we are standing on hard or soft ace hands(s/h) (str)")
        sys.exit(1)
    busts=0
    hands=0

    for bustLoop in range(handSims):#simulation loop
        cards=[get_card(),get_card()]#Drawing initial hand
        while True:
            if stand(standValue,stand_on_soft,cards)==False:
                cards.append(get_card())#hit
                total,soft_ace_count=score(cards)
                if total>21:
                    busts+=1
                    hands+=1
                    break
            else:
                hands+=1
                break
    print("hands played=", hands)
    print("total busts=", busts)
    print("Bust percentage=",round(busts/hands*100,2))  #output

def get_card():
    import random
    return random.randint (1,13)



def score(cards):
    total=0
    soft_ace_count=0
    for w in range(len(cards)):
         if cards[w]==1:
             cards.append(cards.pop(w))
    for q in range(len(cards)):
        if cards[q]>=2 and cards[q]<=10:
            total+=cards[q]
        elif cards[q]>10:
            total+=10
        else:
            if total<=10:
                total+=11
                soft_ace_count+=1
            else:
                total +=1
    return (total, soft_ace_count)



def stand(stand_on_value, stand_on_soft, cards):
    total,soft_ace_count=score(cards)
    if stand_on_soft==True:
        if total>=stand_on_value:
            return True
        else:
            return False
    else:
        if soft_ace_count==0 and total>=stand_on_value:
            return True
        elif soft_ace_count==0 and total<stand_on_value:
            return False
        elif soft_ace_count!=0 and total>stand_on_value:
            return True
        else:
            return False





if __name__ == '__main__':
        main()
