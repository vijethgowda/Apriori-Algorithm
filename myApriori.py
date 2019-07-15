from collections import defaultdict

def get_transactions():
	file = open('store_data(1).csv')
	items = set()
	transactions = list()
	for trans in file:
		item_list = trans.split(',')
		transactions.append(item_list[:-1])
		for item in item_list:
			items.add(item)
	#items.remove('')
	#items.remove('\n')
	return transactions, items

def getSupport(transactions, items):
	freqSet = defaultdict(int)
	for item in items:
		for trans in transactions:
			if item in trans:
				freqSet[item] += 1
	return (freqSet)

def getItemsWithMinSupport(dataset, minSupp):
	newItems = []
	for item in dataset:
		if item[1] >= minSupp:
			newItems.append(item)
	return newItems
	'''
	for item in dataset:
		if item[1] < minSupp:
			dataset.remove(item)
	return dataset
	'''

def getNewItems(dataset):
	newItemSet = list()
	n = len(dataset)
	for i in range(n):
		for j in range(i+1, n):
			newItem = [dataset[i][0], dataset[j][0]]
			newItemSet.append(newItem)

	return newItemSet

def getNewSupport(transactions, items):
	freqSet = defaultdict(int)
	for item in items:
		for trans in transactions:
			flag = 0
			_item = ""
			for i in range(len(item)):
				_item += item[i]
				if item[i] not in trans:
					flag=1
					break
			if flag==0:
				freqSet[_item] += 1
	return (freqSet)


if __name__ == '__main__':
	
	transactions, items = get_transactions()
	#minSupp = int(input("Enter the minimum support: "))
	#minConf = int(input("Enter the minimum confidence: "))
	minSupp = 10
	minConf = 60
	minSupp = (minSupp/100) * len(transactions)

	print("C1: ------------------------")
	freqSet = getSupport(transactions, items)
	requiredFreqSet = {}
	requiredFreqSet = sorted(freqSet.items())
	for item in requiredFreqSet:
		print(item)

	print("L1: ------------------------")
	itemsWithMinSupport = getItemsWithMinSupport(requiredFreqSet, minSupp)
	for item in itemsWithMinSupport:
		print(item)


	items = getNewItems(itemsWithMinSupport)

	print("\n\n\nC2: ------------------------")
	freqSet = getNewSupport(transactions, items)
	requiredFreqSet = {}
	requiredFreqSet = sorted(freqSet.items())
	for item in requiredFreqSet:
		print(item)

	print("L2: ------------------------")
	itemsWithMinSupport = getItemsWithMinSupport(requiredFreqSet, minSupp)
	for item in itemsWithMinSupport:
		print(item)

	items = getNewItems(itemsWithMinSupport)
	newItems = []
	for i in range(len(items)):
		item = []
		a = list(items[i][0])
		b = list(items[i][1])
		item = sorted(list(set(a + b)))
		if (len(item) == 3) and (item not in newItems):
			newItems.append(item)

	items = newItems
	print("\n\n\nC3: ------------------------")
	freqSet = getNewSupport(transactions, items)
	requiredFreqSet = {}
	requiredFreqSet = sorted(freqSet.items())
	for item in requiredFreqSet:
		print(item)

	print("L3: ------------------------")
	itemsWithMinSupport = getItemsWithMinSupport(requiredFreqSet, minSupp)
	for item in itemsWithMinSupport:
		print(item)