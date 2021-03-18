import pytest

from api.official_live_api import Api_official_live

from tools.read_txt import read_txt
from tools import tool


class Test_official:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = Api_official_live()

    # 看房测试方法
    @pytest.mark.parametrize("businesstype",read_txt("Personal_Center.txt"))
    def test01_mp_list(self,businesstype):
        # 调用看房列表方法
        r = self.mp.api_official_live(businesstype)
        # # 提取token
        # tool.Tools.get_token(r)
        # 断言
        tool.Tools.official_assert_common(r)


