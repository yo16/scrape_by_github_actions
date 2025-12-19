"""
スクレイピングのメイン関数
２次元配列を返す
"""

from .sites.TeckFundingNews import scrape_tech_funding_news_list

def scrape_main(site_name):
    if site_name == "TeckFundingNews":
        category = "uk"  # for test
        
        article_list = scrape_tech_funding_news_list(category)
    else:
        raise ValueError(f"Invalid site name: {site_name}")
    #print(article_list)

    return article_list


