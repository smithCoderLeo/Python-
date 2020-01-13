# 遍历目录下的文件
sample_dir = ''
for root, dirs, files in os.walk(sample_dir):
    for file in files:
        abs_path = os.path.join(root, file)
        with open(abs_path, 'r') as fr:

# 针对读取编码出错的读取方法
with open(file_path, 'rb') as fr:
    for v_str_line in fr:
        v_str_line = v_str_line.decode("utf-8", "ignore")
        print(v_str_line)
        
# 读取文件，存成字典，对字典按照值排序
def sort_file_size():
    sample_dir = '' # 待处理文件夹
    file_dict = {}
    for root, dirs, files in os.walk(sample_dir):
        for file in files:
            abs_path = os.path.join(root, file)
            size = os.path.getsize(abs_path)
            file_dict[abs_path] = size
    # 对字典按照值排序
    file_dict = sorted(file_dict.items(), key=lambda asd:asd[1], reverse=True)
    with open('sort_elephant_filename.txt', 'w', encoding='utf-8') as fw:
        for i in file_dict:
            fw.write(i[0])
            fw.write('\n')
