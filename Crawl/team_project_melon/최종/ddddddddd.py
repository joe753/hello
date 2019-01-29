import re


url = "https://www.melon.com/artist/timeline.htm?artistId=752425"

pattern = re.compile("com/(.*)")
album_id = re.findall(pattern, url)

print (album_id)