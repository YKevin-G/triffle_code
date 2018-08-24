import os
class node:
	value = None
	# 文件名列表
	filelist = []
	# 文件目录名列表
	dirnamelist = []
	# 文件对象列表
	dirobjlist = []
	def __init__(value):
		value = value

class DFS(object):
	"""docstring for DFSandBFS"""
	def __init__(self,root):
		super(DFS, self).__init__()
		# 这就相当于在深度优先遍历时的栈用list来模拟，list有pop,和leftpop(模拟队列时使用)
		preffix = []
		root = root
	def mainn(self):
		if(self.root == "计算机"):
			# 表明这是整个计算机文件系统的根节点
		else:
			# 根节点下的某一个目录或者文件
			if(os.path.isdir(self.root)):
				self.preffix.append(self.root)
				nnode = node(self.root)
				for name in os.path.listdir(self.root):
					if(os.path.isdir(name)):
						self.nnode.dirnamelist.append(name)
					else:
						self.nnode.filelist.append(name)
				# 这个用来包含每一个文件下的目录，
				outline = []
				outline.append(dirnamelist)
				while(len(outline)>=1):
					temp = outline.pop()

				
			else:
				# 这是文件


		
