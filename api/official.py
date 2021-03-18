import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class Api_official():
    # 初始化 （baseurl+资源path）
    def __init__(self):
        # 定义  北京城市写字楼首页url
        self.url_office_beijing_index = api.Office_HOST + "/officebuilding/officebuilding/1/index"
        # log.info("正在初始化城市首页url:{}".format(self.url_official_beijing_index))
        # 定义   杭州城市写字楼首页url
        self.url_office_hangzhou_index = api.Office_HOST + "/officebuilding/officebuilding/2/index"
        # 定义   南京城市写字楼首页url
        self.url_office_nanjing_index = api.Office_HOST + "/officebuilding/officebuilding/8/index"
        # 定义  上海城市写字楼首页
        self.url_office_shanghai_index = api.Office_HOST + '/officebuilding/officebuilding/9/index'
        # 定义  成都写字楼首页
        self.url_office_chengdu_index = api.Office_HOST + "/officebuilding/officebuilding/15/index"
        # 定义  青岛写字楼首页
        self.url_office_qingdao_index = api.Office_HOST + "/officebuilding/officebuilding/21/index"
        # 定义 登录url
        self.url_office_login = api.Office_HOST + "/appapi/user/v1/loginbypwdecc"
        # log.info("正在初始化登录url：{}".format(self.url_official_login))
        # 定义地区列表url
        self.url_office_List_of_regions = api.Office_HOST + "/officebuilding/area/1/index"
        # log.info("正在初始化地区列表url:{}".format(self.url_official_List_of_regions))
        # 定义房源详情url
        self.url_office_Listing_details = api.Office_HOST + "/officebuilding/officebuilding/1/detail"
        # log.info("正在初始化办公房源详情url:{}".format(self.url_official_Listing_details))
        # 定义筛选url
        self.url_office_screen = api.Office_HOST + "/officebuilding/officebuilding/1/index"
        # log.info("正在初始化筛选url:{}".format(self.url_official_screen))
        # #定义 在线委托url
        # self.url_official_entrust = api.Official_HOST + "/officebuilding/area/getcityarea"
        # # log.info("正在初始化在线委托url:{}".format(self.url_official_entrust))
        # # 定义在线委托发送验证码url
        # self.url_official_Code = api.Official_HOST + "/appapi/user/v1/sendsms"
        # # log.info("正在初始化发送验证码:{}".format(self.url_official_Code))
        # 定义北京新房首页url
        self.url_newhouse_bj_index = api.Newhouse_HOST + "/home/index"
        # 定义杭州新房首页url
        self.url_newhouse_hz_index = api.Office_HOST + "/appapi/home/2/info"
        # 定义苏州新房首页url
        self.url_newhouse_sz_index = api.Office_HOST + "/appapi/home/5/info"
        # 定义太原新房首页url
        self.url_newhouse_ty_index = api.Office_HOST + "/appapi/home/6/info"
        # 定义天津新房首页url
        self.url_newhouse_tj_index = api.Office_HOST + "/appapi/home/7/info"
        # 定义南京新房首页url
        self.url_newhouse_nj_index = api.Office_HOST + "/appapi/home/8/info"
        # 定义上海新房首页url
        self.url_newhouse_sh_index = api.Office_HOST + "/appapi/home/9/info"
        # 定义成都新房首页url
        self.url_newhouse_cd_index = api.Office_HOST + "/appapi/home/15/info"
        # 定义南宁新房首页url
        self.url_newhouse_nn_index = api.Office_HOST + "/appapi/home/16/info"
        # 定义郑州新房首页url
        self.url_newhouse_zz_index = api.Office_HOST + "/appapi/home/18/info"
        # 定义无锡新房首页url
        self.url_newhouse_wx_index = api.Office_HOST + "/appapi/home/19/info"
        # 定义武汉新房首页url
        self.url_newhouse_wh_index = api.Office_HOST + "/appapi/home/20/info"
        # 定义青岛新房首页url
        self.url_newhouse_qd_index = api.Office_HOST + "/appapi/home/21/info"
        # 定义长沙新房首页url
        self.url_newhouse_cs_index = api.Office_HOST + "/appapi/home/22/info"
        # 定义南昌新房首页url
        self.url_newhouse_nc_index = api.Office_HOST + "/appapi/home/24/info"
        # 定义常州新房首页url
        self.url_newhouse_cz_index = api.Office_HOST + "/appapi/home/25/info"
        # 定义东莞新房首页url
        self.url_newhouse_dg_index = api.Office_HOST + "/appapi/home/99/info"

    # 北京城市写字楼首页接口
    def api_bj_office_index(self):
        # log.info("正在调用北京城市写字楼首页接口:{}".format(self.url_official_index))
        return requests.post(url=self.url_office_beijing_index)

    # 杭州城市写字楼首页接口
    def api_hz_office_index(self):
        return requests.post(url=self.url_office_hangzhou_index)

    # 南京城市写字楼首页接口
    def api_nj_office_index(self):
        return requests.post(url=self.url_office_nanjing_index)

    # 上海城市写字楼首页接口
    def api_sh_office_index(self):
        return requests.post(url=self.url_office_shanghai_index)

    # 成都城市写字楼首页接口
    def api_cd_office_index(self):
        return requests.post(url=self.url_office_chengdu_index)

    # 青岛城市写字楼首页接口
    def api_qd_office_index(self):
        return requests.post(url=self.url_office_qingdao_index)

    # 登录接口
    def api_login(self, loginname, password):
        data = {"loginname": loginname, "password": password}
        # log.info("正在调用登录接口：{} headers:{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_office_login, data=data, headers=api.headers)

    # 写字楼地区列表接口
    def api_office_List_of_regions(self):
        # log.info("正在调用地区列表接口:{} ".format(self.url_official_List_of_regions))
        return requests.post(url=self.url_office_List_of_regions)

    # 写字楼房源详情页
    def api_office_Listing_details(self, officeid, cityid):
        data = {"officeid": officeid, "cityid": cityid}
        # log.info("正在调用房源详情页接口:{}".format(self.url_official_Listing_details))
        return requests.post(url=self.url_office_Listing_details, data=data, headers=api.headers)

    # 写字楼区域筛选
    def api_office_screen(self, districtid, sqid, page=1, pcount=15):
        data = {"districtid": districtid, "sqid": sqid, "page": page, "pcount": pcount}
        # log.info("正在调用区域筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼地铁筛选
    def api_office_Metro_screening(self, lineid, stationid, page=1, pcount=15):
        data = {"lineid": lineid, "stationid": stationid, "page": page, "pcount": pcount}
        # log.info("正在调用地铁筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼价格筛选url
    def api_office_Price_screening(self, price, page=1, pcount=15):
        data = {"price": price, "page": page, "pcount": pcount}
        # log.info("正在调用价格筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼面积筛选url
    def api_office_Area_screening(self, buildarea, page=1, pcount=15):
        data = {"buildarea": buildarea, "page": page, "pcount": pcount}
        # log.info("正在调用面积筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼更多筛选url
    def api_office_More_screening(self, tag, decoratetype, page=1, pcount=15):
        data = {"tag": tag, "decoratetype": decoratetype, "page": page, "pcount": pcount}
        # log.info("正在调用更多筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼排序筛选url
    def api_office_Sort_filter(self, psort, page=1, pcount=1):
        data = {"psort": psort, "page": page, "pcount": pcount}
        # log.info("正在调用排序筛选接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 写字楼关键词搜索房源url
    def api_office_search(self, keyword, page=1, pcount=15):
        data = {"keyword": keyword, "page": page, "pcount": pcount}
        # log.info("正在调用搜索接口:{}".format(self.url_official_screen))
        return requests.post(url=self.url_office_screen, data=data, headers=api.headers)

    # 北京新房首页url
    def api_newhouse_bj_index(self, cityid):
        data = {"cityid": cityid}
        return requests.post(url=self.url_newhouse_bj_index, data=data, headers=api.headers)

    # 杭州新房首页url
    def api_newhouse_hz_index(self):
        return requests.post(url=self.url_newhouse_hz_index)

    # 苏州新房首页url
    def api_newhouse_sz_index(self):
        return requests.post(url=self.url_newhouse_sz_index)

    # 太原新房首页url
    def api_newhouse_ty_index(self):
        return requests.post(url=self.url_newhouse_ty_index)

    # 天津新房首页url
    def api_newhouse_tj_index(self):
        return requests.post(url=self.url_newhouse_tj_index)

    # 南京新房首页url
    def api_newhouse_nj_index(self):
        return requests.post(url=self.url_newhouse_nj_index)

    # 上海新房首页url
    def api_newhouse_sh_index(self):
        return requests.post(url=self.url_newhouse_sh_index)

    # 成都新房首页url
    def api_newhouse_cd_index(self):
        return requests.post(url=self.url_newhouse_cd_index)

    # 南宁新房首页URL
    def api_newhouse_nn_index(self):
        return requests.post(url=self.url_newhouse_nn_index)

    # 郑州新房首页url
    def api_newhouse_zz_index(self):
        return requests.post(url=self.url_newhouse_zz_index)

    # 无锡新房首页url
    def api_newhouse_wx_index(self):
        return requests.post(url=self.url_newhouse_wx_index)

    # 武汉新房首页url
    def api_newhouse_wh_index(self):
        return requests.post(url=self.url_newhouse_wh_index)

    # 青岛新房首页url
    def api_newhosue_qd_index(self):
        return requests.post(url=self.url_newhouse_qd_index)

    # 长沙新房首页url
    def api_newhouse_cs_index(self):
        return requests.post(url=self.url_newhouse_cs_index)

    # 南昌新房首页url
    def api_newhouse_nc_index(self):
        return requests.post(url=self.url_newhouse_nc_index)

    # 常州新房首页url
    def api_newhouse_cz_index(self):
        return requests.post(url=self.url_newhouse_cz_index)

    # 东莞新房首页url
    def api_newhouse_dg_index(self):
        return requests.post(url=self.url_newhouse_dg_index)
