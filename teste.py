# ----------------------------
# VERIFICAÇÃO E INSTALAÇÃO AUTOMÁTICA DE MÓDULOS
# ----------------------------
import subprocess
import sys

def instalar_modulo(modulo):
    try:
        __import__(modulo)
    except ImportError:
        print(f"Instalando módulo {modulo}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", modulo])

# Lista de módulos necessários
modulos_necessarios = ["requests", "schedule", "Pillow", "feedparser", "openai"]

for m in modulos_necessarios:
    instalar_modulo(m)

# ----------------------------
# IMPORTS APÓS INSTALAÇÃO
# ----------------------------
import requests
import schedule
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import openai
import feedparser

# ----------------------------
# CONFIGURAÇÕES
# ----------------------------
INSTAGRAM_BUSINESS_ID = "SEU_INSTAGRAM_BUSINESS_ID"
ACCESS_TOKEN = "SEU_ACCESS_TOKEN"
OPENAI_API_KEY = "SUA_CHAVE_OPENAI"
openai.api_key = OPENAI_API_KEY

# ----------------------------
# 1. BUSCAR TENDÊNCIAS E TEMAS
# ----------------------------
def buscar_tendencias():
    feed = feedparser.parse("https://news.google.com/rss/search?q=saúde+bem+estar&hl=pt-BR&gl=BR&ceid=BR:pt-419")
    top_noticias = [entry.title for entry in feed.entries[:5]]
    return top_noticias

# ----------------------------
# 2. BUSCAR ARTISTAS/INFLUENCIADORES RELACIONADOS
# ----------------------------
def buscar_artistas(tema):
    prompt = f"""
    Liste 5 artistas, influenciadores ou especialistas em saúde e bem-estar
    relacionados ao seguinte tema: {tema}.
    Para cada um, descreva onde vivem, sua rotina ou foco principal.
    Retorne em formato:
    Nome - Local - Foco/rotina
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    artistas = response.choices[0].message.content.strip()
    return artistas

# ----------------------------
# 3. BOT DE CONTEÚDO COM IA
# ----------------------------
def gerar_texto_post(tema, artistas):
    prompt = f"""
    Crie um texto educativo, curto, envolvente e amigável sobre: {tema}.
    Inclua referências aos seguintes artistas/influenciadores:
    {artistas}
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def gerar_imagem(texto):
    img = Image.new('RGB', (1080, 1080), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    d.text((50, 500), texto, fill=(0, 0, 0), font=font)
    nome_arquivo = f"post_{int(time.time())}.png"
    img.save(nome_arquivo)
    return nome_arquivo

# ----------------------------
# 4. BOT DE PUBLICAÇÃO
# ----------------------------
def postar_instagram(imagem_path, legenda):
    url_upload = f"https://graph.facebook.com/v17.0/{INSTAGRAM_BUSINESS_ID}/media"
    payload = {
        'image_url': imagem_path,
        'caption': legenda,
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url_upload, data=payload)
    if response.status_code == 200:
        creation_id = response.json()['id']
        publish_url = f"https://graph.facebook.com/v17.0/{INSTAGRAM_BUSINESS_ID}/media_publish"
        publish_response = requests.post(publish_url, data={'creation_id': creation_id, 'access_token': ACCESS_TOKEN})
        print("Post publicado:", publish_response.json())
    else:
        print("Erro ao criar post:", response.text)

# ----------------------------
# 5. ENGAGEMENT SIMPLES
# ----------------------------
def curtir_comentarios():
    print("Simulando curtir comentários relevantes...")

# ----------------------------
# 6. ROTINA DIÁRIA COM APROVAÇÃO
# ----------------------------
def rotina_diaria():
    print(f"\n=== Rotina diária iniciada em {datetime.now()} ===")
    
    tendencias = buscar_tendencias()
    print("Tendências do dia:", tendencias)

    for tema in tendencias:
        artistas = buscar_artistas(tema)
        print("\nArtistas relacionados encontrados:\n", artistas)
        
        texto_post = gerar_texto_post(tema, artistas)
        imagem_post = gerar_imagem(texto_post)

        print("\n=== NOVO POST SUGERIDO ===")
        print("Tema:", tema)
        print("Texto:", texto_post)
        decisao = input("Deseja publicar este post? (s/n): ").lower()
        if decisao == 's':
            postar_instagram(imagem_post, texto_post)
        else:
            print("Post não publicado.")

    curtir_comentarios()

# ----------------------------
# AGENDAMENTO DIÁRIO
# ----------------------------
schedule.every().day.at("09:00").do(rotina_diaria)

# ----------------------------
# LOOP DE EXECUÇÃO
# ----------------------------
while True:
    schedule.run_pending()
    time.sleep(60)





    #----------------------------------------------------------------------------------------------------------------------
    # inserir em um novo arquivo...
    # ----------------------------
# VERIFICAÇÃO E INSTALAÇÃO AUTOMÁTICA DE MÓDULOS
# ----------------------------
import subprocess
import sys

def instalar_modulo(modulo):
    try:
        __import__(modulo)
    except ImportError:
        print(f"Instalando módulo {modulo}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", modulo])

modulos_necessarios = ["requests", "schedule", "Pillow", "feedparser", "openai"]
for m in modulos_necessarios:
    instalar_modulo(m)

