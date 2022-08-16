from Card import Card

class PlayerHand:
    def __init__(self):
        self.root = None
        self.card_count = 0
        
    def getTotalCards(self):
        return self.card_count

    def isEmpty(self):
        return self.card_count == 0
    
    def getMin(self):
        if self.root:
            current = self.root
            while current.hasLeftChild():
                current = current.left
            return current
        else:
            return None

    def getSuccessor(self, suit, rank):
        card = Card(suit, rank)
        currentNode = self._get(card, self.root)
        if currentNode:
            return currentNode.findSuccessor()
    
    def put(self, suit, rank):
        if self.root:
            dupli = self.get(suit, rank)
            if dupli:
                dupli.setCount(dupli.getCount() + 1)
            else:
                card = Card(suit, rank)
                self._put(card, self.root)
        else:
            card2 = Card(suit, rank)
            self.root = card2
        self.card_count = self.card_count + 1

    def _put(self, card, currentNode):
        if card < currentNode:
            if currentNode.hasLeftChild():
                self._put(card, currentNode.left)
            else:
                card.setParent(currentNode)
                currentNode.setLeft(card)
        elif card > currentNode:
            if currentNode.hasRightChild():
                self._put(card, currentNode.right)
            else:
                card.setParent(currentNode)
                currentNode.setRight(card)
            
    def delete(self, suit, rank):
        if not self.root:
            return False
        if self.card_count > 1 and self.root.hasAnyChildren():
            deletion_card = self.get(suit, rank)
            if deletion_card:
                deletion_card.setCount(deletion_card.getCount() - 1)
                self.card_count = self.card_count - 1
                if deletion_card.getCount() == 0:
                    self.remove(deletion_card)
            else:
                return False
        if not self.root.hasAnyChildren() and self.root == Card(suit, rank):
            self.root.setCount(self.root.getCount() - 1)
            self.card_count = self.card_count - 1
            if self.root.getCount() == 0:
                self.root = None
        elif not self.root.hasAnyChildren() and self.root != Card(suit, rank):
            return False
        return True

    def remove(self, currentNode):
        if currentNode.isLeaf():
            if currentNode.isLeftChild():
                currentNode.parent.left = None
            elif currentNode.isRightChild():
                currentNode.parent.right = None
        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.suit = succ.suit
            currentNode.rank = succ.rank
            currentNode.count = succ.count
        else:
            if currentNode.getLeft():
                if currentNode.isLeftChild():
                    currentNode.left.setParent(currentNode.parent)
                    currentNode.parent.setLeft(currentNode.getLeft())
                elif currentNode.isRightChild():
                    currentNode.left.setParent(currentNode.parent)
                    currentNode.parent.setRight(currentNode.getLeft()) #?
                else:
                    currentNode.count = currentNode.left.count
                    currentNode.replaceNodeData(currentNode.left.getSuit(), \
                                                currentNode.left.getRank(), \
                                                currentNode.left.getLeft(), \
                                                currentNode.left.getRight())
            else:
                if currentNode.isLeftChild():
                    currentNode.right.setParent(currentNode.parent)
                    currentNode.parent.setLeft(currentNode.getRight())
                elif currentNode.isRightChild():
                    currentNode.right.setParent(currentNode.parent)
                    currentNode.parent.setRight(currentNode.getLeft())
                else:
                    currentNode.count = currentNode.right.count
                    currentNode.replaceNodeData(currentNode.right.getSuit(), \
                                                currentNode.right.getRank(), \
                                                currentNode.right.getLeft(), \
                                                currentNode.right.getRight())
                 

    def get(self, suit, rank):
        if self.root:
            card = Card(suit, rank)
            res = self._get(card, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _get(self, card, currentNode):
        if currentNode and card:
            if currentNode == card:
                return currentNode
            elif card < currentNode:
                return self._get(card, currentNode.left)
            else:
                return self._get(card, currentNode.right)

    def inOrder(self, card = None):
        inorder_string = ''
        if card is None:
            card = self.root
        if card:
            if card.hasLeftChild():
                inorder_string += self.inOrder(card.getLeft())
            inorder_string += card.__str__() #?
            if card.hasRightChild():
                inorder_string += self.inOrder(card.getRight())
        return inorder_string
        
    
    def preOrder(self, card = None):
        preorder_string = ''
        if card is None:
            card = self.root
        if card:
            preorder_string += card.__str__() #?
            if card.hasLeftChild():
                preorder_string += self.preOrder(card.getLeft())
            if card.hasRightChild():
                preorder_string += self.preOrder(card.getRight())
        return preorder_string
                
                 

hand = PlayerHand()
hand.put('D', 'A')
hand.put('S', 'K')
hand.put('S', '2')
hand.put('C', 'Q')
hand.put('H', '7')
hand.put('S', 'K')
hand.put('C', 'K')
#print(hand.getSuccessor('S', 'K'))
#print(hand.getSuccessor('D', 'A'))
#print(hand.getMin())
#print(hand.isEmpty())
#print(hand.getTotalCards())
#print(hand.preOrder())
#print(hand.get('S', 'K'))
#print(hand.getSuccessor('H', '7'))
'''
assert hand.preOrder() == \
"D A | 1\n\
S K | 2\n\
S 2 | 1\n\
C Q | 1\n\
H 7 | 1\n\
C K | 1\n"

assert hand.inOrder() == \
"D A | 1\n\
S 2 | 1\n\
H 7 | 1\n\
C Q | 1\n\
C K | 1\n\
S K | 2\n"
'''

#print(hand.root)
#print(hand.root.right)
#print(hand.root.right.left)
#print(hand.root.right.left.right)
#print(hand.root.right.left.left)
#print(hand.root.right.left.right.left)
#print(hand.root.right.left.right.left.right,1)
#print(hand.root.right.left.right.left.left,2)

#print(hand.root.right.left.right.right)
#print(hand.root.right.left.right.right.right)
#print(hand.root.right.left.right.right.left)
