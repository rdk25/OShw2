from BlockDevice.py import *
from numpy import *

class FileSystem:



@staticmethod
def createFileSystem(filename,block_count,magicNumber,blocksize=1024,inode_count):
	blockdevice = BlockDevice("blockdevice",block_count,True)
	buff = [magicnum] + [1024] + [block_count] + [inode_count] + [1, 2, 3, 0]
	packed_buff = numpy.packbits(buff)
	ba = bytearray(packed_buff)
	print(packed_buff)
	blockdevice.write_block(0,ba)
	buff2 = ([1,1]+[0,0,0,0,0,0,|]+[0,0,0,0,0,0,0,0,|]*(block_count/8-8))[:-1] #added silly workaround to not print | at end of map
	packed_buff2 = numpy.packbits(buff2)
	ba2 = bytearray(packed_buff2)
	print(packed_buff2)
	blockdevice.write_block(1,packed_buff2)
	buff3 = [0]*inode_count
	packed_buff3 = numpy.packbits(buff3)
	ba3 = bytearray(packed_buff3)
	print(packed_buff3)
	blockdevice.write_block(1,ba3)

	blockMap = ([True]*3)+([False]*100)

class BlockMap:

	def __init__(self,blockdevice):
		self.blockdevice = blockdevice

	def alloc_block(self,blockdevice):
		PackedMap = self.blockdevice.read_block(1)
		Map = (numpy.unpackbits(PackedMap))[0]
		i = 0
		for thing in Map:
			if thing == 0:
				thing == 1
				packed_map = numpy.packbits(Map)
				self.blockdevice.write_block(1,packed_map)
				return i
			elif thing == 1:
					i += 1
			else:
				pass

	def free_block(self,num):

		if num == 0 or 1 or 2:
			return "You can't smegging do that!"
		else:
			PackedMap = self.blockdevice.read_block(1)
			Map = (numpy.unpackbits(PackedMap))[0]
			i = 0
			for thing in Map:
				if thing == |:
					pass
				else:
					if i == num:
						if thing == 0
							return "That block is already free!"
						else:
							thing == 0
							packed_map = numpy.packbits(Map)
							self.blockdevice.write_block(1,packed_map)
							return i
					else:
						i += 1

class iNode:

	def __init__(self):
		self.number 
		self.creationDate
		self.lastModDate
		self.flag
		self.permissions
		self.level
		self.blockNums

	def alloc_inode(type):



	def free_inode(num):



