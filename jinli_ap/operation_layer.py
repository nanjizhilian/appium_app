import re
import os


APP_PATH = '/Users/Downloads/app.apk'


# 测试的包的路径和包名
def apk_path(APP_PATH):
    appLocation = APP_PATH  # " /Users/Downloads/app.apk "
    return appLocation


# 读取设备 id   popen接收三个参数 第一个参数是使用的命令，第二个是，模式权限可以是 'r'(默认) 或 'w'。
def equipment_id():
    """
    :param adb:         command -- 使用的命令。
    :param mode:        模式权限可以是 'r'(默认) 或 'w'。
    :param buffring:    指明了文件需要的缓冲大小：0意味着无缓冲；
                        1意味着行缓冲；其它正值表示使用参数大小的缓冲
                        （大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，
                        一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。
                        如果没有改参数，使用系统的默认值。
    :return:
    """
    readDeviceId = list(os.popen('adb devices').readlines())
    return readDeviceId

# 正则表达式匹配出 id 信息
def re_id():
    readDeviceId = equipment_id()
    deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
    print("贾维斯：\t >>先生设备id为:", deviceId)


# 读取设备系统版本号
def system_version_number():
    deviceAndroidVersion = list(os.popen('adb shell getprop ro.build.version.release').readlines())
    deviceVersion = re.findall(r'^\w*\b', deviceAndroidVersion[0])[0]
    print("贾维斯：\t >>> sir系统版本号为:", deviceVersion)
    return deviceVersion


# 读取 APK 的 package 信息
def read_apk():
    appLocation = apk_path()
    appPackageAdb = list(os.popen('aapt dump badging ' + appLocation).readlines())
    appPackage = re.findall(r'\'com\w*.*?\'', appPackageAdb[0])[0]
    print("贾维斯：sir:package的信息为：", appPackage)
    return appPackage

# 删除以前的安装包
def delete_apk():
    appPackage = read_apk()
    os.system('adb uninstall ' + appPackage)

