import asyncio
async def hello():
    print('hello world')
loop = asyncio.get_event_loop()  # 이벤트 루프를 얻음
loop.run_until_complete(hello())  # hello가 끝날때까지 기다림(코루틴객체 or 퓨처객체)
loop.close()


# await
import asyncio

async def add(a, b):
    print('add: {0} + {1}'.format(a, b))
    await asyncio.sleep(1.0)  # 1초 대기. assyncio.sleep도 네이티브 코루틴
    return a + b

async def print_add(a, b):
    result = await add(a, b)
    print('print_add : {0} + {1} = {2}'.format(a, b, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_add(1, 2))
loop.close()

#비동기 웹페이지 가져오기
## asyncio 사용 x
from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'orange']]

begin = time()
result = []
for url in urls:
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request)
    page = response.read()
    result.append(len(page))

print(result)
end = time()
print('실행시간: {0:.3f}초'.format(end - begin))

## asyncio 사용
from time import time
from urllib.request import Request, urlopen

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'orange']]

async def fetch(url):
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = await loop.run_in_executor(None, urlopen, request)
    page = await loop.run_in_executor(None, response.read)
    return len(page)

async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]  # 퓨쳐객체를 리스토로 만듦
    result = await asyncio.gather(*futures)  # 결과를 한꺼번에 가져옴
    print(result)

begin - time()
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
end = time()
print('실행시간 : {0.3f}초'.format(end - begin))