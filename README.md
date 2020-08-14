# nobudgetsci-tweets

Códigos que utilizei pro projeto "Mapa de compartilhamento de preprints no Twitter", como parte da No Budget Science Hackweek de 2020. 
Não é o meu projeto principal durante a hackathon.

Todos os códigos deste repositório estão disponíveis para livre uso sob a licença MIT. 

# Para baixar os dados

* [Vá para este link](https://raw.githubusercontent.com/jvfe/nobudgetsci-tweets/master/data/preprint_tweets.csv)

* Clique com o botão direito do seu mouse e selecione "Salvar página como"

* O dado tem as seguintes colunas:
  
  * paper_link: O link do preprint.
  * paper_title: O título do preprint.
  * handle: O handle do twitter do usuário que compartilhou o preprint.
  * message: O texto da postagem do usuário - Essa informação muitas vezes tá cortada, por causa da forma pela qual a página carrega.

# Reproduzindo a extração de dados

* [Como instalar o gerenciador conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)

* Criando o ambiente a partir do arquivo environment.yml, digite no seu terminal:

```$ conda env create -f environment.yml```

* Uma vez instalado, ative o ambiente:

```$ conda activate nobudgetsci-tweets```

* Rode o *crawler* ou "raspador" - **Essa atividade leva bastante tempo, para mudar a quantidade de preprints que deseja raspar, altere o parâmetro "max_preprints" dentro de scrape_tweets.py.**

```$ python scrape_tweets.py```
