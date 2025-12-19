from scrape import scrape_main
from write import write_main

def main():
    #print("start main")

    # スクレイピングで取得したデータを２次元配列で取得
    article_list = scrape_main("TeckFundingNews")
    #print("len of article_list:", len(article_list))
    if len(article_list) == 0:
        print("error: article_list is empty")
        raise RuntimeError(
            "error: article_list is empty"
        )
        return

    # データをGoogle Sheetsに書き込む
    write_main("GoogleSpreadSheets", article_list)

if __name__ == "__main__":
    main()