import os
import random

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# print(len(info_str))
# print(dict_1)
# print(dict_2)
# print(dict_3)


# dict_1 = to_dictionary('../char_std_5990.txt', 'gbk')
# dict_2 = to_dictionary('../text_info_results.txt', 'utf-8')

'''
1. 从文字库随机选择10个字符
2. 生成图片
3. 随机使用函数
'''


# 从文字库中随机选择n个字符
def sto_choice_from_info_str(info_str, quantity=10):
    start = random.randint(0, len(info_str) - 11)
    end = start + 10
    random_word = info_str[start:end]

    return random_word


def random_word_color():
    font_color_choice = [[54, 54, 54], [32, 32, 32], [75, 75, 75], [12, 12, 12]]
    font_color = random.choice(font_color_choice)

    noise = np.array([random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)])
    font_color = (np.array(font_color) + noise).tolist()

    # print('font_color：',font_color)

    return tuple(font_color)


# 生成一张图片
def create_an_image(bground_path, width, height):
    bground_list = os.listdir(bground_path)
    bground_choice = random.choice(bground_list)
    bground = Image.open(bground_path + bground_choice)
    # print('background:',bground_choice)
    # print(bground.size[0],bground.size[1])
    x, y = random.randint(0, bground.size[0] - width), random.randint(0, bground.size[1] - height)
    bground = bground.crop((x, y, x + width, y + height))

    return bground


# 选取作用函数
def random_choice_in_process_func():
    pass


# 模糊函数
def darken_func(image):
    # .SMOOTH
    # .SMOOTH_MORE
    # .GaussianBlur(radius=2 or 1)
    # .MedianFilter(size=3)
    # 随机选取模糊参数
    filter_ = random.choice(
        [ImageFilter.SMOOTH,
         # ImageFilter.SMOOTH_MORE,
         ImageFilter.GaussianBlur(radius=0.3)]
    )
    image = image.filter(filter_)
    # image = img.resize((290,32))

    return image


# 旋转函数
def rotate_func():
    pass


# 噪声函数
def random_noise_func():
    pass


# 字体拉伸函数
def stretching_func():
    pass


# 随机选取文字贴合起始的坐标, 根据背景的尺寸和字体的大小选择
def random_x_y(bground_size, font_size):
    width, height = bground_size
    # print(bground_size)
    # 为防止文字溢出图片，x，y要预留宽高
    x = random.randint(0, 2)
    y = random.randint(0, 2)

    return x, y


def random_font_size():
    # font_size = random.randint(24,27)
    font_size = random.randrange(15, 30, 2)  # 考虑不同大小的字体

    return font_size


def random_font(font_path):
    font_list = os.listdir(font_path)
    random_font = random.choice(font_list)

    return font_path + random_font


# 查找字体的最小包含矩形
class FindImageBBox(object):
    def __init__(self, ):
        pass

    def do(self, img):
        height = img.shape[0]
        width = img.shape[1]
        v_sum = np.sum(img, axis=0)
        h_sum = np.sum(img, axis=1)
        left = 0
        right = width - 1
        top = 0
        low = height - 1
        # 从左往右扫描，遇到非零像素点就以此为字体的左边界
        for i in range(width):
            if v_sum[i] > 0:
                left = i
                break
        # 从右往左扫描，遇到非零像素点就以此为字体的右边界
        for i in range(width - 1, -1, -1):
            if v_sum[i] > 0:
                right = i
                break
        # 从上往下扫描，遇到非零像素点就以此为字体的上边界
        for i in range(height):
            if h_sum[i] > 0:
                top = i
                break
        # 从下往上扫描，遇到非零像素点就以此为字体的下边界
        for i in range(height - 1, -1, -1):
            if h_sum[i] > 0:
                low = i
                break
        return (left, top, right, low)


