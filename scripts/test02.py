import pytest

from api.agent_api import Api_agent

from tools.read_txt import read_txt
from tools import tool


class Test_agent:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = Api_agent()

    # 看房测试方法
    @pytest.mark.parametrize("brokerid,cityid",read_txt("key_word.txt"))
    def test01_mp_list(self,brokerid,cityid):
        # 调用看房列表方法
        r = self.mp.api_agent_list(brokerid,cityid)
        # # 提取token
        # tool.Tools.get_token(r)
        # 断言
        tool.Tools.agent_assert_common(r)


