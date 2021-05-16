import py1337x

torrent = py1337x.py1337x()


def queryMessageContent(torrentId):
    response = torrent.info(torrentId=torrentId)
    genre = '\n\n'+', '.join(response['genre']) if response['genre'] else None
    description = '\n'+response['description'] if genre and response['description'] else '\n\n'+response['description'] if response['description'] else None
    msg = f"<b>✨ {response['name']}</b>\n{response['category']}\n{response['language']}\n {response['leechers']}{'<b>'+genre+'</b>' if genre else ''}{'<code>'+description+'</code>' if description else ''}\n\n<b>Magnet Link: </b><code>{response['magnetLink']}</code>"

    return msg
