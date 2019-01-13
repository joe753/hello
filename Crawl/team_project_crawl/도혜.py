import requests
from bs4 import BeautifulSoup
import function

url = function.request_url("http://www.jobkorea.co.kr/Recruit/GI_Read/27349501?rPageCode=SL", "#gib_frame")
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
a = soup.select('div.artTplInner table')

# select 결과가 list라서 string화 함
k = a[0]

heads = k.select('th')
data = k.select('td')
dls = k.select('dl')

# ----------------------------주석 무시-----------------------------
# dls_s = str(dls).split(',')
# # print(data, "\n")
# # # print(dls, "\n")
# # for i in range(0, len(heads)):
# #     print(data[i])
# -----------------------------------------------------------------

# th랑 td랑 갯수가 같으니까(row 수) head 수만큼 loop 돌린다.
for i in range(0,len(heads)):
    a = heads[i].text
    b = data[i].text
    # 만일 data 안에 "dl"이 있을 때
    if 'dl' in str(data[i]):
        b = []
        # dt와 dd를 select 하고
        for dl in dls:
            dts = dl.select('dt')
            dds = dl.select('dd')
            # 각 dt당 dd의 수(len(dds))만큼 loopp를 돌리면서 dd를 가져온다.
            # 근데 여기서... 이 사이트는 dd의 갯수가 2라서 len(dds)-2까지만 돌렸는데 사실은 dds의 수만큼 돌아야 해서
            # 이것은 Fail임..
            for dt in dts:
                c = "==========={}======== {}  {}".format(dt.text, dds[len(dds)-2].text, dds[len(dds)-1].text)
                b.append(c)
    print("\n {} : {} \n".format(a, b))


    