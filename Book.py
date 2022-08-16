class Book:
    def __init__(self, title = '', author = '', year = None):
        self.title = title
        self.author = author
        self.year = year
    def getTitle(self):
        return self.title
    def getAuthor(self):
        return self.author 
    def getYear(self):
        return self.year 
    def getBookDetails(self):
        return ('Title: {}, Author: {}, Year: {}'.format(self.title, self.author, self.year))
    def __gt__(self, rhs):
        if self.author.lower() == rhs.author.lower():
            if self.year == rhs.year:
                return self.title.lower() > rhs.title.lower()
            else:
                return self.year > rhs.year
        else:
            return self.author.lower() > rhs.author.lower()
