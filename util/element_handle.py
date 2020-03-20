from io import BytesIO

# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
# 如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes

class Element_Handle(object):

    def ele(self):
        '''
        截图元素图片
        :return:
        '''
        element = self.driver.find_element_by_id('cn.xxxxxx:id/login_sign')
        pngbyte = element.screenshot_as_png
        image_data = BytesIO(pngbyte)
        img = Image.open(image_data)
        img.save('element.png')
        # 该方式能直接获取到登录按钮区域的截图