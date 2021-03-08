# unzip encrypted files
# 解压加密压缩包zip到新目录
import zipfile,os

Sampledir = ""
NewSampleDir = ""

if not os.path.exists(NewSampleDir):
    os.makedirs(NewSampleDir)

for root, dirs, files in os.walk(Sampledir):
    for d in dirs:
        dirPath = os.path.join(root, d)
        newGroupDir = os.path.join(NewSampleDir, d)
        if not os.path.exists(newGroupDir):
            os.mkdir(newGroupDir)
        for i in os.listdir(dirPath):
            sampleAbsPath = os.path.join(dirPath, i)
            # unzip
            zf = zipfile.ZipFile(sampleAbsPath)
            list = zf.namelist()
            for f in list:
                zf.extract(f, newGroupDir, b"your pwd") # 

print "finish"
