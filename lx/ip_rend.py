import socket


# 找出packagename和activity
import re
import subprocess


class ApkInfo():
    def __init__(self, apkPath):
        self.apkPath = apkPath

    def getApkBaseInfo(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)

        print('packagename:' + packagename)
        print('versionCode:' + versionCode)
        print('versionName:' + versionName)
        return packagename, versionName, versionCode


def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


if __name__ == '__main__':
    # print(get_host_ip())
    ApkInfo(r"/Users/liuwei/Downloads/x聊项目/测试服/X聊SDK版.apk").getApkBaseInfo()


