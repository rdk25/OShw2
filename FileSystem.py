from BlockDevice.py import *
from numpy import *

class FileSystem:

@staticmethod
def createFileSystem(filename,block_count,magicNumber,blocksize=1024,inode_count):
	blockdevice = BlockDevice("blockdevice",block_count,True)
	buff = [magicnum, 1024, block_count, inode_count, 1, 2, 3]
	packed_buf = numpy.packbits(buff)
	blockdevice.write_block(0,packed_buff)
