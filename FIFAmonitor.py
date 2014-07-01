#coding: utf-8

__author__ = 'João Pedro <joopeeds@gmail.com>'

import urllib2, json, pynma, datetime


class MonitorFIFA():
    def __init__(self, winsound=False, android=False):
        self.game_code = "57"
        self.mykey = 'mykey'
        self.url = "https://fwctickets.fifa.com/TopsAkaCalls/Calls.aspx/getRefreshChartAvaDem?l=en&c=BRA"
        self.p = pynma.PyNMA(self.mykey)
        self.winsound = winsound
        self.android = android


    def update(self):
        response = urllib2.urlopen(self.url)
        ok = "OK" if response.getcode() == 200 else "BAD REQUEST"
        print "Update - " + ok + " " + str(datetime.datetime.now())
        resp = response.read()
        resp_dic = json.loads(resp)
        again = json.loads(resp_dic["d"]["data"])
        for each in again["BasicCodes"]["PRODUCTPRICES"]:
            if each["PRPProductId"] == "IMT" + self.game_code and each["PRPCategoryId"] in ["1", "2", "3", "4"] and \
                            each["Quantity"] != "0":
                if self.winsound:
                    import winsound
                    winsound.Beep(2000, 5000)
                if self.android:
                    self.p.push("FIFA Monitor", "Tickets available",
                            "The tickets for the game %s are available right now. Run!" % self.game_code)
                print "The tickets for the game %s are available right now. Run!" % self.game_code



while True:
    t = MonitorFIFA(winsound=True)
    t.update()