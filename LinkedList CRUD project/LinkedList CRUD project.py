class Node:
	def __init__(self,nodeData=None):
		self.nodeData = nodeData
		self.nextNode = None


class SinglyLinkedList:# it'll basically act as a wrapper class which will wrap around the whole Singly linked list

	Start = None #static variable

	@staticmethod
	def isEmpty():
		if SinglyLinkedList.Start is None:
			return True
		else:
			return False
	@staticmethod
	def pushData(nodeData):
		node = Node(nodeData)
		if(SinglyLinkedList.isEmpty()):
			SinglyLinkedList.Start = node
		else:
			current = SinglyLinkedList.Start
			while current.nextNode is not None:
				current = current.nextNode
			current.nextNode = node
	@staticmethod
	def insertAtStart(nodeData):
		node = Node(nodeData)
		if(SinglyLinkedList.isEmpty()):
			SinglyLinkedList.Start = node
		else:
			current = SinglyLinkedList.Start
			SinglyLinkedList.Start = node
			node.nextNode = current
	@staticmethod
	def displayData():
		if(SinglyLinkedList.isEmpty()):
			print("Oops!! List is empty")
		else:
			current = SinglyLinkedList.Start
			while current is not None:
				print(current.nodeData,end='->')
				current = current.nextNode
			print("None\n")

	@staticmethod
	def insertAtEnd(nodeData):
		if(SinglyLinkedList.isEmpty()):
			print("Oops!! List is empty")
		else:
			node = Node(nodeData)
			current = SinglyLinkedList.Start
			while current.nextNode is not None:
				current = current.nextNode
			current.nextNode = node

	@staticmethod
	def Size():
		if(SinglyLinkedList.isEmpty()):
			count = 0
			return count
		else:
			current = SinglyLinkedList.Start
			count = 1
			while current.nextNode is not None:
				count += 1
				current = current.nextNode
			return count

	@staticmethod
	def insertAtPos(pos,nodeData):	
		if (pos > SinglyLinkedList.Size() + 1):
			print("Oops! position is out of bond")
		elif pos is 1:
			SinglyLinkedList.insertAtStart(nodeData)
		elif pos is SinglyLinkedList.Size():
			SinglyLinkedList.insertAtEnd(nodeData)
		else:
			node = Node(nodeData)
			current = SinglyLinkedList.Start
			for x in range(pos-2):
				current = current.nextNode
			node.nextNode = current.nextNode
			current.nextNode = node

	@staticmethod
	def reverseLinkedList():
		print("After Reversing linked list =")
		prev = None
		nextt = None
		current = SinglyLinkedList.Start
		while(current is not None):
			nextt = current.nextNode
			current.nextNode = prev
			prev = current
			current = nextt
		SinglyLinkedList.Start = prev

	@staticmethod
	def deleteNthNode(n):
		if n > SinglyLinkedList.Size():
			print(f"Oops!! no element is present at {n}th Position")
		elif n is 1:
			current = SinglyLinkedList.Start
			SinglyLinkedList.Start = SinglyLinkedList.Start.nextNode
			del current
		else:
			prev = SinglyLinkedList.Start
			current = SinglyLinkedList.Start.nextNode
			for x in range(n-2):
				current = current.nextNode
				prev = prev.nextNode
			prev.nextNode = current.nextNode 
			del current

	@staticmethod
	def reverseDisplayRec(current): # current = Start initiated before the call of this fucntion 
		if current is None:
			return
		else:
			SinglyLinkedList.reverseDisplayRec(current.nextNode)
			print(current.nodeData)  
			

data = input("\nEnter the series of data to be pushed into linkedlist (use ',' as delimiter) : \n").split(',')

for d in data:
	SinglyLinkedList.pushData(d)

print('\nYour Linked List :')
SinglyLinkedList.displayData()

while True:
	print('Which operation you want to perform  onto your linkedlist?  :')
	print('1. Insert Data at start')
	print('2. Insert Data at end')
	print('3. Insert Data at nth position')
	print('4. Delete Data at nth position')
	print('5. Reverse display of the linked list')
	print('6. Reverse the whole linked list')
	print('7. Exit\n')
	n = int(input('Enter (1-7) :'))

	if n is 1:
		nodeData = int(input('Enter the data to insert at start = '))
		SinglyLinkedList.insertAtStart(nodeData)
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 2:
		nodeData = int(input('Enter the data to insert at end = '))
		SinglyLinkedList.insertAtEnd(nodeData)
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 3:
		pos = int(input('At which position you want to enter = '))
		nodeData = int(input(f'Enter the data to insert at {pos}th position = '))
		SinglyLinkedList.insertAtPos(pos,nodeData)
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 4:
		n = int(input('Which node you want to delete ?'))
		SinglyLinkedList.deleteNthNode(n)
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 5:
		SinglyLinkedList.reverseLinkedList()
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 6:
		SinglyLinkedList.deleteDuplicate()
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 7:
		SinglyLinkedList.reverseLinkedList()
		print('Linked List after operation :')
		SinglyLinkedList.displayData()
		continue
	elif n is 8:
		exit()
	else:
		print('OOPS!! your Input is out of bound')
