#Date: 26-09-18
#Author: Suraj Kumar
#Roll No: 181046037

class BST:
	class _TreeNode:
		def __init__(self,ele):
			self.data=ele
			self.left=None
			self.right=None
	def __init__(self):
		self.root=None	#stores the reference of root
		self.count=0
### Adding a Node to A tree ####
	def add_node(self,ele):
		current=parent=self.root
		while current is not None and current.data!=ele:
			parent=current
			if ele < current.data:
				current=current.left
			elif ele > current.data:
				current=current.right
		if current is None:
			new_node=self._TreeNode(ele)
			if parent is None:
				self.root=new_node
			elif ele < parent.data:
				parent.left=new_node
			elif ele > parent.data:
				parent.right=new_node
			self.count+= 1
	def isempty(self):
		return self.count==0
### To Find number of elements in a Tree###
	def nodecount(self):
		return self.count
#### Method to search element in tree #####
	def lookup(self,key):
		if not self.isempty():
			current =self.root
			while current!=None:
				if current.data>key:
					current=current.left
				elif current.data<key:
					current=current.right
				else:
					break
				return current!=None
### Code for In oreder Traversal###
	def inorder(self):	#in order traversal always print the elements in ascending order
		if not self.isempty():
			self._inorder_(self.root)
	def _inorder_(self,node):
		if not node is None:
			self._inorder_(node.left)
			print(node.data)
			self._inorder_(node.right)
###Code for Pre order Traversal###
	def preorder(self):
		if not self.isempty():
			self._preorder_(self.root)
	def _preorder_(self,node):
		if not node is None:
			print(node.data)
			self._preorder_(node.left)
			self._preorder_(node.right)
###code for Post order Traversal###
	def postorder(self):
		if not self.isempty():
			self._postorder_(self.root)
	def _postorder_(self,node):
		if not node is None:
			self._preorder_(node.left)
			self._preorder_(node.right)
			print(node.data)
############ Level Order ###############
	def level_order(self):
		l=[]
		current=self.root
		l.append(self.root)
		while len(l):
			current=l[0]
			if current.left is not None:
				l.append(current.left)
			if current.right is not None:
				l.append(current.right)
			print(current.data)
			del l[0]
###Code to Delete the element from tree###
	def delete(self,key):
		if not self.isempty():
			self.root=self._delete_(self.root,key)
	def _delete_(self,node,key):
		if node is None:
			return node
		elif key < node.data:
			node.left=self._delete_(node.left,ele)
		elif key > node.data:
			node.right=self._delete_(node.right,ele)
		else:
			if node.left is None:
				temp=node.right
				node=None
				return temp
			elif node.right is None:
				temp=node.left
				node=None
				return temp
			temp=min(node.right)
			node.key=temp.key
			node.right=delete(node.right,temp.key)
		return node
###Code to print minimum element in a tree###
	def min(self,node):
		if node.left is None:
			return node
		else:
			return self.min(node.left)
###Code for Maximum element in Tree###
	def max(self, node):
		if node.right is None:
			return node
		else:
			return self.max(node.right)
###code for Descending oreder of a tree###
	def descending(self):
		if not self.isempty():
			self._descending_(self.root)
	def _descending_(self,node):
		if not node is None:
			self._descending_(node.right)
			print(node.data)
			self._descending_(node.left)
### Code to Find the Height of Tree###
	def height(self):
		return self._height_(self.root)
	def _height_(self,node):
		if node is None:
			return 0
		else:
			leftdepth=self._height_(node.left)
			rightdepth=self._height_(node.right)
		return (max(int(rightdepth)+1,int(leftdepth)+1))
#### method to count number of nodes in the left sub tree ####
	def left_subtree(self):
		current=self.root.left
		return self.count_left(current)
	def count_left(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.count_left(node.left)+self.count_left(node.right))

##### number of nodes in right sub tree ####
	def right_subtree(self):
		current=self.root.right
		return self.count_right(current)
	def count_right(self,node):
		if node is None:
			return 0
		else:
			return 1+(self.count_right(node.left)+self.count_right(node.right))



#B=BST()
data_list=[x for x in input("Enter elements to a tree: ",).split(',')]
for i in data_list:
	B.add_node(i)
print('The elements in a tree: ', B.nodecount())
#print(root)
#B.viewtree()
#ele=input('enter the element to find: ')
#B.lookup(ele)
#B.inorder()
#B.preorder()
#B.postorder()
#B.level_order()
#B.delete(ele)
#B.viewtree()
#B.findMin()
#B.inorder()
#B.descending()
#B.height()
#B.left_subtree()
#B.right_subtree()
