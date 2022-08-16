class Apartment:
    def __init__(self, rent = 0, metersFromUCSB = 0, condition = 'N/A'):
        self.rent = rent
        self.metersFromUCSB = metersFromUCSB
        self.condition = condition
    def getRent(self):
        return self.rent
    def getMetersFromUCSB(self):
        return self.metersFromUCSB
    def getCondition(self):
        return self.condition
    def getApartmentDetails(self):
        return '(Apartment) Rent: ${}, Distance From UCSB: {}m, Condition: {}'.format(self.rent, self.metersFromUCSB, self.condition)
    def __lt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent < rhs.rent
        elif self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB < rhs.metersFromUCSB
        elif self.condition != rhs.condition:
            if self.condition == 'excellent':
                return True
            elif self.condition == 'average':
                if rhs.condition == 'excellent':
                    return False
                else:
                    return True
            elif self.condition == 'bad':
                return False
        else:
            return False
    def __gt__(self, rhs):
        if self.rent != rhs.rent:
            return self.rent > rhs.rent
        elif self.metersFromUCSB != rhs.metersFromUCSB:
            return self.metersFromUCSB > rhs.metersFromUCSB
        elif self.condition != rhs.condition:
            if self.condition == 'excellent':
                return False
            elif self.condition == 'average':
                if rhs.condition == 'excellent':
                    return True
                else:
                    return False
            elif self.condition == 'bad':
                return True
        else:
            return False
    def __eq__(self, rhs):
        if type(rhs) != type(self):
            return False
        return (self.rent == rhs.rent) and (self.metersFromUCSB == rhs.metersFromUCSB) and (self.condition == rhs.condition)
