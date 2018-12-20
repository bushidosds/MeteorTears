# -*- coding:utf-8 -*-
import unittest
from lib.public import wraps


class ChannelGetchildren(unittest.TestCase):

    """ChannelGetchildren接口测试脚本"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @wraps.cases_runner
    @wraps.result_assert
    def test_channel_getchildren(self, *args, **kwargs):
        """添加渠道数据"""
        response = kwargs.get('response')
        self.assertEqual(kwargs.get('expect_assert_value'), kwargs.get('kwassert_value'))