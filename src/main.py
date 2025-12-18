from scrape import scrape_main
from write import write_main

def main():
    # スクレイピングで取得したデータを２次元配列で取得
    article_list = scrape_main("TeckFundingNews")
    #print(article_list)

    # データをGoogle Sheetsに書き込む
    write_main("GoogleSpreadSheets", article_list)

if __name__ == "__main__":
    main()