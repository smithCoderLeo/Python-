# 统计opcode出现的频率
for i in os.listdir(PATH)[:1000]:
	row = [0]*(len(headers)-1)
	file = os.path.join(PATH, i)
	# row[0] = file
	if os.path.isfile(file):
		row[0] = file
		call('objdump -M intel -D ' + file[2:] + ' > hello.txt', shell=True)
		with open('hello.txt', 'r') as f:
			for l in f:
				if ':' in l:
					# print l
					for i, opcode in enumerate(opcodes_list):
						if opcode in l:
							row[i+1] += 1
		row.append('?')
		with open("check.csv", "a") as csv_file:
			writer = csv.writer(csv_file, delimiter=',')
			writer.writerow(row)
