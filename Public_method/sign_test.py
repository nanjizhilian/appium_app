import hashlib


def sign(sign_str=None):
    md5 = hashlib.md5()  # 创建md5对象
    sign_str = sign_str   # 要加密的对象
    sign_bytes_utf8 = sign_str.encode()  # 方法以 encoding 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。
    md5.update(sign_bytes_utf8)  # 进行加密
    sign_md5 = md5.hexdigest()  # 该方法只接受byte类型，否则会报错
    print(sign_md5)
    return sign_md5



