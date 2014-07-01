#coding: utf-8

__author__ = 'João Pedro <joopeeds@gmail.com>'

import urllib2, json, pynma


class MonitorFIFA():
    def __init__(self):
        self.game_code = "57"
        self.mykey = 'mykey'
        self.url = "https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA"
        self.p = pynma.PyNMA(self.mykey)


    def update(self):
        self.p.push("FIFA Tickets", "Ticket available", "testing")
        response = urllib2.urlopen(self.url)
        resp = response.read()
        resp_dic = json.loads(resp)
        again = json.loads(resp_dic["d"]["data"])
        for each in again["BasicCodes"]["PRODUCTPRICES"]:
            if each["PRPProductId"] == "IMT" + self.game_code and each["PRPCategoryId"] in ["1", "2", "3", "4"] and \
                            each["Quantity"] != "-1":
                self.p.push("FIFA Monitor", "Tickets available",
                            "The tickets for the game %s are available right now. Run!" % self.game_code)


while True:
    t = MonitorFIFA()
    t.update()