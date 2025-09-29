# 📑 Sistema de Recomendação de Filmes com Login e Cadastro

##  Visão Geral

Este sistema é uma aplicação de **recomendação de filmes** utilizando **AutoEncoder (TensorFlow/Keras)** e persistência de dados com **SQLite**.
A interface foi desenvolvida em **Tkinter (Python GUI)**, permitindo **cadastro e login de usuários** e apresentando recomendações personalizadas.

---

##  Tecnologias Utilizadas

* **Python 3.12+**
* **Bibliotecas**:

  * `pandas` – manipulação de dados
  * `numpy` – operações numéricas
  * `sqlite3` – banco de dados relacional local
  * `tkinter` – interface gráfica
  * `scipy` – estrutura de matrizes esparsas
  * `scikit-learn` – divisão de dados (train/test)
  * `tensorflow.keras` – construção e treino do AutoEncoder

---

##  Estrutura do Projeto

```
sistematcc/
│── usuarios.db          # Banco SQLite criado automaticamente
│── movies.csv           # Dataset de filmes (MovieLens)
│── ratings.csv          # Dataset de avaliações (MovieLens)
│── sistema.py           # Script principal
```

---

##  Banco de Dados

O sistema usa **SQLite** com uma tabela `usuarios`:

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);
```

* Cada usuário é identificado pelo `email`.
* As credenciais são armazenadas localmente no arquivo `usuarios.db`.

---

##  Datasets

O sistema utiliza os arquivos do **MovieLens Small Dataset** (100k ratings).
Arquivos necessários (colocar na mesma pasta do script):

* `movies.csv` → informações sobre os filmes
* `ratings.csv` → avaliações de usuários

Fonte: [MovieLens Dataset](https://grouplens.org/datasets/movielens/)

---

##  Funcionamento do AutoEncoder

1. Carrega os ratings de usuários e transforma em **User-Item Matrix**.
2. Treina um **AutoEncoder** para aprender representações latentes dos usuários.
3. Ao logar, o sistema gera **recomendações personalizadas** para o usuário ativo.

---

##  Interface Gráfica (Tkinter)

### 🔹 Tela Inicial

* Opções: **Login** ou **Cadastro**

### 🔹 Tela de Cadastro

* Campos: Nome, Email, Senha
* Armazena usuário em `usuarios.db`

### 🔹 Tela de Login

* Autentica usuário
* Se válido → abre **Tela de Recomendações**

### 🔹 Tela de Recomendações

* Lista de **filmes recomendados**
* Filtros:

  * **Gênero** (campo de texto, busca parcial)
  * **Autor** (não utilizado no MovieLens, mas presente no código para expansão futura)

---

##  Fluxo de Uso

1. Execute no terminal:

   ```powershell
   python sistema.py
   ```
2. Na interface:

   * Se não tiver conta → **Cadastrar Usuário**
   * Se já tiver conta → **Login**
3. Após login → recebe recomendações de filmes
4. Pode aplicar filtros (gênero / autor)

---

##  Melhorias Futuras

* Implementar **hash de senhas** para segurança.
* Salvar o modelo **AutoEncoder** treinado (`autoencoder.h5`) para evitar treino a cada execução.
* Substituir `author` por **diretor/ano** (usando datasets enriquecidos).
* Integrar com **MongoDB** para persistência não relacional (usuários, histórico de recomendações).
* Criar versão **Web** (Flask/FastAPI + HTML/CSS/JS).

---

##  Requisitos de Instalação

Criar `requirements.txt` com:

```
pandas
numpy
scipy
scikit-learn
tensorflow
```

Instalar dependências:

```powershell
pip install -r requirements.txt

#O Sistema faz parte de um projeto criado para apresentação de um Projeto de Conclusão de Curso (TCC)
