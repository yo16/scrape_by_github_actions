"""
Tech Founding Newsのスクレイピング
"""

import requests
from bs4 import BeautifulSoup
import urllib3

# SSL証明書の警告を無効化
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://techfundingnews.com/"
CATEGORIES = [
    "uk",
    "europe",
    "us",
    "vc",
    "AI"
]

# ブラウザのヘッダーを設定
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Cache-Control": "max-age=0",
}


def scrape_tech_funding_news_list(category):
    print(f"start scraping {category}")

    article_list = []

    response = requests.get(f"{BASE_URL}category/{category}", headers=HEADERS, verify=False)
    
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup.prettify())

    # selector:
    # #primary > div.cs-posts-area.cs-posts-area-posts > div.cs-posts-area__outer > div > article
    articles = soup.select("main #primary > div.cs-posts-area.cs-posts-area-posts > div.cs-posts-area__outer > div > article")
    #print(f"found {len(articles)} articles")
    for i, article in enumerate(articles):
        print(f"found article {i+1}")
        div_content = article.select_one("div.cs-entry__outer > div.cs-entry__inner.cs-entry__content")
        if div_content:
            # 取得する情報の初期化
            tag_texts = []
            article_tags = ""
            article_title = ""
            article_url = ""
            article_summary = ""
            article_date = ""

            # タグを取得
            tag_lis = div_content.select("div.cs-entry__post-meta:first-child ul.post-categories > li")
            if tag_lis:
                tag_texts = [li.text for li in tag_lis]

            # タイトルを取得
            title_elem = div_content.select_one("h2.cs-entry__title")
            link_elem = div_content.select_one("h2.cs-entry__title > a")
            if title_elem and link_elem:
                article_title = title_elem.text
                article_url = link_elem["href"]
            
            # 記事の要約を取得
            summary_elem = div_content.select_one("div.cs-entry__excerpt")
            if summary_elem:
                # トリムして取得
                article_summary = summary_elem.text.strip()
            
            # 記事の日付を取得
            date_elem = div_content.select_one("div.cs-entry__post-meta > div.cs-meta-date")
            if date_elem:
                article_date = date_elem.text
            
            #print(f"article_title: {article_title}")
            #print(f"article_url: {article_url}")
            #print(f"article_summary: {article_summary}")
            #print(f"article_date: {article_date}")
            #print(f"tag_texts: {tag_texts}")

            # タグは、カンマ区切りの文字列で取得
            article_tags = ", ".join(tag_texts)
            article_list.append([
                article_title,
                article_url,
                article_summary,
                article_date,
                article_tags
            ])
    
    # 2次元配列を返す
    return article_list


if __name__ == "__main__":
    category = CATEGORIES[0]    # for test
    article_list = scrape_tech_funding_news_list(category)
    print(article_list)

