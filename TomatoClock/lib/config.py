# -*- coding: utf-8 -*-
# Created: 3/9/2018
# Project : TomatoClock


from .kkLib import MetaConfigObj

class ProfileConfig(metaclass=MetaConfigObj):
    class Meta:
        __store_location__ = MetaConfigObj.StoreLocation.Profile

    donate_alerted = False
    ttc_current_version = ""


class UserConfig(metaclass=MetaConfigObj):
    class Meta:
        __store_location__ = MetaConfigObj.StoreLocation.MediaFolder
        __config_file__ = "_pomodore_config.json"

    report_recent_days = [7, 14, 30, 60, 180]
    LIVE_CODE_DOWNLOAD = True
    ANSWER_TIMEOUT_SECONDS = 30
    BREAK_MINUTES = {
        "10MIN": 2,
        "15MIN": 3,
        "20MIN": 4,
        "25MIN": 5,
        "50MIN": 10
    }
    SHOW_ANSWER_ON_CARD_TIMEOUT = True
    PLAY_SOUNDS = {
        "abort": True,
        "break": True,
        "half_way_limit": True,
        "start": True,
        "timeout": True,
    }
    SHOW_DECK_STATISTICS = True
    SHOW_OVERALL_STATISTICS = True
