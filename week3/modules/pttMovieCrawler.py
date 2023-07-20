# 爬取 PTT 電影板
import urllib.request as request
import re
import bs4
import ssl

context = ssl._create_unverified_context()

dataPool = []
# 先抓取到目前的頁數有多少
domain = "https://www.ptt.cc"
req = request.Request(domain + "/bbs/movie/index.html", headers={
  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
})
with request.urlopen(req, context=context) as res:  
  data = res.read().decode("utf-8")
  html = bs4.BeautifulSoup(data, "html.parser")
  previousPage = html.find_all("a", class_="btn wide")[1]["href"] # /bbs/movie/index9614.html
  pageNums = int(re.search(r"/bbs/movie/index(\d+)\.html", previousPage).group(1)) + 1

# 抓取到單一頁面的方法
def getData(i):
  # 抓取主頁資訊
  req = request.Request(f"{domain}/bbs/movie/index{'' if i == 0 or None else pageNums - i}.html", headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
  })
  with request.urlopen(req, context=context) as res:  
    data = res.read().decode("utf-8")
    html = bs4.BeautifulSoup(data, "html.parser")
    posts = html.find_all("div", class_="r-ent")
    with open("movie.txt", mode="w", encoding="utf-8") as file:  
      for post in posts:
        # 於主頁抓取 title
        titleLink = post.find("div", class_="title").a
        if titleLink == None:
          title = None  
        else:
          title = titleLink.string
        
        # 於主頁抓取 nrec
        nrec = post.find("div", class_="nrec").span
        if nrec == None:
          nrec = '0'
        else:
          nrec = nrec.string

        # 於主頁抓取各篇文章的 url（該文章存在才處理）
        if titleLink != None:
          postUrl = domain + titleLink["href"]
          # 進入各文章抓取日期資訊
          req = request.Request(postUrl, headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.15"
          })
          with request.urlopen(req, context=context) as res:
            data = res.read().decode("utf-8")
            html = bs4.BeautifulSoup(data, "html.parser")
            time = html.find_all("span", class_="article-meta-value")[3].string
            dict = {
              "title": title,
              "nrec": nrec,
              "time": time
            }
            dataPool.append(dict)

def crawl(pageNum):
  for i in range(0, pageNum):
    getData(i)
  with open("movie.txt", mode="w", encoding="utf-8") as file:
    for data in dataPool:
      file.write(f"{data['title']}, {data['nrec']}, {data['time']}\n")
