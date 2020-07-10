"""
九宫格拼图
"""
from PIL import Image


def split_image():
    image = Image.open("test.JPG")
    width, height = image.size

    # 高和宽进行比较，较大的作为新图像的长度
    new_length = height if height > width else width

    # 创建一张正方形空图片，底色为白色
    new_image = Image.new(image.mode, (new_length, new_length), color="white")

    # 将要处理的图片粘贴到新创建的图片上，居中
    if height > width:
        new_image.paste(image, (int((new_length - width) / 2)), 0)
    else:
        new_image.paste(image, (0, int((new_length - height) / 2)))

    # 切割为三份
    new_length = int(new_length / 3)

    # 用来保存每一个切图
    box_list = []
    for i in range(0, 3):
        for j in range(0, 3):
            # 确定每个图片位置
            box = (j * new_length, i * new_length, (j + 1) * new_length, (i + 1) * new_length)  # (left, top, right, bottom)
            box_list.append(box)

    # 通过crop函数对图片进行切割
    image_list = [new_image.crop(box) for box in box_list]

    for (index, image) in enumerate(image_list):
        image.save(str(index) + ".png", "PNG")
    print("九宫格图片生成完毕！")


def main():
    split_image()


if __name__ == '__main__':
    main()