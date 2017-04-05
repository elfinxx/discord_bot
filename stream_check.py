import urllib

import requests
from bs4 import BeautifulSoup


def get_list():
    return [("최치선의 오버워치", "https://www.youtube.com/channel/UC6A64-_olxbJdFz6h-b-xLw"),
            ("Mako의 오버워치", "https://www.youtube.com/channel/UC6VhuVd58L8Wogun1e8eWHA"),
            ("OGN 오버워치", "https://www.twitch.tv/ogn_ow"),
            ("위자드형", "https://www.twitch.tv/wizardhyeong"),
            ("바트워치", "https://www.youtube.com/channel/UC5tZ01703qpXPxhSWKixuoQ")]


def get_live_streams():
    msg = []
    stream_list = get_list()

    for stream_name, stream_url in stream_list:
        if "youtube.com" in stream_url:
            page = urllib.request.urlopen(stream_url).read()
            soup = BeautifulSoup(page, "lxml")
            els = soup.select("div.yt-lockup-badges")

            is_live = False

            for e in els:
                if "스트리밍" in e.text:
                    is_live = True
                    break
            msg.append((is_live, stream_name, stream_url))


        else:
            channel_name = stream_url.replace("https://www.twitch.tv/", "")
            req_url = "https://api.twitch.tv/kraken/streams/" + channel_name + "?client_id=0vxh1ovcs87rwkmm0il60punn0bl1d"
            res = requests.get(req_url).json()
            is_live = False
            if res['stream'] is not None:
                is_live = True

            msg.append((is_live, stream_name, stream_url))

    return msg