# ----------------------------
# IMPORTS
# ----------------------------
import requests
import schedule
import time
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import openai
import feedparser
import os

# ----------------------------
# CONFIGURAÇÕES
# ----------------------------
INSTAGRAM_BUSINESS_ID = "SEU_INSTAGRAM_BUSINESS_ID"
ACCESS_TOKEN = "SEU_ACCESS_TOKEN"
OPENAI_API_KEY = "SUA_CHAVE_OPENAI"
openai.api_key = OPENAI_API_KEY

# Pasta para salvar imagens e stories
os.makedirs("imagens_posts", exist_ok=True)
os.makedirs("imagens_stories", exist_ok=True)

# ----------------------------
# 1. BUSCAR TENDÊNCIAS E TEMAS
# ----------------------------
def buscar_tendencias():
    feed = feedparser.parse("https://news.google.com/rss/search?q=saúde+bem+estar&hl=pt-BR&gl=BR&ceid=BR:pt-419")
    top_noticias = [entry.title for entry in feed.entries[:5]]
    return top_noticias

# ----------------------------
# 2. BUSCAR ARTISTAS/INFLUENCIADORES
# ----------------------------
def buscar_artistas(tema):
    prompt = f"""
    Liste 5 artistas, influenciadores ou especialistas em saúde e bem-estar
    relacionados ao seguinte tema: {tema}.
    Para cada um, descreva onde vivem, sua rotina ou foco principal.
    Retorne em formato:
    Nome - Local - Foco/rotina
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    artistas = response.choices[0].message.content.strip()
    return artistas

# ----------------------------
# 3. GERAR TEXTO E IMAGEM DO POST
# ----------------------------
def gerar_texto_post(tema, artistas):
    prompt = f"""
    Crie um texto educativo, curto, envolvente e amigável sobre: {tema}.
    Inclua referências aos seguintes artistas/influenciadores:
    {artistas}
    """
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def gerar_imagem_dalle(prompt_texto):
    """Gera imagem realista usando DALL·E"""
    response = openai.Image.create(
        prompt=prompt_texto,
        n=1,
        size="1080x1080"
    )
    url_imagem = response['data'][0]['url']
    imagem_data = requests.get(url_imagem).content
    caminho = f"imagens_posts/post_{int(time.time())}.png"
    with open(caminho, "wb") as f:
        f.write(imagem_data)
    return caminho

# ----------------------------
# 4. GERAR STORIES COM CAIXINHA DE PERGUNTAS
# ----------------------------
def gerar_story(tema):
    """Cria um story simples com caixinha de perguntas"""
    img = Image.new('RGB', (1080, 1920), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    texto = f"{tema}\nO que você acha? Responda na caixinha abaixo!"
    d.text((50, 900), texto, fill=(0, 0, 0), font=font)
    caminho = f"imagens_stories/story_{int(time.time())}.png"
    img.save(caminho)
    return caminho

# ----------------------------
# 5. POSTAR NO INSTAGRAM
# ----------------------------
def postar_instagram(imagem_path, legenda):
    url_upload = f"https://graph.facebook.com/v17.0/{INSTAGRAM_BUSINESS_ID}/media"
    payload = {
        'image_url': imagem_path,
        'caption': legenda,
        'access_token': ACCESS_TOKEN
    }
    response = requests.post(url_upload, data=payload)
    if response.status_code == 200:
        creation_id = response.json()['id']
        publish_url = f"https://graph.facebook.com/v17.0/{INSTAGRAM_BUSINESS_ID}/media_publish"
        publish_response = requests.post(publish_url, data={'creation_id': creation_id, 'access_token': ACCESS_TOKEN})
        print("Post publicado:", publish_response.json())
    else:
        print("Erro ao criar post:", response.text)

def postar_story(imagem_path):
    """Exemplo de postagem de story (precisa de URL pública da imagem ou uso da API oficial)"""
    print(f"Story gerado: {imagem_path} (simulação, publique via API ou manualmente)")

# ----------------------------
# 6. ENGAGEMENT SIMPLES
# ----------------------------
def curtir_comentarios():
    print("Simulando curtir comentários relevantes...")

# ----------------------------
# 7. ROTINA DIÁRIA
# ----------------------------
def rotina_diaria():
    print(f"\n=== Rotina diária iniciada em {datetime.now()} ===")
    
    tendencias = buscar_tendencias()
    print("Tendências do dia:", tendencias)

    for tema in tendencias:
        artistas = buscar_artistas(tema)
        print("\nArtistas relacionados encontrados:\n", artistas)
        
        texto_post = gerar_texto_post(tema, artistas)
        imagem_post = gerar_imagem_dalle(texto_post)

        story_path = gerar_story(tema)

        print("\n=== NOVO POST SUGERIDO ===")
        print("Tema:", tema)
        print("Texto:", texto_post)
        decisao = input("Deseja publicar este post? (s/n): ").lower()
        if decisao == 's':
            postar_instagram(imagem_post, texto_post)
            postar_story(story_path)
        else:
            print("Post não publicado.")

    curtir_comentarios()

# ----------------------------
# 8. AGENDAMENTO DIÁRIO
# ----------------------------
schedule.every().day.at("09:00").do(rotina_diaria)

# ----------------------------
# LOOP DE EXECUÇÃO
# ----------------------------
while True:
    schedule.run_pending()
    time.sleep(60)