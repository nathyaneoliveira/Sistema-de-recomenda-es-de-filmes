import pandas as pd
import numpy as np
import sqlite3
import tkinter as tk
from scipy.sparse import csr_matrix
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers, models
from tkinter import ttk, messagebox

# Carregamento dos dados MovieLens

df_movies = pd.read_csv("movies.csv")
df_ratings_full = pd.read_csv("ratings.csv")

# Converter notas para binário

df_ratings_full['binary_rating'] = (df_ratings_full['rating'] >= 4).astype(int)

# Mostra 30 usuários

np.random.seed(42)
sample_users = np.random.choice(df_ratings_full['userId'].unique(), size=30, replace=False)
df_ratings = df_ratings_full[df_ratings_full['userId'].isin(sample_users)]

# Mapear IDs para índices

user_ids = df_ratings['userId'].unique()
movie_ids = df_ratings['movieId'].unique()

u2idx = {u: i for i, u in enumerate(user_ids)}
i2idx = {i: j for j, i in enumerate(movie_ids)}
idx2i = {v: k for k, v in i2idx.items()}

# Criar matriz usuário-item

rows = df_ratings['userId'].map(u2idx)
cols = df_ratings['movieId'].map(i2idx)
data = df_ratings['binary_rating'].values
M = csr_matrix((data, (rows, cols)), shape=(len(user_ids), len(movie_ids))).toarray()

# AutoEncoder
n_items = M.shape[1]

input_layer = layers.Input(shape=(n_items,))
encoded = layers.Dense(128, activation='relu')(input_layer)
encoded = layers.Dense(64, activation='relu')(encoded)
decoded = layers.Dense(128, activation='relu')(encoded)
output_layer = layers.Dense(n_items, activation='sigmoid')(decoded)

autoencoder = models.Model(input_layer, output_layer)
autoencoder.compile(optimizer='adam', loss='binary_crossentropy')

X_train, X_test = train_test_split(M, test_size=0.2, random_state=42)
autoencoder.fit(
    X_train, X_train,
    epochs=10,
    batch_size=16,
    validation_data=(X_test, X_test),
    verbose=0
)

# Função de recomendação

def recommend_autoencoder(user_id, topk=20):
    if user_id not in u2idx:
        populares = df_ratings_full.groupby("movieId")['rating'].count().sort_values(ascending=False).head(topk).index
        recs = df_movies[df_movies['movieId'].isin(populares)][['title', 'genres', 'movieId']]
        return recs

    user_idx = u2idx[user_id]
    user_vector = M[user_idx].reshape(1, -1)

    scores = autoencoder.predict(user_vector, verbose=0)[0]
    seen = np.where(user_vector[0] > 0)[0]
    scores[seen] = -1
    recs_idx = np.argsort(-scores)[:topk]

    recommended_movieIds = [idx2i[i] for i in recs_idx]
    recs = df_movies[df_movies['movieId'].isin(recommended_movieIds)][['title', 'genres', 'movieId']]
    return recs

# Banco de dados usuários

def init_db():
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            senha TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def cadastrar_usuario(nome, email, senha):
    try:
        conn = sqlite3.connect("usuarios.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def validar_login(email, senha):
    conn = sqlite3.connect("usuarios.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha = ?", (email, senha))
    user = cursor.fetchone()
    conn.close()
    return user

# Interfaces Tkinter

def abrir_tela_recomendacao(usuario):
    tela_login.destroy()
    rec_window = tk.Tk()
    rec_window.title("Sistema de Recomendação Filmes")
    rec_window.geometry("600x500")

    ttk.Label(rec_window, text=f"Bem-vindo, {usuario[1]}!", font=("Arial", 14)).pack(pady=10)

    # Frame para filtros
    frame_filtros = ttk.Frame(rec_window)
    frame_filtros.pack(pady=5)

    ttk.Label(frame_filtros, text="Gênero preferido (opcional):").grid(row=0, column=0, padx=5, pady=2)
    entry_genero = ttk.Entry(frame_filtros)
    entry_genero.grid(row=0, column=1, padx=5, pady=2)

    ttk.Label(frame_filtros, text="Autor/Diretor preferido (opcional):").grid(row=1, column=0, padx=5, pady=2)
    entry_autor = ttk.Entry(frame_filtros)
    entry_autor.grid(row=1, column=1, padx=5, pady=2)

    # Botão de recomendação
    text_result = tk.Text(rec_window, wrap="word", height=20, width=70)
    text_result.pack(pady=10)

    def recomendar_com_filtro():
        user_id = usuario[0]
        genero = entry_genero.get().strip().lower()
        autor = entry_autor.get().strip().lower()

        recs = recommend_autoencoder(user_id, topk=20)

        if genero:
            recs = recs[recs['genres'].str.lower().str.contains(genero)]

        if autor and 'author' in recs.columns:
            recs = recs[recs['author'].str.lower().str.contains(autor)]

        if not recs.empty:
            recs = recs.sample(n=min(5, len(recs)), replace=False, random_state=None)

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, " Filmes recomendados:\n\n")
        if recs.empty:
            text_result.insert(tk.END, "Nenhum filme encontrado com esses filtros.\n")
        else:
            for _, row in recs.iterrows():
                text_result.insert(tk.END, f"- {row['title']} ({row['genres']})\n")

    ttk.Button(rec_window, text="Recomendar", command=recomendar_com_filtro).pack(pady=5)

    rec_window.mainloop()

# Cadastro e Login

def abrir_tela_cadastro():
    def cadastrar():
        nome = entry_nome.get()
        email = entry_email.get()
        senha = entry_senha.get()

        if nome and email and senha:
            if cadastrar_usuario(nome, email, senha):
                messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
                cadastro_window.destroy()
            else:
                messagebox.showerror("Erro", "Email já cadastrado!")
        else:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")

    cadastro_window = tk.Toplevel(tela_login)
    cadastro_window.title("Cadastro")
    cadastro_window.geometry("400x300")

    ttk.Label(cadastro_window, text="Nome:").pack(pady=5)
    entry_nome = ttk.Entry(cadastro_window)
    entry_nome.pack(pady=5)

    ttk.Label(cadastro_window, text="Email:").pack(pady=5)
    entry_email = ttk.Entry(cadastro_window)
    entry_email.pack(pady=5)

    ttk.Label(cadastro_window, text="Senha:").pack(pady=5)
    entry_senha = ttk.Entry(cadastro_window, show="*")
    entry_senha.pack(pady=5)

    ttk.Button(cadastro_window, text="Cadastrar", command=cadastrar).pack(pady=10)

def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()
    user = validar_login(email, senha)
    if user:
        abrir_tela_recomendacao(user)
    else:
        messagebox.showerror("Erro", "Email ou senha inválidos!")

# Tela de Login principal

init_db()

tela_login = tk.Tk()
tela_login.title("Login - Sistema de Recomendação")
tela_login.geometry("400x250")

ttk.Label(tela_login, text="Email:").pack(pady=5)
entry_email = ttk.Entry(tela_login)
entry_email.pack(pady=5)

ttk.Label(tela_login, text="Senha:").pack(pady=5)
entry_senha = ttk.Entry(tela_login, show="*")
entry_senha.pack(pady=5)

ttk.Button(tela_login, text="Login", command=fazer_login).pack(pady=10)
ttk.Button(tela_login, text="Cadastrar", command=abrir_tela_cadastro).pack(pady=5)

tela_login.mainloop()