📑 Documentação 1 – Sistema de Recomendação de Filmes








Descrição

O Sistema de Recomendação de Filmes é um projeto acadêmico desenvolvido para TCC – Trabalho de Conclusão de Curso, utilizando Inteligência Artificial e persistência de dados.

Objetivos do sistema:

Cadastrar e autenticar usuários em SQLite

Recomendação personalizada de filmes usando AutoEncoder

Aplicar filtros de gênero e autor/diretor

Fornecer interface gráfica intuitiva com Tkinter

Aprendizado de preferências baseado em filtragem colaborativa

Estrutura do Projeto
sistematcc/
│── usuarios.db          # Banco SQLite (criado automaticamente)
│── movies.csv           # Catálogo de filmes (MovieLens)
│── ratings.csv          # Avaliações dos usuários
│── sistema.py           # Script principal do TCC
│── requirements.txt     # Dependências do projeto

Requisitos

Python 3.12+

Bibliotecas listadas no requirements.txt:

pandas

numpy

sqlite3

tkinter

scipy

scikit-learn

tensorflow

Instalação das dependências
pip install -r requirements.txt

Compilação e Execução

Para iniciar o sistema:

python sistema.py

Exemplos de Uso
Cadastro de usuário
Nome: João Silva
Email: joao@email.com
Senha: ********

Login e recomendação

Usuário realiza login

Sistema sugere filmes de acordo com histórico de avaliações

Exemplo de saída:

Filmes recomendados:
- O Poderoso Chefão (Crime, Drama)
- A Origem (Ação, Ficção Científica)
- Forrest Gump (Drama, Romance)
- ...


Possibilidade de filtrar por gênero ou autor/diretor (quando disponível)

Contribuição

Projeto acadêmico para TCC. Sugestões podem ser feitas via GitHub ou discutidas em sala de aula.

Licença

Uso acadêmico restrito ao Trabalho de Conclusão de Curso.

Estado

Cadastro e login funcionando

Sistema de recomendação com AutoEncoder implementado

Filtros por gênero e autor/diretor funcionando parcialmente

Próximos módulos: salvar modelo treinado, integração com MongoDB, versão Web
