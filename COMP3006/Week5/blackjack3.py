
def main():

    import sys,csv
    from collections import defaultdict,Counter

    try:#Making sure all of the arguments passed in correctly
        handSims = int(sys.argv[1])

    except ValueError:
        print("The sys argument is as follows:  [1]=number of simulated hands(int)")
        sys.exit(1)

    with open('week5Blackjackdata.csv', 'w+',newline='') as f:
            write = csv.writer(f)
            gridList=[['P-Strategy','D-H13','D-S13','D-H14','D-S14','D-H15','D-S15','D-H16','D-S16','D-H17','D-S17','D-H18','D-S18','D-H19','D-S19','D-H20','D-S20']]


            for player in range(13,21):#looping through the player strategies
                    for sh in range(2):
                        if sh==0:
                            playerSoft=False
                            SH="H"
                        else:
                            playerSoft=True
                            SH="S"

                        stratList=[]
                        stratList.append("P-"+str(player)+SH)

                        for dealer in range(13,21):#looping through the dealer strategies
                            for ch in range(2):
                                if ch==0:
                                    dealersoft=False
                                else:
                                    dealersoft=True


                                playerWs=0
                                handsPlayed=0
                                while handsPlayed < handSims:
                                    playerStrat=Strategy(player,playerSoft)
                                    playerhand=playerStrat.play()
                                    playerscore,_ = playerhand.score()


                                    dealerStrat=Strategy(dealer,dealersoft)
                                    dealerhand=dealerStrat.play()
                                    dealerscore,_ =dealerhand.score()

                                    if playerhand.is_bust() or (not playerhand.is_blackjack() and dealerhand.is_blackjack()) :
                                        handsPlayed+=1#Loss situation #1
                                    elif (not playerhand.is_bust() and not dealerhand.is_bust()) and playerscore<dealerscore:
                                        handsPlayed+=1 #Loss situations #2
                                    elif (not playerhand.is_bust() and dealerhand.is_bust()) or (playerhand.is_blackjack() and not dealerhand.is_blackjack()):
                                        playerWs+=1 #Win situations #1
                                        handsPlayed+=1
                                    elif (not playerhand.is_bust() and not dealerhand.is_bust()) and playerscore>dealerscore:
                                        playerWs+=1#Win situations #2
                                        handsPlayed+=1
                                    else:
                                        handsPlayed+=0 #Push
                                stratList.append(round(playerWs/handsPlayed*100,1))
                        gridList.append(stratList)
            write.writerows(gridList)



class Hand:

    def __init__(self,cards=None):
        if cards==None:
            self.cards = []
        else:
            self.cards=cards
            self.total, self.soft_ace_count = self.score()

    def __str__(self):
        return 'Hand(cards='+self.cards+',total='+self.total+',soft_ace_count='+self.soft_ace_count+')'

    def add_card(self):
        import random
        self.cards.append(random.randint (1,13))
        self.score()
        return self.total

    def is_blackjack(self):
        if len(self.cards)==2 and self.total==21:
            return True
        else:
            return False

    def is_bust(self):
        if self.total>21:
            return True
        else:
            return False

    def score(self):

        self.total=sum(min(x,10)for x in self.cards)
        self.soft_ace_count=0

        if self.total < 12 and 1 in self.cards:
            self.total += 10
            self.soft_ace_count = 1

        return self.total,  self.soft_ace_count


class Strategy:

    def __init__(self,stand_on_value, stand_on_soft):
        self.stand_on_value = stand_on_value
        self.stand_on_soft = stand_on_soft


    def __repr__(self):
         return '{stand_on_value'+self.stand_on_value+', stand_on_soft:'+(self.stand_on_soft)+ '}'

    def __str__(self):
        if self.stand_on_soft == True:
            return 'S'+''+str(self.stand_on_value)+''
        if self.stand_on_soft == False:
            return 'H'+''+str(self.stand_on_value)+''

    def stand(self, h):
        total, soft_ace_count = h.score()

        if self.stand_on_soft==True:
            if total >= self.stand_on_value:
                return True
            else:
                return False
        else:
            if (soft_ace_count == 0 and total >= self.stand_on_value) or (soft_ace_count != 0 and total > self.stand_on_value):
                return True
            else:
                return False

    def play(self):

        import random
        #Hand.cards=[(random.randint (1,13)),(random.randint (1,13))]#Drawing initial hand

        # instantiating an object named h of type Hand
        h = Hand([random.randint (1,13), random.randint (1,13)])

        while not self.stand(h):
            h.add_card()
        return h



if __name__ == '__main__':
        main()
