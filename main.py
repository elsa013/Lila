import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

# --- COMANDO MEME CON FRASI DI TESTO ---
@bot.command()
async def meme(ctx):
    """Invia una frase o battuta casuale da una lista di stringhe"""
    # Lista contenente le frasi/battute testuali
    lista_battute = [
        "Ci sono 10 tipi di persone al mondo: chi capisce il binario e chi no.",
        "Il mio computer è così lento che quando clicco su 'Nuova Cartella' mi chiede se voglio aprirla in pensione.",
        "Ho detto al mio medico che ho la schiena a pezzi. Mi ha risposto: 'Hai provato a spegnere e riaccendere?'",
        "Programmatore (s.): Organismo che trasforma la caffeina in codice.",
        "Il codice funziona al primo colpo. Qualcosa non quadra, meglio formattare tutto."
    ]
    
    # Sceglie una frase a caso dalla lista
    battuta_casuale = random.choice(lista_battute)
    
    # Invia la frase testuale in chat
    await ctx.send(battuta_casuale)

bot.run("IL TOKEN SEGRETO VA QUI")
