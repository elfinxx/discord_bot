from urllib.request import urlopen

from bs4 import BeautifulSoup


def get_upcoming_match():
    result = []
    html = urlopen("https://www.plusforward.net/")  # Insert your URL to extract
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    matchs = bs_obj.select("#matchticker > div.sidetable > a.siderow")

    i = 0
    for match in matchs:
        if i > 9:
            break

        flag = match.select("span.s_flag")[0]
        flag1 = match.select("span.s_flag")[1]
        if "Korea" in flag["title"] or "Korea" in flag1["title"]:
            result.append(("https://www.plusforward.net" + match['href'],
                           "`" + match.select("td")[0].text + "` vs `" + match.select("td")[1].text + "`",
                           match.select("span.date")[0].text))

        i = i + 1
    return result


def get_match_result():
    result = []
    html = urlopen("https://www.plusforward.net/")  # Insert your URL to extract
    bs_obj = BeautifulSoup(html.read(), 'html.parser')
    matchs = bs_obj.select("#matchticker > div.sidetable > a.siderow")

    for i in range(9, len(matchs)):
        match = matchs[i]
        flag = match.select("span.s_flag")[0]
        flag1 = match.select("span.s_flag")[1]
        if "Korea" in flag["title"] or "Korea" in flag1["title"]:
            result.append(("https://www.plusforward.net" + match['href'],
                           match.select("td")[0].text + " vs" + match.select("td")[1].text))

    return result
