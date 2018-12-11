# -*- coding:utf-8 -*-


class GetJsonParams(object):

    @classmethod
    def get_value(cls, my_dict: dict, key: str) -> str:
        """
        解析一个嵌套字典，并获取指定key的值

        :Args:
         - my_dict: 解析的字典,  DICT TYPE.
         - key: 指定解析的键,  SRT TYPE.

        :Usage:
            get_value({'hello': 'world'}, 'hello')
        """

        if isinstance(my_dict, dict):
            if my_dict.get(key) or my_dict.get(key) == 0 or my_dict.get(key) == ''\
                    and my_dict.get(key) is False or my_dict.get(key) == []:
                return my_dict.get(key)

            for my_dict_key in my_dict:
                if cls.get_value(my_dict.get(my_dict_key), key) or \
                                cls.get_value(my_dict.get(my_dict_key), key) is False:
                    return cls.get_value(my_dict.get(my_dict_key), key)

        if isinstance(my_dict, list):
            for my_dict_arr in my_dict:
                if cls.get_value(my_dict_arr, key) \
                        or cls.get_value(my_dict_arr, key) is False:
                    return cls.get_value(my_dict_arr, key)

    @classmethod
    def for_keys_to_dict(cls, *args: tuple, my_dict: dict) -> dict:
        """
        指定多个key，并获取一个字典的多个对应的key，组成一个新的字典

        :Arg:
         - args: 指定的key值, TUPLE TYPE.
         - my_dict: 解析的字典, DICT TYPE.

        :Usage:
            for_keys_to_do_dict('hello', {'hello': 'hello'})
        """
        result = {}
        if len(args) > 0:
            for key in args:
                result.update({key: cls.get_value(my_dict, str(key))})
        return result


if __name__ == '__main__':
    my_dicts = {
        "test_1_ip_api": {
            "url": "http://httpbin.org/ip",
            "assert": {
                "ResponseType": [
                    "type",
                    "dict"
                ],
                "origin": [
                    "type",
                    "str"
                ]
            },
            "method": "get",
            "params": "",
            "desc": "\u6d4b\u8bd5httpbin\u7684ip\u63a5\u53e3\u8fd4\u56de\u6b63\u5e38"
        },
        "test_2_headers_api": {
            "url": "http://httpbin.org/headers",
            "method": "get",
            "params": "",
            "headers": {
                "User-Agent": "BaiduSpider"
            },
            "assert": {
                "Connection": "close",
                "Host": "httpbin.org",
                "Accept-Encoding": "gzip, deflate",
                "User-Agent": "BaiduSpider"
            },
            "desc": "\u6d4b\u8bd5httpbin headers \u63a5\u53e3\u8fd4\u56de\u6b63\u5e38"
        },
        "test_3_post_api": {
            "url": "http://httpbin.org/post",
            "data": {
                "username": "Raymond",
                "password": "123456"
            },
            "method": "post",
            "desc": "\u6d4b\u8bd5httpbin/post\u63a5\u53e3\u7684\u8bf7\u6c42\u4e0e\u8fd4\u56de\u7ed3\u679c\u6b63\u786e",
            "assert": {
                "username": "Raymond",
                "password": "123456"
            }
        }
    }
    print(GetJsonParams.get_value(my_dicts, 'username'))
