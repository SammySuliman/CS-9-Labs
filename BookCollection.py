from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False
    def getNumberOfBooks(self):
        if self.isEmpty() == False:
            current = self.head
            counter = 1
            while current.getNext != None:
                current = current.getNext()
                if current == None:
                    break
                counter += 1
            return counter
        else:
            return 0
    def insertBook(self, book):
        current = self.head
        previous = None
        stop = False

        # find the correct place in the list to add
        while current != None and not stop:
            if current.getData() > book:
                stop = True
            else:
                previous = current
                current = current.getNext()

        # create Node with item to add
        temp = BookCollectionNode(book)

	# Case 1: insert at the front of the list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else: # Case 2: insert not at front of list
            temp.setNext(current)
            previous.setNext(temp)
    def getBooksByAuthor(self, author):
        current = self.head
        string = ''
        while current != None:
            if current.getData().author.lower() == author.lower():
                string += ('Title: {}, Author: {}, Year: {}\n'.format(current.getData().title, current.getData().author, current.getData().year))
                current = current.getNext()
            else:
                current = current.getNext()
        return string
    def getAllBooksInCollection(self):
        current = self.head
        string = ''
        while current != None:
            string += ('Title: {}, Author: {}, Year: {}\n'.format(current.getData().title, current.getData().author, current.getData().year))
            current = current.getNext()
        return string
        
            
#b0 = Book("Cujo", "King, Stephen", 1981)
#b1 = Book("The Shining", "King, Stephen", 1977)
#b2 = Book("Ready Player One", "Cline, Ernest", 2011)
#b3 = Book("Rage", "King, Stephen", 1977)

#bc = BookCollection()
#bc.insertBook(b0)
#bc.insertBook(b1)
#bc.insertBook(b2)
#bc.insertBook(b3)

#temp = BookCollectionNode(b2)

#print(bc.getBooksByAuthor('Cline, ErNest'))
#print(temp.getData().author.lower() == 'KING, Stephen'.lower())
#print(bc.getAllBooksInCollection())

#print(bc.getNumberOfBooks())