def main(save_path, file, mobile_nums, word_id_dict, id_word_dict):
    # 随机选取10个字符
    # random_word = sto_choice_from_info_str(10)
    k = 0
    for num, mobile_num in enumerate(mobile_nums):
        # 字符转索引
        # c_arr = []
        # for c in mobile_num:
        #     c_arr.append(str(word_id_dict[c]) + "512859468")
        # mobile_num_index = "".join(c_arr)[:-1]

        # label_converter = strLabelConverter(alphabets.alphabet)
        # mobile_num_index,index_length = label_converter.encode(mobile_num)

        # 随机选取字体大小
        font_size = random_font_size()
        # 生成一张背景图片，已经剪裁好，宽高为32*280
        # raw_image = create_an_image('./background/', font_size * 6+20, font_size + 2)
        raw_image = create_an_image('./background/', 1000, font_size + 2)
        # raw_image = create_an_image('./background/', 245, font_size + 2)

        # 随机选取字体
        # font_name = random_font('./font/') zjb
        font_name = random_font('./font_more/')
        # 随机选取字体颜色
        font_color = random_word_color()

        # 随机选取文字贴合的坐标 x,y
        draw_x, draw_y = random_x_y(raw_image.size, font_size)

        # 将文本贴到背景图片
        font = ImageFont.truetype(font_name, font_size)
        draw = ImageDraw.Draw(raw_image)
        draw.text((draw_x, draw_y), mobile_num, fill=font_color, font=font)

        # 随机选取作用函数和数量作用于图片
        # raw_image = darken_func(raw_image)
        # raw_image = raw_image.rotate(0.2)
        # 保存文本信息和对应图片名称
        # with open(save_path[:-1]+'.txt', 'a+', encoding='utf-8') as file:
        file.write('%s.png\t%s\n' % (str(num), mobile_num))
        # file.write('%s.png\t%s\n' % (str(num), mobile_num_index))
        # 显示索引对应的字符，以便确认索引是否正确
        # file.write('%s.png %s\n' % (str(num),"".join([id_word_dict[int(id)] for id in mobile_num_index.split("-")])))
        # # 二值化
        raw_image_arr = np.array(raw_image)
        # raw_image_arr = cv2.cvtColor(raw_image_arr, cv2.COLOR_RGB2BGR)
        imagegray = cv2.cvtColor(raw_image_arr, cv2.COLOR_RGB2GRAY)
        raw_image_arr_bin = cv2.adaptiveThreshold(imagegray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                                  25, 6)

        img_obj = Image.fromarray(raw_image_arr_bin)
        raw_image_arr_bin = np.array(img_obj.rotate(0.1))

        # 查找字体的最小包含矩形
        find_image_bbox = FindImageBBox()
        cropped_box = find_image_bbox.do(raw_image_arr_bin)
        left, upper, right, lower = cropped_box
        raw_image_arr_bin = raw_image_arr_bin[upper: lower + 1, left: right + 1]

        if raw_image_arr_bin.shape[0] ==0:
            k += 1
            print("--------------------------------------已经有 %s 个图片的最小矩形宽度==0 ；font_name：%s, font_size:%s,content:%s" % (
            k, font_name, font_size,mobile_num))
            break

        if random.random() < 0.3 and raw_image_arr_bin.shape[0]>2:  # 一定概率添加点噪声
            for i in range(50):
                temp_x = np.random.randint(0, raw_image_arr_bin.shape[0] - 1)
                temp_y = np.random.randint(0, raw_image_arr_bin.shape[1] - 1)
                raw_image_arr_bin[temp_x][temp_y] = 255
                raw_image_arr_bin[temp_x + 1][temp_y] = 255
                raw_image_arr_bin[temp_x + 1][temp_y + 1] = 255
                raw_image_arr_bin[temp_x][temp_y + 1] = 255

        if random.random() < 0.3 and font_size >= 26:  # 一定概率腐蚀
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
            # raw_image_arr_bin = cv2.dilate(raw_image_arr_bin, kernel)
            raw_image_arr_bin = cv2.erode(raw_image_arr_bin, kernel)

        cv2.imwrite(os.path.join(save_path, '%s.png' % str(num)), raw_image_arr_bin)
        # raw_image.save(os.path.join(save_path, '%s.png' % str(num)))


def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]

    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]

    # 最后八位数字
    suffix = random.randint(9999999, 100000000)

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# 生成手机号
def get_nums(counts):
    mobile_nums = []
    for k in range(counts):
        phone = create_phone()
        print(phone)
        mobile_nums.append(phone)
    return mobile_nums


def to_dictionary(text_path='', code='utf-8'):
    with open(text_path, 'rb') as file:
        info_list = [part.decode(code, 'ignore').strip() for part in file.readlines()]
        string = ''.join(info_list)
        setting = set(string)
        dictionary_reverse = {value: key for key, value in enumerate(setting)}
        dictionary = {key: value for key, value in enumerate(setting)}
    return dictionary_reverse, dictionary


if __name__ == '__main__':
    # 处理具有工商信息语义信息的语料库，去除空格等不必要符号
    info_list = []
    with open('info.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for part in lines:
            # info_list.extend(part.split('\t'))
            info_list.extend(part.split())

    tv = "val_set_all"
    info_list = info_list[:1024]

    # tv = "train_set_all"
    # info_list = info_list[512:512 + 16384*16*2*4]
    # info_list = info_list[:1024]

    # _word_id_dict, _id_word_dict = to_dictionary('info.txt', 'utf-8')
    _word_id_dict, _id_word_dict = None, None

    # 图片标签
    file = open('data_set_all/%s.txt' % tv, 'w', encoding='utf-8')
    main('data_set_all/%s/' % tv, file, info_list, _word_id_dict, _id_word_dict)
    file.close()
