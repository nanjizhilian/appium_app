import requests,json
def treasurebox():
    url = "http://47.103.100.111:8094/v1/chatroom/treasurebox/join/&token=72835d3b81a25ec07cf6de9fdaec3455"
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    request_param = {
        "userid": 430093063176720384,
        "roomid": 430418677263896576,
        "boxId": 100,
        "bizid": 4130548091433820161581996099,
    }
    response = requests.post(url, data=json.dumps(request_param), headers=headers)
    print(response.text)


if __name__ == '__main__':
    treasurebox()


