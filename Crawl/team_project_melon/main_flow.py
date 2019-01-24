from bs4 import BeautifulSoup
import requests
import time
import random
import json
import melon_function as mf
import album
import song_rank as sr
import singer as s
import make_songsinger as ms


url = "http://vlg.berryservice.net:8099/melon/list"
trs = mf.request(url).select('tbody tr[data-song-no]')

album_lst = album.album_data(trs)

album_insert = "insert ignore into Album (album_id, album_title, album_genre, rating, releasedt, album_comp, entertainment) values (%s, %s, %s, %s, %s, %s, %s) "
mf.save(album_lst, album_insert)


songs = mf.song_data()
mssong_insert = "insert ignore into MS_Song (song_no, title, genre, album_id) values (%s, %s, %s, %s) "
mf.save(songs, mssong_insert)


rank_lst = sr.song_rank()
rank_insert = "insert into Song_Rank (song_no, rank, rankdt, likecnt) values (%s, %s, %s, %s) "
mf.save(rank_lst, rank_insert)


singer_id_lst = s.singer()
singer_insert = "insert ignore into Singer(artist_id, name) values(%s, %s)"
mf.save(singer_id_lst, singer_insert)


songsinger_data = ms.songsinger()
songsinger_insert = "insert ignore into SongSinger(song, singer) values(%s, %s)"
mf.save(songsinger_data, songsinger_insert)

