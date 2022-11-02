import os

import requests
import json


def DownloadFiles(user_ID):
    folder_path = 'D:/Games/Osu/Songs/'
    r = requests.get(f'https://osu.ppy.sh/users/{user_ID}/scores/best?mode=osu&limit=100')
    data = json.loads(r.text)
    sz = len(data)
    k = 0
    for i in data:
        mapId = i['beatmap']['beatmapset_id']
        target_path = f"{folder_path}{mapId}.osz"
        if not os.path.exists(target_path):
            r = requests.get(f'https://kitsu.moe/api/d/{mapId}')
            f = open(f"{target_path}", "wb")
            f.write(r.content)
            f.close()
        else:
            print(f"{mapId} downloaded")
        k += 1
        print(k / sz)


if __name__ == '__main__':
    users_id = [7562902, 11367222, 6447454, 4504101, 7525949, 7512553, 9269034, 5339515, 6304246, 2291265]
    for i in users_id:
        DownloadFiles(i)
