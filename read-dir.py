# 遍历目录下的文件
sample_dir = ''
for root, dirs, files in os.walk(sample_dir):
    for file in files:
        abs_path = os.path.join(root, file)
        with open(abs_path, 'r') as fr:

# 针对读取是编码出错的读取方法
with open(file_path, 'rb') as fr:
    for v_str_line in fr:
        v_str_line = v_str_line.decode("utf-8", "ignore")
        print(v_str_line)
