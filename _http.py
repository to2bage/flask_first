import requests


class HTTP:
    """ urilib or requests """
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # 符合restful的api要求返回json
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        #     pass
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ""
        #     pass
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text
    pass


if __name__ == '__main__':
    rect = HTTP.get("http://t.yushu.im/v2/book/isbn/9787501524044")
    print(rect)
    pass