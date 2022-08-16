def insertionSort(aList):
	for index in range(1,len(aList)):

		currentvalue = aList[index]
		position = index

		# shift elements over by one
		while position > 0 and aList[position-1] > currentvalue:
                    print(aList)
		    aList[position] = aList[position-1]
		    print(aList)
		    position = position-1

		# insert element in appropriate place
		aList[position] = currentvalue

insertionSort([1, 10, 3, 7, 9, 5])
