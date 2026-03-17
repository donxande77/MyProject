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