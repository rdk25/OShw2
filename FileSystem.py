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
	buff2 = [1,1]+[0,0,0,0,0,0,|]+[0,0,0,0,0,0,0,0,|]*(block_count/8-8)
	packed_buff2 = numpy.packbits(buff2)
	print(packed_buff2)
	blockdevice.write_block(1,packed_buff2)
	
