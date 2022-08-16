from Apartment import Apartment

def mergesort(apartmentList):
	if len(apartmentList) > 1:
		mid = len(apartmentList) // 2

		# uses additional space to create the left / right
		# halves
		lefthalf = apartmentList[:mid]
		righthalf = apartmentList[mid:]

		# recursively sort the lefthalf, then righthalf
		mergesort(lefthalf)
		mergesort(righthalf)

		# merge two sorted sublists (left / right halves)
		# into the original list (alist)
		i = 0 # index for lefthalf sublist
		j = 0 # index for righthalf sublist
		k = 0 # index for alist

		while i < len(lefthalf) and j < len(righthalf):
			if (lefthalf[i] < righthalf[j]) or (lefthalf[i] == righthalf[j]): # less than or equal to?
				apartmentList[k] = lefthalf[i]
				i = i + 1
			else:
				apartmentList[k] = righthalf[j]
				j = j + 1
			k = k + 1

		# put the remaining lefthalf elements (if any) into
		# alist
		while i < len(lefthalf):
			apartmentList[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		# put the remaining righthalf elements (if any) into
		# alist
		while j < len(righthalf):
			apartmentList[k] = righthalf[j]
			j = j + 1
			k = k + 1
			
def ensureSortedAscending(apartmentList):
    previous = apartmentList[0]
    index = 1
    while index < len(apartmentList):
        current = apartmentList[index]
        if current < previous:
            return False
        else:
            previous = current
            index += 1
    return True


def getNthApartment(apartmentList, n):
    try:
        return apartmentList[n].getApartmentDetails()
    except Exception:
        return "(Apartment) DNE"

def getTopThreeApartments(apartmentList):
    mergesort(apartmentList)
    index = 0
    string = ''
    while index <= 2 and index <= len(apartmentList)-1:
        if index != 0:
            string += '\n'
        if index == 0:
            string += '1st: '
        elif index == 1:
            string += '2nd: '
        elif index == 2:
            string += '3rd: '
        string += apartmentList[index].getApartmentDetails()
        index += 1
    return string
        
