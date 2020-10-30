#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @DateTime: 2020/4/2 15:15

# print '({0}-{1})'.format(*[u'\u4e00', u'\u9fa5'])
# print ('hello {name1}  i am {name2}'.format(name1='Kevin', name2='Tom'))
#
# args = ['aa']
# kwargs = {'name1': 'tom', 'name2': 'jerry'}
# print 'hello {name1} {} i am {name2}'.format(*args, **kwargs)


# def add(a, b):
#     return a + b
#
#
# data = [1, 2]
# print add(*data)
# data = {'a': 3, 'b': 4}
# print add(**data)
#
# str()


def format_info_of_language(info):
    """根据语言类型返回相应语言信息"""
    return_info = info

    if isinstance(info, (str, unicode)):
        # 如果不全是字母,则直接使用该字符串 -- unicode的isalpha,中文会被判断为字母
        if not str(info).isalpha():
            return info
        else:
            return_info = __(info, 'zh-cn')

    elif isinstance(info, tuple):
        return_info = __(info[0], 'zn-cn')
        if not return_info:
            return_info = info[0]
        return_info = return_info % info[1:]

    return return_info


class LanguageUtils(object):
    """语言处理相关工具集"""

    @classmethod
    def check_default_lang(cls, app_id, check_obj=None):
        """检测目标对象是否包含了地区默认语言配置"""

        try:
            if not check_obj:
                return False

            if isinstance(check_obj, basestring):
                check_obj = eval(check_obj)

            default_lang = cls.get_default_lang(app_id)

            # 当前只检测字典和列表类型
            if isinstance(check_obj, dict):
                # in 判断要比 dict.has_key('key') 快, 且python3之后就没有has_key了
                return default_lang in check_obj.keys()
            elif isinstance(check_obj, list):
                # 当前暂不考虑列表元素类型不一致的情况，以后有需要再加
                if check_obj[0] and isinstance(check_obj[0], dict):
                    for element in check_obj:
                        if default_lang not in element.keys():
                            return False
                else:
                    return default_lang in check_obj
            return True

        except (SyntaxError, NameError):
            # 主要为了适配2.9版本check_obj可能为纯字符串的情况，3.0以后应根据业务需要，选择性的调用该方法。
            return True
        except Exception as e:
            err_msg = 'Language detection is abnormal:app_id:{app_id},check_obj:{obj},exception:{except_msg}'.\
                format(app_id=app_id, obj=check_obj, except_msg=e.message)
            return False

    @staticmethod
    def get_default_lang(app_id):
        """获取逻辑区域标识对应的默认语言"""
        return 'zh-cn'


if __name__ == '__main__':
    # json 语法规定 数组或对象之中的字符串必须使用双引号，不能使用单引号
    # 官网描述："A string is a sequence of zero or more Unicode characters, wrapped in double quotes, \
    # using backslash escapes"
    str_test1 = '{"en": "如月06号舰队en", "zh-cn": "如月06号舰队"}'
    str_test2 = "{'en': '如月06号舰队en', 'zh-cn': '如月06号舰队'}"
    str_test3 = '["zh-cn", "en", "zh-tw"]'
    str_test4 = '非多语言对象'
    str_test5 = u'11111'
    str_test6 = 'hello a'
    dict_test1 = {"en": "如月06号舰队en", "zh-cn": "如月06号舰队"}
    list_test1 = ["zh-cn", "en", "zh-tw"]
    list_test2 = [{'zh-cn': 1}, {'en': 2, 'zh-cn': 2}]
    list_test3 = []

    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test1)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test2)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test3)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test4)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test5)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=str_test6)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=dict_test1)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=list_test1)
    assert LanguageUtils.check_default_lang(app_id=1010, check_obj=list_test2)
    assert not LanguageUtils.check_default_lang(app_id=1010, check_obj=list_test3)


