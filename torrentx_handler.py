# (c) @AbirHasan2005 & Hemanta Pokharel & The Anon Cat

import py1337x

torrent = py1337x.py1337x()


def queryMessageContent(torrentId):
    response = torrent.info(torrentId=torrentId)
    genre = '\n\n'+', '.join(response['genre']) if response['genre'] else None
    description = '\n'+response['description'] if genre and response['description'] else '\n\n'+response['description'] if response['description'] else None
    msg = f"<b>✨ {response['name']}</b>\n\n<b>Category:</b> <code>{response['category']}</code>\n<b>Language:</b> <code>{response['language']}</code>\n<b>Seeders:</b> <code>{response['seeders']}</code>\n<b>Leechers:</b> <code>{response['leechers']}</code>\n<b>Size:</b> <code>{response['size']}</code>\n<b>Downloads:</b> <code>{response['downloads']}</code>\n<i>Uploaded: {response['uploadDate']}</i>\n<i>Last Checked {response['lastChecked']}</i>\nUploaded by <b>{response['uploader']}</b>{'<b>'+genre+'</b>' if genre else ''}{'<code>'+description+'</code>' if description else ''}\n\n<b>Magnet Link:</b>\n<code>{response['magnetLink']}</code>"

    return msg
