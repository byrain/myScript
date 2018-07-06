#coding=utf-8
import sys,os,stat

defaultParameters = {
		"DB_SID":"fixgwyun",
		"DB_Username":"test",
		"DB_Listener":"OracleOraDb10g_home1TNSListener",
		"DB_Service":"OracleServiceFIXGWYUN",
		"AUTO_HOME":".\Automation\FIXGatewayAutomation_Aegisoft\PLSQL",
		"EXEC_HOME_Parent":".\\Automation\\FIXGatewayAutomation_Aegisoft\\3.5.1.1_FIX_Automation\\3511",
		"EXEC_HOME":"%EXEC_HOME_Parent%\\%TEST_Name%",
		"AegiSoft":''' ".\\TRTN\Aegisoft\\" ''',

		"V_SOURCE_ID":"publisher32LBN1",
		"main_group_name":"R321",
		"counter_group_name":"R321",
		"main_name":"receiver32LBN1FDC"
		}
		
def getFilename(rootDir):
	for lists in os.listdir(rootDir):
		path = os.path.join(rootDir,lists)
		if os.path.isdir(path):
			getFilename(path)
		elif (os.path.splitext(path)[1] == ".bat"):
			modifyBatFile(path)

def modifyBatFile(filename):
	fp = open(filename) 
	listConetent = []
	for i in fp.readlines():	
		listConetent.append(i)
	fp.close()
	content = ""
	eleName = ""
	eleValue = ""
	for i in listConetent:
		try:
			eleName = i.split("=")[0].split(" ")[1]
			eleValue = i.split("=")[1]
		except Exception, e:
			pass
		if eleName in defaultParameters:
			# i = i.split("=")[0] + "=" + defaultParameters[eleName]
			# eleName = ""
			i = i.replace(eleValue,defaultParameters[eleName])
		if len(i) > 1:
			content = content + i + "\r\n"
	open(filename,'wb').writelines(content)

def main():
	rootDir = os.getcwd()
	getFilename(rootDir)

if __name__ == '__main__':
	main()
