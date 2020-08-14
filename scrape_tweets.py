# -*- coding: utf-8 -*-
"""Neste script iremos em links da lista preprint_list.tsv, extraindo 
os tweets e os handles, no sentido de ter ao final uma dado tabular.
"""

from bs4 import BeautifulSoup as bsoup
from selenium import webdriver
import csv


def createHeadlessFirefoxBrowser():

    # Criação do navegador

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")
    return webdriver.Firefox(options=options)


def scrape_tweets(url):

    # Acessando página
    browser = createHeadlessFirefoxBrowser()
    browser.implicitly_wait(10)
    try:
        browser.get(url)
    except Exception:
        print(f"Não consegui raspar dessa url: {url}")
        browser.quit()
    else:
        # Raspando página
        paper_html = bsoup(browser.page_source, "html.parser")

        browser.quit()

        paper_title = paper_html.find("h1", {"id": "page-title"}).get_text()
        html_handles = paper_html.find_all("div", class_="handle")
        html_posts = paper_html.find_all("p", class_="summary")

        # Extraindo apenas o texto
        posts = [i.get_text() for i in html_posts]
        handles = [i.get_text() for i in html_handles]

        # Criando lista final
        paper_table = []
        for j in range(len(handles)):
            dict_atual = {
                "paper_link": url,
                "paper_title": paper_title,
                "handle": handles[j],
                "message": posts[j],
            }
            paper_table.append(dict_atual)

        return paper_table


def main(max_preprints=500):
    """max_preprints define o máximo de preprints da lista
    preprint_list que serão raspados. Altere caso deseje raspar mais ou menos."""

    with open("preprint_list.tsv", "r") as f:
        preprints = f.read().splitlines()

    # Raspando a página de cada preprint
    resultado_final = []
    for preprint in preprints[0:max_preprints]:
        try:
            atual = scrape_tweets(preprint)
            resultado_final.extend(atual)
        except Exception:
            pass

    # Escrevendo o dado final
    keys = resultado_final[0].keys()
    with open("data/preprint_tweets.csv", "w", newline="") as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(resultado_final)


if __name__ == "__main__":
    main()
