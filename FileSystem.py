from BlockDevice.py import *
from numpy import *

class FileSystem:



@staticmethod
def createFileSystem(filename,block_count,magicNumber,blocksize=1024,inode_count):
	blockdevice = BlockDevice("blockdevice",block_count,True)
	buff = [magicnum] + [1024] + [block_count] + [inode_count] + [1, 2, 3, 0]
	packed_buff = numpy.packbits(buff)
	print(packed_buff)
	blockdevice.write_block(0,packed_buff)
	buff2 = ([1,1]+[0,0,0,0,0,0,|]+[0,0,0,0,0,0,0,0,|]*(block_count/8-8))[:-1] #added silly workaround to not print | at end of map

	packed_buff2 = numpy.packbits(buff2)
	print(packed_buff2)
	blockdevice.write_block(1,packed_buff2)
	buff3 = [0]*inode_count
	packed_buff3 = numpy.packbits(buff3)
	print(packed_buff3)
	blockdevice.write_block(1,packed_buff3)

	blockMap = ([True]*3)+([False]*100)

class BlockMap:

	def __init__(self):
		self.map = ([1,1]+[0,0,0,0,0,0,|]+[0,0,0,0,0,0,0,0,|]*(block_count/8-8))[:-1] 


	def alloc_block(self):
		i = 0
		for thing in self.map:
			if thing == 0:
				thing == 1
				return i
			elif thing == 1:
					i += 1
			else:
				pass

	def free_block(self,num):
		if num == 0 or 1 or 2:
			return ("You can't fucking do that!")
		else:
			i = 0
			for thing in self.map:
				if thing == | :
					pass
				else:
					if i == num:
						thing == 0
						return
					else:
						i += 1


class iNode:

	def alloc_inode(type):


	def free_inode(num):


	
