# 定位元素封装
from ui_appium.jinli import stop_app
from handle.user_data import user_data


class To_elemenT_Location():

    def __init__(self):
        self.get_appium_obj = stop_app()
        self.get_server = self.get_server.get_driver()

    def ElemenT(self,Location,Location_element):
        if Location == "ClassName":
            class_name = self.get_server.find_element_by_Class_name(Location_element)
            return class_name
        elif Location == "Id":
            Id = self.get_server.find_element_by_id(Location_element)
            return Id
        elif Location == "xpath":
            XPATH = self.get_server.find_element_by_xpath(Location_element)
            return XPATH
        elif Location == "text":
            Text = self.get_server.find_elements_by_link_text(Location_element)
            return Text
        elif Location == "css_selector":
            css_selector = self.get_server.find_element_by_css_selector(Location_element)
            return css_selector
        else:
            print("贾维斯：\t>>> 先生您的定位方法有误")
        return self.ElemenT


