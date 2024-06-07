from instaloader import Instaloader, Profile, Post

# Criar uma instância do Instaloader
loader = Instaloader()

# Carregar o perfil do Instagram
profile = Profile.from_username(loader.context, 'fatec.adamantina')

# Imprimir métricas do perfil
print('Seguidores:', profile.followers)
print('Seguindo:', profile.followees)

# Definir um dicionário para armazenar hashtags e suas contagens
hashtags_count = {}

# Definir variáveis para o total de curtidas, comentários e visualizações
total_likes = 0
total_comments = 0
total_views = 0

# Iterar sobre as postagens do perfil
for post in profile.get_posts():
    # Extrair as hashtags da legenda da postagem
    hashtags = post.caption_hashtags

    # Incrementar a contagem de cada hashtag no dicionário
    for hashtag in hashtags:
        if hashtag in hashtags_count:
            hashtags_count[hashtag] += 1
        else:
            hashtags_count[hashtag] = 1

    # Incrementar o total de curtidas, comentários e visualizações
    total_likes += post.likes
    total_comments += post.comments
    total_views += post.likes + post.comments

# Imprimir as métricas de engajamento
print('\nMétricas de Engajamento:')
print(f'Total de Curtidas: {total_likes}')
print(f'Total de Comentários: {total_comments}')
print(f'Total de Visualizações: {total_views}')

# Imprimir as hashtags mais populares
#print('\nHashtags Mais Populares:')
#for hashtag, count in sorted(hashtags_count.items(), key=lambda x: x[1], reverse=True)[:10]:
#   print(f'{hashtag}: {count}')


##################

# Iterar sobre as postagens do perfil
for post in profile.get_posts():
    # Imprimir informações detalhadas de cada postagem
    print('Postagem:', post.url)
    print('Curtidas:', post.likes)
    print('Comentários:', post.comments)
    print('Data de Publicação:', post.date_utc)
    print('Localização:', post.location)

    # Baixar a mídia da postagem (opcional)
    # loader.download_post(post, target='.')



    print('-' * 50)


######

