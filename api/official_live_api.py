import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class Api_official_live:
    # 初始化 （baseurl+资源path）
    def __init__(self):
        # 定义 看房现场url
        self.url_official_live = api.Official_HOST + "/appapi/livebroadcast/1/livelist"
        log.info("正在初始化看房现场url：{}".format(self.url_official_live))
        # 回放url
        self.url_official_playback = api.Official_HOST + "/appapi/livebroadcast/replaylog"
        log.info("正在初始化回放计数url:{}".format(self.url_official_playback))
        # 楼盘详情
        self.url_official_lp_details =api.Official_HOST+"/appapi/estate/1/detail"
        log.info("正在初始化楼盘详情url:{}".format(self.url_official_lp_details))
    # 看房 列表接口
    def api_official_live(self, businesstype):
        data = {"businesstype": businesstype}
        log.info("正在调用看房现场接口：{} headers:{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_official_live, json=data, headers=api.headers)
    # 回放接口
    def api_official_playback(self,roomid,secret,extra):
        data ={"roomid":roomid,"secret":secret,"extra":extra}
        log.info("正在调用回放接口:{}headers:{}".format(data,api.headers))
        # 调用接口
        return requests.post(url=self.url_official_playback,json=data,headers =api.headers)