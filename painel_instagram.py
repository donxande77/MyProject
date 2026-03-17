# ----------------------------
# INSTALAÇÃO AUTOMÁTICA DE MÓDULOS
# ----------------------------
import subprocess
import sys

def instalar_modulo(modulo):
    try:
        __import__(modulo)
    except ImportError:
        print(f"Instalando módulo {modulo}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", modulo])

modulos_necessarios = ["requests", "Pillow", "feedparser", "openai", "streamlit"]
for m in modulos_necessarios:
    instalar_modulo(m)

# ----------------------------
# IMPORTS
# ----------------------------
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from datetime import datetime
import feedparser
import openai
import streamlit as st
import time

# ----------------------------
# CONFIGURAÇÕES
# ----------------------------
INSTAGRAM_BUSINESS_ID = "SEU_INSTAGRAM_BUSINESS_ID"
ACCESS_TOKEN = "SEU_ACCESS_TOKEN"
OPENAI_API_KEY = "SUA_CHAVE_OPENAI"
openai.api_key = OPENAI_API_KEY

# Pastas para imagens e stories
os.makedirs("imagens_posts", exist_ok=True)
os.makedirs("imagens_stories", exist_ok=True)

# Fonte para textos
try:
    FONT = ImageFont.truetype("arial.ttf", 40)
except:
    FONT = ImageFont.load_default()

# ----------------------------
# 1. BUSCAR TENDÊNCIAS
# ----------------------------
def buscar_tendencias():
    feed = feedparser.parse(
        "https://news.google.com/rss/search?q=saúde+bem+estar&hl=pt-BR&gl=BR&ceid=BR:pt-419"
    )
    return [entry.title for entry in feed.entries[:5]]

# ----------------------------
# 2. BUSCAR ARTISTAS/INFLUENCIADORES
# ----------------------------
def buscar_artistas(tema):
    prompt = f"""
Liste 5 artistas, influenciadores ou especialistas em saúde e bem-estar
relacionados ao seguinte tema: {tema}.
Para cada um, descreva onde vivem, sua rotina ou foco principal.
Retorne em formato: Nome - Local - Foco/rotina
"""
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# ----------------------------
# 3. GERAR POST (TEXTO + IMAGEM)
# ----------------------------
def gerar_texto_post(tema, artistas):
    prompt = f"""
Crie um texto educativo, curto e envolvente sobre: {tema}.
Inclua referências aos seguintes artistas/influenciadores: {artistas}
"""
    response = openai.ChatCompletion.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

def gerar_imagem_dalle(prompt_texto):
    """Gera imagem realista via DALL·E"""
    response = openai.Image.create(
        prompt=prompt_texto,
        n=1,
        size="1080x1080"
    )
    url_imagem = response['data'][0]['url']
    caminho = f"imagens_posts/post_{int(time.time())}.png"
    r = requests.get(url_imagem, stream=True)
    if r.status_code == 200:
        with open(caminho, "wb") as f:
            for chunk in r.iter_content(1024):
                f.write(chunk)
    return caminho

# ----------------------------
# 4. GERAR STORIES COM CAIXINHA DE PERGUNTAS
# ----------------------------
def gerar_story(tema):
    img = Image.new('RGB', (1080, 1920), color=(255, 255, 255))
    d = ImageDraw.Draw(img)
    texto = f"{tema}\nO que você acha? Responda na caixinha abaixo!"
    d.text((50, 900), texto, fill=(0,0,0), font=FONT)
    caminho = f"imagens_stories/story_{int(time.time())}.png"
    img.save(caminho)
    return caminho

# ----------------------------
# 5. STREAMLIT PAINEL DE APROVAÇÃO
# ----------------------------
st.title("Painel de Aprovação de Posts - Saúde e Bem-Estar")

tendencias = buscar_tendencias()
st.write("Tendências do dia:")
for idx, tema in enumerate(tendencias):
    st.subheader(f"{idx+1}. {tema}")
    
    artistas = buscar_artistas(tema)
    st.text(f"Artistas/Inlfuencers:\n{artistas}")
    
    texto_post = gerar_texto_post(tema, artistas)
    st.text_area("Texto do post:", texto_post, height=150)
    
    imagem_post = gerar_imagem_dalle(texto_post)
    st.image(imagem_post, caption="Imagem do post")
    
    story_path = gerar_story(tema)
    st.image(story_path, caption="Story com caixinha de perguntas")
    
    publicar = st.checkbox(f"Aprovar e publicar '{tema}'?", key=idx)
    
    if publicar:
        st.write(f"Post e Story para '{tema}' aprovados! Preparados para envio via API.")
        # Aqui você poderia chamar a função postar_instagram(imagem_post, texto_post)
        # e postar_story(story_path) se tiver URLs públicas ou API de stories configurada.

st.write("=== Fim do painel ===")