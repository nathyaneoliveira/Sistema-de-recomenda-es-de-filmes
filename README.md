# 📑 Sistema de Recomendação de Filmes

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?logo=python)
![Status](https://img.shields.io/badge/status-Em%20Desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-Acad%C3%AAmico-red)
![Framework](https://img.shields.io/badge/Framework-Tkinter-ff4b4b)

---

## Descrição

O **Sistema de Recomendação de Filmes** é um projeto acadêmico desenvolvido para **TCC – Trabalho de Conclusão de Curso**, utilizando **Inteligência Artificial** e **persistência de dados**.

Objetivos do sistema:

* Cadastrar e autenticar usuários em **SQLite**
* Recomendação personalizada de filmes usando **AutoEncoder**
* Aplicar filtros de **gênero** e **autor/diretor**
* Fornecer interface gráfica intuitiva com **Tkinter**
* Aprendizado de preferências baseado em **filtragem colaborativa**

---

## Estrutura do Projeto

```
sistematcc/
│── usuarios.db          # Banco SQLite (criado automaticamente)
│── movies.csv           # Catálogo de filmes (MovieLens)
│── ratings.csv          # Avaliações dos usuários
│── sistema.py           # Script principal do TCC
│── requirements.txt     # Dependências do projeto
```

---

## Requisitos

* Python **3.12+**
* Bibliotecas listadas no `requirements.txt`:

  * pandas
  * numpy
  * sqlite3
  * tkinter
  * scipy
  * scikit-learn
  * tensorflow

### Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## Compilação e Execução

Para iniciar o sistema:

```bash
python sistema.py
```

---

## Cadastro e Login

### Cadastro de usuário

```
Nome: João Silva
Email: joao@email.com
Senha: ********
```

* O usuário é salvo em `usuarios.db` no SQLite
* O email deve ser único

### Login

* Usuário informa email e senha
* Sistema valida no banco de dados
* Se válido → abre a interface de recomendações

---

## Recomendações de Filmes

* O sistema utiliza um **AutoEncoder** treinado com **filtragem colaborativa**
* Recomendações geradas com base nas preferências do usuário

### Exemplo de saída

```
Filmes recomendados:
- O Poderoso Chefão (Crime, Drama)
- A Origem (Ação, Ficção Científica)
- Forrest Gump (Drama, Romance)
- Interestelar (Aventura, Ficção Científica)
- Parasita (Thriller, Drama)
```

### Filtros

* **Gênero:** pesquisa parcial no campo `genres`
* **Autor/Diretor:** atualmente não disponível no MovieLens, mas preparado para expansão futura

---

## Fluxo de Uso

1. Instalar dependências
2. Executar o script `sistema.py`
3. Realizar cadastro ou login
4. Selecionar filtros (opcional)
5. Visualizar recomendações personalizadas

---

## Contribuição

Projeto acadêmico para **TCC**. Sugestões podem ser feitas via **GitHub** ou discutidas em sala de aula.

---

## Licença

Uso acadêmico restrito ao **Trabalho de Conclusão de Curso**.

---

## Estado do Projeto

* Cadastro e login funcionando
* Sistema de recomendação com AutoEncoder implementado
* Filtros por gênero funcionando
* Próximos módulos:

  * Hash de senhas para segurança
  * Salvar modelo treinado (`autoencoder.h5`)
  * Integração com MongoDB para histórico
  * Versão Web com Flask ou FastAPI

Quer que eu faça isso agora?
