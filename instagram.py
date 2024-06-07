import instaloader

# Crie uma instância do Instaloader
loader = instaloader.Instaloader()

# Insira o nome do perfil do Instagram que deseja analisar
profile = "ronnieshida"

# Carregue o perfil
profile_data = instaloader.Profile.from_username(loader.context, profile)

# Imprima algumas estatísticas de engajamento
print(f"Seguidores: {profile_data.followers}")
print(f"Seguindo: {profile_data.followees}")
print(f"Número de postagens: {profile_data.mediacount}")

# Calcule a média de curtidas e comentários por postagem
total_likes = 0
total_comments = 0
for post in profile_data.get_posts():
    total_likes += post.likes
    total_comments += post.comments
media_likes_por_post = total_likes / profile_data.mediacount
media_comentarios_por_post = total_comments / profile_data.mediacount

print(f"Média de curtidas por postagem: {media_likes_por_post}")
print(f"Média de comentários por postagem: {media_comentarios_por_post}")
