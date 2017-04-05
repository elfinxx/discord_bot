import asyncio
import json
from random import randrange

import discord
import requests
from discord.game import Game

from stream_check import get_live_streams
from upcoming import get_upcoming_match

host = 'irc.uriirc.org'
port = 16661
ssl = False

NICK = "바트"
CHANNEL = "#bart"

# 293243433277980683
# rK-NMqdvqS09V54wltbAzEMAIkRA5LAr

# bot token : MjkzMjQzNDMzMjc3OTgwNjgz.C7DvzA.Fxm6EDdJHPmirGmNga4HzE8pHK0
client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    command = message.content.split(' ')[0]

    if "포비아" in message.content:
        i = randrange(0, 100)
        print(i)
        if i > 90:
            await client.send_message(message.channel, "JOON(aka p) is king god emperor overwatch master..")

    if ("치선" in message.content or "호무라" in message.content) and "talk" not in message.content:
        i = randrange(0, 100)
        print(i)
        if i > 98:
            await client.send_message(message.channel, "프로방장러 치선 마스터님 내전 방좀 만들어주세여..")

    if command == '!?':
        print("ques")
        await client.send_message(message.channel, '! + `list`, `u` or `일정`,')

    elif command == "!live" or command == "!라이브":
        live_result = get_live_streams()
        live_result.sort(key=lambda tup: tup[0], reverse=True)
        return_text = "[스트리머 정보]\n\n"
        for tup in live_result:
            if tup[0] is True:
                return_text = return_text + "*LIVE* "
            return_text = return_text + "[" + tup[1] + "] " + tup[2] + "\n"

        await client.send_message(message.channel, return_text)

    elif command == '!u' or command == '!일정':
        result = get_upcoming_match()

        if len(result) == 0:
            await client.send_message(message.channel, "한국팀 경기 일정이 당분간 없습니다")
        else:
            return_text = "다가오는 경기 일정을 안내해드립니다.\n경기 중계는 아마도 http://www.twitch.tv/ogn_ow\n\n"
            for match in result:
                time_remaining = match[2].replace("m", "분").replace("h", "시간").replace("d", "일")

                if "시" in time_remaining or "분" in time_remaining:
                    return_text += match[1] + " 경기는 " + time_remaining + " 후에 시작합니다.\n"
                elif "Live" in time_remaining:
                    return_text += match[1] + " 경기는 지금 " + time_remaining + "! :heart_eyes:\n"
                else:
                    return_text += "\n"
            await client.send_message(message.channel, return_text)

    elif command == '!짤' or command == '!jj':
        jjals = requests.get('http://localhost:5000/api/jjals').json()
        i = randrange(len(jjals))
        await client.send_message(message.channel, jjals[i - 1])

    elif message.content.startswith('!짤등록') or message.content.startswith('!rj'):
        print(command)
        if len(message.content.split(' ')) < 2:
            await client.send_message(message.channel, "<짤등록 블라블라블라> 형식로 기억시킬 수 있습니다.")
        else:
            headers = {"Content-Type": "application/json"}
            jjal_str = message.content.replace('!짤등록 ', '').replace('!rj ', '')
            payload = {"content": jjal_str}
            print(payload)

            res = requests.post('http://localhost:5000/api/jjal', data=json.dumps(payload), headers=headers)
            print(res.content)
            await client.send_message(message.channel, jjal_str + " 외웠어요")

    elif message.content.startswith('!call'):
        await client.send_message("hi")

    elif message.content.startswith('!who'):
        members = client.get_all_members()
        in_game = "현재 오버워치 하시는 분들입니다.\n"
        for user in members:
            game_name = str(user.game)
            if game_name == "Overwatch":
                in_game = in_game + "\n" + user.name

        await client.send_message(message.channel, in_game)

    elif message.content.startswith('!list'):
        await client.send_message(message.channel,
                                  "사용자 데이터는 다음 구글 시트 문서에서 제공됩니다.\n" + 'https://docs.google.com/spreadsheets/d/1D63gLoHAt2l_yaW-F47pkjsqq-82JlGKZ5wXolEj-fI/edit#gid=2027227396')

    elif message.content.startswith('!play'):
        game_name = message.content.replace('!play ', '')
        await client.change_presence(game=discord.Game(name=game_name))



client.run('MjkzMjQzNDMzMjc3OTgwNjgz.C7DvzA.Fxm6EDdJHPmirGmNga4HzE8pHK0')
