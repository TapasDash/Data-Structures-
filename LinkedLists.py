class Node:
	def __init__(self,nodeData=None):
		self.nodeData = nodeData
		self.nextNode = None


class SinglyLinkedList:# it'll basically act as a wrapper class which will wrap around the whole Singly linked list

	Start = None #static variable

	def isEmpty():
		if SinglyLinkedList.Start is None:
			return True
		else:
			return False

	def pushData(nodeData):
		node = Node(nodeData)
		if(SinglyLinkedList.isEmpty()):
			SinglyLinkedList.Start = node
		else:
			current = SinglyLinkedList.Start
			while current.nextNode is not None:
				current = current.nextNode
			current.nextNode = node

	def insertAtStart(nodeData):
		node = Node(nodeData)
		if(SinglyLinkedList.isEmpty()):
			SinglyLinkedList.Start = node
		else:
			current = SinglyLinkedList.Start
			SinglyLinkedList.Start = node
			node.nextNode = current

	def displayData():
		current = SinglyLinkedList.Start
		while current is not None:
			print(current.nodeData,end='->')
			current = current.nextNode
		print("None")

	def insertAtEnd(nodeData):
		node = Node(nodeData)
		current = SinglyLinkedList.Start
		while current.nextNode is not None:
			current = current.nextNode
		current.nextNode = node

	def Size():
		current = SinglyLinkedList.Start
		count = 1
		while current.nextNode is not None:
			count += 1
			current = current.nextNode
		return count

	def insertAtPos(pos,nodeData):	
		if(pos > SinglyLinkedList.Size() + 1):
			print("Oops! position is out of bond")
		else:
			node = Node(nodeData)
			current = SinglyLinkedList.Start
			for x in range(pos-2):
				current = current.nextNode
			node.nextNode = current.nextNode
			current.nextNode = node

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

	def deleteNthNode(n):
		if n > SinglyLinkedList.Size():
			print("Oops!! no element is present at",n,"Position")
		elif n is 1:
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

	def reverseDisplayRec(current): # current = Start initiated before the call of this fucntion 
		if current is None:
			return
		else:
			SinglyLinkedList.reverseDisplayRec(current.nextNode)
			print(current.nodeData)  


	def reverseLinkedListRec(current,nextt): # current = Start initiated before the call of this fucntion
		if nextt is None:					# next = Start.nextNode
			SinglyLinkedList.Start = current 
			return
		else:
			SinglyLinkedList.reverseLinkedListRec(current.nextNode,nextt.nextNode)
			nextt.nextNode = current
			current.nextNode = None

	def deleteDuplicate():
		data = SinglyLinkedList.Start
		prev = SinglyLinkedList.Start.nextNode
		current = prev.nextNode
		
		
		while data is not None: # while(data!=NULL) in C++/Java

			while current is not None: # while(current!=NULL) in C++/Java

				if data.nodeData is prev.nodeData:
					data.nextNode = current
					del prev

				elif data.nodeData is current.nodeData:
					prev.nextNode = current.nextNode
					del current

				else:
					current = current.nextNode
					prev = prev.nextNode

		data = data.nextNode
		prev = data.nextNode
		current = prev.nextNode



SinglyLinkedList.pushData(5)
SinglyLinkedList.pushData(7)
SinglyLinkedList.pushData(8)
SinglyLinkedList.pushData(8)
SinglyLinkedList.pushData(9)
SinglyLinkedList.displayData()
print(SinglyLinkedList.Size())
SinglyLinkedList.deleteDuplicate()
SinglyLinkedList.displayData()
