import os
import shutil

def renameAndCopy(absPath, targetFloder):
	if not os.path.isdir(targetFloder):
		os.makedirs(targetFloder)
	qflFile = targetFloder + "\\" +os.path.split(absPath)[1]
	vbsFile = qflFile[:-3] + "vbs"	
	if not os.path.exists(vbsFile):
		shutil.copy(absPath, targetFloder)
		os.rename(qflFile, vbsFile)


def getFile(originFolder, targetFloder):
	for  lists in os.listdir(originFolder):
		path = os.path.join(originFolder, lists)
		if ".qfl" in path:
			renameAndCopy(path, targetFloder)
		if os.path.isdir(path):
			getFile(path, targetFloder)


def main():
	getFile(r"C:\automated-testing\QTP\lib\TNS", r"C:\byRainProgram\TRTN\QFL_TO_VBS [QTP]")
	print "Done"


if __name__ == '__main__':
	main()