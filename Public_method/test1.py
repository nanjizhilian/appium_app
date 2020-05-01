import pandas as pd
import os


XLSX_PATH = '../util/xlsx_test.xlsx'

# 读取前n行所有数据
def gain_n_all_data(xlsx_path,xlsx_head):
    """
    要闯入的参数详解：
    :param xlsx_path: 要传入xlsx的地址，默认会获取第一个sheel
    :param xlsx_head: 要传入行的参数，int类型
    :return:
    """
    """
    read_excel(xlsx_path)  # 读取xlsx的sheel值
    head(xlsx_head)       # 读取前7行的所有数据，dataFrame结构，注意获取的是前N行，
    values                #  #list形式，读取表格所有数据
    """
    Return_value_memory = []
    if type(xlsx_head) != int:
        print("贾维斯：抱歉先生您的参数类型不对")

    elif os.path.exists(xlsx_path) == False:    # 判断文件是否存在
        print("贾维斯：抱歉先生您传入的文件路径有误")
    else:
        xlsx_path_obj = pd.read_excel(xlsx_path)
        data1 = xlsx_path_obj.head(xlsx_head)
        data2 = xlsx_path_obj.values
        print("获取到所有title的值:\n{0}".format(data1))  # 格式化输出
        print("获取到所有的值:\n{0}".format(data2))  # 格式化输出
        Return_value_memory.append(data1)
        Return_value_memory.append(data1)
        return Return_value_memory


class XlsxData_Get():
    def xlsx_open(slef,xlsx_path=XLSX_PATH):
        """
        :param xlsx_path: xlsx 文件地址
        :return:
        """
        if os.path.exists(xlsx_path) == True:
            df = pd.read_excel(xlsx_path, keep_default_na=False)
            return df
        else:
            print("贾维斯：先生您的xlsx路径有误！！！")

    def xlsx_all_row(self,all_row):
        """
        :param all_row: 所有行
        :return:
        """
        xlop_obj = self.xlsx_open()
        if type(all_row) == int:
            data1 = xlop_obj.ix[all_row].values
            print("第%d行" % (all_row), "\n所有数据：\n{0}\n".format(data1))
            return data1
        else:
            print("贾维斯：先生您传行的类型不对！！要int类型")

    def row_column(self,row,column):
        """
        :param row: 行
        :param column:  列
        :return:
        """
        obj = self.xlsx_open()
        if type(row, column) == int:
            data2 = obj.ix[row, column]  # 读取指定行列位置数据
            print("第%d行 第%d列" % (row, column), "\n数据：\n{0}\n".format(data2))
            return data2
        else:
            print("贾维斯：类型错误：只要int类型")

    def Multiple_row_columns(self,n_row,N_row):
        """
        :param n_row: 第几行
        :param N_row: 第几行
        :return:
        """
        op_obj = self.xlsx_open()
        if type(n_row, N_row) == int:
            data3 = op_obj.ix[[n_row, N_row]].values  # 读取指定多行
            print("第%d行 or 第%d行" % (n_row, N_row), "\n数据：\n{0}\n".format(data3))
            return data3
        else:
            print("贾维斯：先生：类型错要int类型")

    def Specified_column_all_row(self,finger_column,all_n):
        """
        :param finger_column: 指定列
        :param all_n:   所有行
        :return:
        """
        obj = self.xlsx_open()
        if type(finger_column, all_n) == int:
            data4 = obj.ix[finger_column, [all_n]].values  # 读取指定列的所有行
            print("第%d行 第%d列" % (finger_column, all_n), "\n数据为\n{0}".format(data4))
            return data4
        else:
            print("贾维斯：先生类型错误")

    def Specified_key_values_all_row(self,row_n,title,data):
        """
        :param row_n: 第几行
        :param title:   标题
        :param data:    标题的内容
        :return:
        """
        df = self.xlsx_open()
        if type(row_n) == int and type(title,data) == str:
            data5 = df.ix[row_n, [title, data]].values  # 读取指定键值列的所有行（第几行的那个标题和那个标题的内容）
            return data5
        else:
            print("贾维斯：先生类型错误")


    def Operations(self,operation,Parameter1,Parameter2,Parameter3):
        if operation == "xlsx_all_row":
            self.xlsx_all_row(Parameter1)
        elif operation == "row_column":
            self.row_column(Parameter1,Parameter2)
        elif operation == "Multiple_row_columns":
            self.Multiple_row_columns(Parameter1,Parameter2)
        elif operation == "Specified_column_all_row":
            self.Specified_column_all_row(Parameter1,Parameter2)
        elif operation == "Specified_key_values_all_row":
            self.Specified_key_values_all_row(Parameter1,Parameter2,Parameter3)
        else:
            print("贾维斯：先生，参数不对")


if __name__ == '__main__':
    pass
