import codecs
import os

import chardet


def to_dictionary(text_path='', code='utf-8'):
	with open(text_path, 'rb') as file:
		info_list = [part.decode(code, 'ignore').strip() for part in file.readlines()]
		string = ''.join(info_list)
		setting = set(string)
		dictionary_reverse = {value : key for key, value in enumerate(setting)}
		dictionary = {key : value for key, value in enumerate(setting)}
	return dictionary_reverse,dictionary

# 转为UTF-8编码
def convert_encoding(data_root_dir):
    for file_name in os.listdir(data_root_dir):
        file_path = os.path.join(data_root_dir, file_name)
        with codecs.open(file_path, 'rb') as f:
            content = f.read()
            source_encoding = chardet.detect(content)['encoding']
            if source_encoding is None:
                print("未知的编码格式", file_name)
                return
            print("%s的原编码格式为：%s" % (file_name, source_encoding))
            if source_encoding != 'utf-8':
                with codecs.open(file_path, 'r', source_encoding) as frb:
                    content = frb.read()
                    with codecs.open(file_path, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        print("%s已转换" % file_name)
            else:
                print("%s文件的原格式是utf-8,无需转换" % file_name)

if __name__ == '__main__':
	convert_encoding("txt")