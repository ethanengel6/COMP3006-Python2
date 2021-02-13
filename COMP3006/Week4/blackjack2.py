
def main():

    import sys,csv
    from collections import namedtuple,defaultdict,Counter

    try:#Making sure all of the arguments passed in a reasonable
       handSims = int(sys.argv[1])

    except ValueError:
        print("The sys argument is as follows:  [1]=number of simulated hands(int)")
        sys.exit(1)

    with open('week5Blackjackdata.csv', 'w+',newline='') as f:

        strats = ['13H','13S','14H','14S','15H','15S','16H','16S','17H','17S','18H','18S','19H','19S','20H','20S']
        stratscounter=0


            for stand_on_value in range(13,21):#looping through the strategies
                for sh in range(2):
                    if sh==0:
                        stand_on_soft=False

                    else:
                        stand_on_soft=True


                    for xx in range(handSims):#simulation loop

                        total=play_hand(stand_on_value, stand_on_soft)

                        if total > 21:
                            hand_total_list.append('BUST')#creating a list of final hand totals
                        else:
                            hand_total_list.append(total)


                for hands in hand_total_list:  #transforming said list into a dictionary of counts
                    hand_total_count[hands] += 1


                hand_total_count['Strategy']=strats[stratscounter]
                stratscounter+=1

                print(hand_total_list)
                hand_total_count['BUST']=round((hand_total_count['BUST']/handSims)*100,1)
                for zz in range(13,22):

                    hand_total_count[zz]=round((hand_total_count[zz]/handSims)*100,1)#turning dictionary of counts into dictionary of %s

                print(hand_total_count)
                f_csv.writerow(hand_total_count)  #writing to csv



def get_card():
    import random
    return random.randint (1,13)



def score(cards):  #computing score from the hand that was dealt

    from collections import namedtuple
    Score=namedtuple('Score', 'total soft_ace_count')
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
    hand_score=Score(total, soft_ace_count)
    return hand_score



def stand(cards,stand_on_value, stand_on_soft,hand_score):#function to determine whether dealer stands/hits
    from collections import namedtuple
    Stand=namedtuple('Stand','stand total')


    if stand_on_soft==True:
        if hand_score[0]>=stand_on_value:
            return Stand(True, hand_score[0])
        else:
            return Stand(False, hand_score[0])
    else:
        if hand_score[1]==0 and hand_score[0]>=stand_on_value:
            return Stand(True, hand_score[0])
        elif hand_score[1]==0 and hand_score[0]<stand_on_value:
            return Stand(False, hand_score[0])
        elif hand_score[1]!=0 and hand_score[0]>stand_on_value:
            return Stand(True, hand_score[0])
        else:
            return Stand(False, hand_score[0])

def play_hand(stand_on_value, stand_on_soft): #function comprised of initial deal, score, determine if stand/hit, potentially
                                                #recalculate the score; if stand, compute final total score
    #total=0
    cards=[get_card(),get_card()]#Drawing initial hand

    while True:
        hand_score=score(cards)

        if stand(cards,stand_on_value, stand_on_soft,hand_score)==(False, hand_score[0]):
            cards.append(get_card())#hit
        else:
            break
    total = hand_score[0]
    return total


if __name__ == '__main__':
        main()
