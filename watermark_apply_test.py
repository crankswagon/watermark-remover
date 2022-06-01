from PIL import Image
import random


def add_text():
            TRANSPARENCY = random.randint(88, 97)

            image = Image.open('./dataset/watermark_test/000000000285.jpg')
            watermark = Image.open('./1.png')

            if watermark.mode!='RGBA':
                if watermark.mode == 'P': #palette mode has transparency expressed in bytes
                    watermark = watermark.convert('RGBA')
                else:
                    alpha = Image.new('L', watermark.size, 255)
                    watermark.putalpha(alpha)

            random_W = random.randint(-50 , 100)
            random_H = random.randint(-50 , 100)

            paste_mask = watermark.split()[3].point(lambda i: int(i * TRANSPARENCY / 100.))
            image.paste(watermark, (random_W , random_H ), mask=paste_mask)

            return image  #测试时请注释这一行 启用48行
            # return image  #训练模型时请注释这一行 启用47行


add_text().save("./dataset/watermark_test/000000000139_marked.jpg") 
