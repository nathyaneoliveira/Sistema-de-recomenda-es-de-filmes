# 📑 Sistema de Recomendação de Filmes

### Projeto de TCC – Trabalho de Conclusão de Curso

---

##  1. Introdução

Este sistema foi desenvolvido como parte de um **Trabalho de Conclusão de Curso (TCC)**, com o objetivo de implementar um **sistema de recomendação de filmes** com autenticação de usuários.

O projeto combina **técnicas de Inteligência Artificial (IA)**, **persistência de dados** e **interface gráfica** para oferecer recomendações personalizadas a cada usuário.

---

##  2. Objetivos

* Desenvolver um sistema **funcional e interativo** para recomendação de filmes.
* Aplicar técnicas de **aprendizado de máquina** utilizando **AutoEncoder**.
* Explorar o conceito de **Persistência Poliglota**: uso de **SQLite** (SQL) e possibilidade de integração futura com **MongoDB** (NoSQL).
* Fornecer um ambiente com **login e cadastro de usuários**, simulando uma aplicação real.

---

##  3. Tecnologias Utilizadas

* **Linguagem principal:** Python 3.12+
* **Bibliotecas:**

  * `pandas` – manipulação de dados
  * `numpy` – operações numéricas
  * `sqlite3` – banco de dados relacional local
  * `tkinter` – interface gráfica
  * `scipy` – matrizes esparsas
  * `scikit-learn` – divisão dos dados (treino e teste)
  * `tensorflow.keras` – construção e treinamento do AutoEncoder

---

##  4. Estrutura do Projeto

```
sistematcc/
│── usuarios.db          # Banco SQLite (criado automaticamente)
│── movies.csv           # Dataset de filmes (MovieLens)
│── ratings.csv          # Dataset de avaliações (MovieLens)
│── sistema.py           # Script principal do TCC
│── requirements.txt     # Dependências do projeto
```

---

##  5. Banco de Dados

### 5.1 SQLite – Usuários

O sistema utiliza **SQLite**, um banco de dados relacional **leve e local**, para armazenar informações de usuários:

```sql
CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL
);
```

* Cada usuário é identificado pelo **email**
* O banco `usuarios.db` é criado automaticamente ao iniciar o sistema

**Referência:** [SQLite Official Documentation](https://www.sqlite.org/docs.html)

### 5.2 MovieLens Dataset – Filmes e Avaliações

O sistema utiliza o **MovieLens Small Dataset** (100k ratings) para treinamento do AutoEncoder:

**Arquivos utilizados:**

| Arquivo       | Descrição                                        | Link oficial                                                          |
| ------------- | ------------------------------------------------ | --------------------------------------------------------------------- |
| `movies.csv`  | Catálogo de filmes (id, título, gênero)          | [MovieLens Movies](https://grouplens.org/datasets/movielens/latest/)  |
| `ratings.csv` | Avaliações de usuários (userId, movieId, rating) | [MovieLens Ratings](https://grouplens.org/datasets/movielens/latest/) |

* O dataset é utilizado para construir a **matriz usuário-filme**
* Permite gerar recomendações personalizadas com base em filtragem colaborativa

---

##  6. Modelo de Recomendação

* Foi implementado um **AutoEncoder** utilizando **TensorFlow/Keras**.
* A matriz usuário-filme é usada como entrada, permitindo que o modelo aprenda padrões de preferências.
* Recomendações são geradas a partir da reconstrução da matriz de ratings.

---

##  7. Interface Gráfica (Tkinter)

### 🔹 Tela Inicial

* Opções: **Login** ou **Cadastro**

### 🔹 Cadastro

* Campos: Nome, Email, Senha
* Grava no banco `usuarios.db`

### 🔹 Login

* Autentica usuário
* Se válido → recomendações personalizadas

### 🔹 Recomendações

* Lista de filmes sugeridos
* Filtros disponíveis:

  * **Gênero** (campo de busca parcial)
  * **Autor** (não disponível no MovieLens, mas mantido para expansão futura)

---

##  8. Fluxo de Uso

1. Instalar dependências:

```powershell
pip install -r requirements.txt
```

2. Executar o sistema:

```powershell
python sistema.py
```

3. Na interface:

* Se não possui conta → **Cadastrar usuário**
* Se já possui → **Login**

4. Após login → sistema mostra recomendações personalizadas.


Quer que eu faça agora?
