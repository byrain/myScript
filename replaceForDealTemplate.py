import os


def modifyFile(filename):
	fp = open(filename,'rb')
	sourceList = []
	targetList = []
	targetString = ""
	content = ""
	lineNumber = 0
	for eachline in fp.readlines():
		sourceList.append(map(ord, eachline))
	fp.close()
	print sourceList
	for temp in sourceList:
		if lineNumber != len(sourceList) - 1:
			temp.remove(temp[-1])		
			temp.remove(temp[-1])
			lineNumber += 1
		targetList.append([1 if x == 124 else x for x in temp])
	targetList[0].remove(targetList[0][0])
	print targetList

	for eachline in targetList:
		for eachWord in eachline:
			 targetString += (chr(eachWord))

	open(filename,'wb').writelines(targetString)


def getFileName(folder):
	fileList = os.listdir(folder)
	for templateFile in fileList:
		filename = os.path.join(folder, templateFile)
		modifyFile(filename)


def main():
	getFileName(r"C:\byRainProgram\TRTN\Project\FXT\FIX_Matching_EMB_templates")
	# readFromFile(r"C:\byRainProgram\TRTN\Project\FXT\FIX_Matching_EMB_templates\FIX_Matching_EMB_SPOT_USDAED_PB-CP Buy2.txt")
	# print map(ord, "a test String: 12346")


if __name__ == '__main__':
	main()