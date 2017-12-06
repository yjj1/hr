# -*- coding:'utf8' -*-
#encoding=utf-8
from bs4 import BeautifulSoup
def trans_xml_to_dict(xml):
    """
    :param xml: 原始 XML 格式数据
    :return: dict 对象
    """

    soup = BeautifulSoup(xml, features='xml')
    xml = soup.find('xml')
    if not xml:
        return {}

    # 将 XML 数据转化为 Dict
    data = dict([(item.name, item.text) for item in xml.find_all()])
    return data