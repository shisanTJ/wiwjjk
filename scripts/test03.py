import pytest

from api.official import Api_official
from tools.get_log import GetLog
from tools.read_txt import read_txt
from tools.send import sendmail

from tools.tool import Tools

log = GetLog.get_logger()


class Test_official:
    # 初始化
    def setup_class(self):
        # 获取ApiMp对象
        self.mp = Api_official()

    # 登录
    @pytest.mark.parametrize("user", read_txt("Personal_Center.txt"))
    def test01_official_login(self, user):
        # 调用登录方法
        r = self.mp.api_login(user[0], user[1])
        # # 提取token
        Tools.get_token(r)
        # 断言
        Tools.official_assert_common(r)
        log.info("登录断言成功")


    # # 城市北京写字楼首页
    def test02_office_bj_index(self):
        # 调用北京写字楼首页方法
        r = self.mp.api_bj_office_index()
        # 断言
        Tools.official_assert_common(r)
        log.info("北京写字楼首页接口正常")

    # 城市杭州写字楼首页
    def test03_office_hz_index(self):
        # 调用杭州写字楼首页方法
        r = self.mp.api_hz_office_index()
        # 断言
        Tools.official_assert_common(r)

    # 南京城市写字楼首页
    def test04_office_nj_index(self):
        # 调用南京写字楼首页方法
        r = self.mp.api_nj_office_index()
        # 断言
        Tools.official_assert_common(r)

    # 上海城市写字楼首页
    def test05_office_sh_index(self):
        # 调用上海写字楼首页方法
        r = self.mp.api_sh_office_index()
        # 断言
        Tools.official_assert_common(r)

    # 成都城市写字楼首页
    def test06_office_cd_index(self):
        # 调用成都写字楼首页方法
        r = self.mp.api_cd_office_index()
        # 断言
        Tools.official_assert_common(r)

    # 青岛城市写字楼首页
    def test07_office_qd_index(self):
        # 调用青岛写字楼首页方法
        r = self.mp.api_qd_office_index()
        # 断言
        Tools.official_assert_common(r)

    # 地区列表
    def test08_office_List_of_regions(self):
        # 调用地区列表接口
        r = self.mp.api_office_List_of_regions()

        # 断言
        Tools.official_assert_common(r)

    # 房源详情
    @pytest.mark.parametrize("Listing_details", read_txt("Listing_details.txt"))
    def test09_office_Listing_details(self, Listing_details):
        # 调用房源详情页接口
        r = self.mp.api_office_Listing_details(Listing_details[0], Listing_details[1])
        # 断言
        Tools.official_assert_common(r)

    # 区域筛选
    @pytest.mark.parametrize("screen", read_txt("screen.txt"))
    def test10_office_screen(self, screen):
        # 调用区域筛选接口
        r = self.mp.api_office_screen(screen[0], screen[1])
        # 断言
        Tools.official_assert_common(r)

    # 地铁筛选
    @pytest.mark.parametrize("metro", read_txt("metro.txt"))
    def test11_office_Metro_screening(self, metro):
        # 调用地铁筛选接口
        r = self.mp.api_office_Metro_screening(metro[0], metro[1])
        # 断言
        Tools.official_assert_common(r)

    # 价格筛选url
    @pytest.mark.parametrize("price", read_txt("price.txt"))
    def test12_office_Price_screening(self, price):
        # 调用价格筛选接口
        r = self.mp.api_office_Price_screening(price)
        # 有问题

        # 断言
        Tools.official_assert_common(r)

    # 面积筛选url
    def test13_office_Area_screening(self):
        # 调用面积筛选接口
        r = self.mp.api_office_Area_screening(buildarea=(0, 500))
        # 断言
        Tools.official_assert_common(r)

    # 更多筛选接口
    def test14_office_More_screening(self):
        # 调用更多筛选接口
        r = self.mp.api_office_More_screening(tag=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), decoratetype=(1, 2, 3, 4, 5))
        # 断言
        Tools.official_assert_common(r)

    # 排序筛选接口
    def test15_office_Sort_filter(self):
        # 调用排序筛选接口
        r = self.mp.api_office_Sort_filter(psort=0)
        # 断言
        Tools.official_assert_common(r)

    # 关键词搜索url
    @pytest.mark.parametrize("key_word", read_txt("Personal_Center.txt"))
    def test16_office_search(self, key_word):
        # 调用关键词搜索接口
        r = self.mp.api_office_search(keyword=key_word[0])
        Tools.official_assert_common(r)
        print(r.json())

    # 北京新房首页
    @pytest.mark.parametrize("cityid", read_txt("cityid.txt"))
    def test17_newhouse_bj_index(self, cityid):
        # 调用北京城市首页接口
        r = self.mp.api_newhouse_bj_index(cityid=cityid)
        # 断言
        Tools.official_assert_common(r, msg="", status=200)

    #
    # 杭州新房首页
    def test18_newhouse_hz_index(self):
        # 调用杭州城市新房首页接口
        r = self.mp.api_newhouse_hz_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 苏州新房首页
    def test19_newhosue_sz_index(self):
        # 调用苏州新房首页接口
        r = self.mp.api_newhouse_sz_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 太原新房首页
    def test20_newhosue_ty_index(self):
        # 调用太原新房首页接口
        r = self.mp.api_newhouse_ty_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 天津新房首页
    def test21_newhouse_tj_index(self):
        # 调用天津新房首页接口
        r = self.mp.api_newhouse_tj_index()

        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 南京新房首页
    def test22_newhouse_nj_index(self):
        # 调用南京新房首页接口
        r = self.mp.api_newhouse_nj_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 上海新房首页
    def test23_newhosue_sh_index(self):
        # 调用上海新房首页接口
        r = self.mp.api_newhouse_sh_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 成都新房首页
    def test24_newhouse_cd_index(self):
        # 调用成都新房首页接口
        r = self.mp.api_newhouse_cd_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 南宁新房首页
    def test25_newhouse_nn_index(self):
        # 调用南宁新房首页接口
        r = self.mp.api_newhouse_nn_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 郑州新房首页
    def test26_newhouse_zz_index(self):
        # 调用郑州新房首页接口
        r = self.mp.api_newhouse_zz_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 无锡新房首页
    def test25_newhouse_cd_index(self):
        # 调用无锡新房首页接口
        r = self.mp.api_newhouse_cd_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 武汉新房首页
    def test26_newhouse_wh_index(self):
        # 调用武汉新房首页接口
        r = self.mp.api_newhouse_wh_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 青岛新房首页
    def test27_newhouse_qd_index(self):
        # 调用成都新房首页接口
        r = self.mp.api_newhosue_qd_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 长沙新房首页
    def test28_newhouse_cs_index(self):
        # 调用长沙新房首页接口
        r = self.mp.api_newhouse_cs_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 南昌新房首页
    def test29_newhouse_nc_index(self):
        # 调用南昌新房首页接口
        r = self.mp.api_newhouse_nc_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 常州新房首页
    def test30_newhouse_cz_index(self):
        # 调用南昌新房首页接口
        r = self.mp.api_newhouse_cz_index()
        # 断言
        Tools.official_assert_common(r, msg="成功", status=200)

    # 东莞新房首页
    def test31_newhouse_dg_index(self):
        # 调用东莞新房首页接口
        r = self.mp.api_newhouse_dg_index()
        # 断言
        Tools.official_assert_common(r,msg="成功", status=200)


    # 发送邮件
    def test32_senmail(self):
        Tools.send_mail()

