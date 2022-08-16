class Card:
    def __init__(self, suit = None, rank = None):
        self.suit = suit
        if suit:
            self.suit = suit.upper()
        self.rank = rank
        if rank:
            self.rank = rank.upper()
        self.count = 1
        self.parent = None
        self.left = None
        self.right = None
        
    def getSuit(self):
        return self.suit
    
    def setSuit(self, suit):
        self.suit = suit.upper()
        
    def getRank(self):
        return self.rank
    
    def setRank(self, rank):
        self.rank = rank.upper()
        
    def getCount(self):
        return self.count
    
    def setCount(self, count):
        self.count = count
        
    def getParent(self):
        return self.parent
    
    def setParent(self, parent):
        self.parent = parent
        
    def getLeft(self):
        return self.left
    
    def setLeft(self, left):
        self.left = left
        self.left.parent = self
        
    def getRight(self):
        return self.right
    
    def setRight(self, right):
        self.right = right
        self.right.parent = self
        
    def isLeaf(self):
        return not (self.getLeft() or self.getRight())
    
    def isRoot(self):
        return not (self.getParent())
    
    def hasBothChildren(self):
        return (self.getRight() and self.getLeft())
    
    def hasAnyChildren(self):
        return (self.getRight()) or (self.getLeft())
    
    def hasLeftChild(self):
        return self.getLeft()
    
    def hasRightChild(self):
        return self.getRight()
    
    def isLeftChild(self):
        if self.parent is None:
            return False
        else:
            return self.parent and self.parent.left.rank == self.rank
        
    def isRightChild(self):
        return self.parent and self.parent.getRight() == self
    
    def __str__(self):
        string = '{} {} | {}\n'.format(self.suit, self.rank, self.count)
        return string
    
    def replaceNodeData(self, suit, rank, lc, rc):
        self.suit = suit
        self.rank = rank
        self.left = lc
        self.right = rc
        if self.left:
            self.left.parent = self
        if self.right:
            self.right.parent = self
            
    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None
        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left
                self.left.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
                self.right.parent = self.parent

    def findSuccessor(self):
        succ = self
        if succ:
            if self.hasRightChild():
                succ = self.right.findMin()
            else:
                if self.parent:
                    if self.isLeftChild():
                        succ = self.parent
                    elif self.isRightChild():
                        succ = self
                        while succ:
                            if self.parent.isLeftChild() and self.parent.parent and self.parent.parent > self:
                                succ = self.parent.parent
                                return succ
                            else:
                                succ = self.parent       
                        succ = self.parent.findSuccessor()
                        self.parent.right = self
                else:
                    succ = None
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def __gt__(self, rhs):
        if self.rank.upper() != rhs.rank.upper():
            card_dict = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
            return card_dict[self.rank.upper()] > card_dict[rhs.rank.upper()]
        if self.suit.upper() != rhs.suit.upper():
            card_dict2 = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
            return card_dict2[self.suit.upper()] > card_dict2[rhs.suit.upper()]
        else:
            return False
            
    def __lt__(self, rhs):
        if self.rank.upper() != rhs.rank.upper():
            card_dict = {'A': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}
            return card_dict[self.rank.upper()] < card_dict[rhs.rank.upper()]
        if self.suit.upper() != rhs.suit.upper():
            card_dict2 = {'C': 0, 'D': 1, 'H': 2, 'S': 3}
            return card_dict2[self.suit.upper()] < card_dict2[rhs.suit.upper()]
        else:
            return False

    def __eq__(self, rhs):
        if (not self) or (not rhs):
            return False
        elif (self.rank.upper() == rhs.rank.upper()) and (self.suit.upper() == rhs.suit.upper()):
            return True
        else:
            return False

card = Card('D', 'A')
card2 = Card('S', '2')
card4 = Card('S', 'A')
card3 = Card('H', '7')
card.setRight(card2)
card2.setLeft(card4)
card2.setRight(card3)
#print(card4.isRightChild())
#print(card4.isLeftChild())
