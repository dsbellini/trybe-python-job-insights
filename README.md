# Boas-vindas ao repositório do Job Insights!

Neste projeto foram implementadas análises a partir de um conjunto de dados sobre empregos.

Os dados foram extraídos do site Glassdoor e obtidos através do Kaggle, uma plataforma disponiblizando conjuntos de dados para cientistas de dados.

<details>
<summary><strong>🚵 Habilidades utilizadas</strong></summary><br />   
<p>Utilizar o terminal interativo do Python.</p>
<p>Utilizar estruturas condicionais e de repetição.</p>
<p>Utilizar funções built-in do Python.</p>
<p>Utilizar tratamento de exceções.</p>
<p>Realizar a manipulação de arquivos.</p>
<p>Escrever funções.</p>
<p>Escrever testes com Pytest.</p>
<p>Escrever meus próprios módulos e importá-los em outros códigos.</p>
</details>


<details>
<summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate".

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>

<details>
  <summary><strong>🛠 Testes</strong></summary><br />

  Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

  ```bash
  $ python3 -m pytest
  ```