# 遍历目录下的文件
sample_dir = ''
for root, dirs, files in os.walk(sample_dir):
    for file in files:
        abs_path = os.path.join(root, file)
