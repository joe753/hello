from bs4 import BeautifulSoup
import time


html = '''
<table>
    <tr>
        <th>회사</th>
        <th>A사</th>
        <th>B사</th>
        <th>C사</th>
    </tr>
    <tr>
        <th>주소</th>
        <td>서울</td>
        <td>강원도</td>
        <td>부산</td>
    </tr>
    <tr>
        <th>직원수</th>
        <td>30명</td>
        <td>55명</td>
        <td>200명</td>
    </tr>
    <tr>
        <th>전화번호</th>
        <td>02-2345-2323</td>
        <td>033-223-2323</td>
        <td>051-121-1212</td>
    </tr>
    <tr>
        <th>대표메일</th>
        <td>a@a.com</td>
        <td>b@b.com</td>
        <td>c@c.com</td>
    </tr>
</table>
'''

soup = BeautifulSoup(html, 'html.parser')


companies = {}
data = {}
for i , tr in enumerate(soup.select('tr')):
    if i == 0:
        for j, th in enumerate(tr.select('th')):
            if j == 0 : continue
            companies[th.text] = j - 1

    else : 
        item_name = tr.select_one('th').text
        lst = []
        for td in tr.select('td'):
            lst.append(td.text)
      
        data[item_name] = lst

print (companies,data)
time.sleep(5)


while True:
    ival = input ("회사와 아이템(종료:q)>>  ")
    ivals = ival.split(' ')

    comp = ival[0]
    item = ival[1]

    idx = companies[comp]
    print ("result is", data[item][idx])