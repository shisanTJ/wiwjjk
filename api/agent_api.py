import api
import requests

from tools.get_log import GetLog

log = GetLog.get_logger()


class Api_agent:
    # 初始化 （baseurl+资源path）
    def __init__(self):
        # 讲房列表url
        self.url_agent_jiangfang = api.Agent_HOST + "/broker/livelist"
        log.info("正在初始化讲房列表url：{}".format(self.url_agent_jiangfang))
        # 直播历史列表接口url
        self.url_agent_live_history = api.Agent_HOST + "/broker/liverecordlist"
        log.info("正在初始化直播历史列表url:{}".format(self.url_agent_live_history))
        # 创建直播间接口
        self.url_agent_create_live = api.Agent_HOST + "/broker/liverecordlist"
        log.info("正在初始化创建直播间url:{}".format(self.url_agent_create_live))
        # 上传直播间接口
        self.url_agent_up_picture = api.Agent_HOST + "/image/upload"
        log.info("正在初始化上传图片url:{}".format(self.url_agent_up_picture))
        # 编辑直播间接口
        self.url_agent_live_edit = api.Agent_HOST + "/live/updateroom"
        log.info("正在初始化编辑直播间接口url:{}".format(self.url_agent_live_edit))
        # 删除直播间接口
        self.url_agent_live_delete = api.Agent_HOST + "/live/delroom"
        log.info("正在初始化删除直播间接口url:{}".format(self.url_agent_live_delete))
        # 发送消息鉴权接口
        self.url_agent_live_msg_authentication = api.Official_HOST + "/im/imauth"
        log.info("正在初始化发送消息鉴权接口url:{}".format(self.url_agent_live_msg_authentication))

    # 经纪人讲房 列表接口
    def api_agent_list(self, brokerid, cityid):
        data = {"brokerid": brokerid, "cityid": cityid}
        log.info("正在调用经纪人讲房列表接口：{} headers:{}".format(data, api.headers))
        # 调用post方法
        return requests.post(url=self.url_agent_jiangfang, json=data, headers=api.headers)
