#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tools
from plugins import jianshu
from plugins import github
from plugins import other


class Iptv (object):
    def __init__(self):
        self.T = tools.Tools()

    def run(self):
        # jianshuList = jianshu.Source()
        # urlList = jianshuList.getSource()
        # for item in urlList:
        #     print(item)
        # GitHub = github.Source()
        # urlList = GitHub.getSource()
        # for item in urlList:
        #     print(item)
        Other = other.Source()
        urlList = Other.getSource()
        for item in urlList:
            print(item)


if __name__ == '__main__':
    obj = Iptv()
    obj.run()
