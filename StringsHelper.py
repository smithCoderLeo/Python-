 # 从目录中提取字符串
    def parse_good_dir(self, dir):
        all_strings = Counter()
        all_imphashes = Counter()
        all_exports = Counter()

        for filePath in get_files(dir, self.goodNotRecursive):
            # Get Extension
            extension = os.path.splitext(filePath)[1].lower()
            if extension not in RELEVANT_EXTENSIONS and self.goodOnlyRelevantExtensions:
                if self.goodDebug:
                    print("[-] 扩展名不符合规范 %s - 跳过文件 %s" % (extension, filePath))
                continue

            # Size Check
            size = 0
            try:
                size = os.stat(filePath).st_size
                if size > (self.goodFs * 1024 * 1024):
                    print("")
                    continue
            except Exception as e:
                pass

            # Check and read file
            try:
                with open(filePath, 'rb') as f:
                    fileData = f.read()
            except Exception as e:
                print("[-] Cannot read file - skipping %s" % filePath)

            # 从文件中提取字符串
            strings = self.extract_strings(fileData)
            # 更新字符串数据库
            all_strings.update(strings)

            # Imphash and Exports
            (imphash, exports) = self.get_pe_info(fileData)
            all_exports.update(exports)
            all_imphashes.update([imphash])

        # return it as a set (unique strings)
        self.goodAllStrings = all_strings
        self.goodAllImphashes = all_imphashes
        return all_strings, all_imphashes, all_exports
