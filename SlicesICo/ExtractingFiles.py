import os
import shutil
# "C:/Users/Administrator/Desktop/teyse2/SlicesICo/apps-325622851583257.apps.fbsbx.com/instant-bundle/1991576137567926/2043282965790146/res/raw-assets"
PeerDirectory=os.path.split(os.path.realpath(__file__))[0]
print(PeerDirectory)
path=PeerDirectory
index=0
for root, dirs, files in os.walk(PeerDirectory):
	# print(dirs) #当前路径下所有子目录
	if index==0 and dirs[0]!="" :
		index=1
		path+="\\"+dirs[0]+"\\"
print(path)

def gci(filepath):
#遍历filepath下所有文件，包括子目录
	files = os.listdir(filepath)
	for fi in files:
		fi_d = os.path.join(filepath,fi)
		if os.path.isdir(fi_d):
			gci(fi_d)
		else:
			file=os.path.join(filepath,fi_d)
			_,extensionName=os.path.splitext(file)
			TargetDirectory=path+extensionName+"\\"
			if not os.path.exists(TargetDirectory):
				os.mkdir(TargetDirectory)
			shutil.copy(file,TargetDirectory)
			# os.remove(file)
gci(path)
print("完成")