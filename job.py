import discord
from discord.ext import commands
import pandas as pd
import nest_asyncio
import asyncio

nest_asyncio.apply()

DISCORD_TOKEN = "" #put your token

# Load and clean dataset
df = pd.read_csv("Employer Information-2.csv", encoding="utf-16", sep="\t", engine="python")
df = df.dropna(subset=["Employer (Petitioner) Name", "Industry (NAICS) Code", "Initial Approval"])
df["Initial Approval"] = pd.to_numeric(df["Initial Approval"], errors="coerce").fillna(0).astype(int)

# Normalize column names
df["Industry (NAICS) Code"] = df["Industry (NAICS) Code"].str.lower()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

# 🔍 Command: !healthcare
@bot.command()
async def healthcare(ctx):
    subset = df[df["Industry (NAICS) Code"].str.contains("health care")]
    top = subset.sort_values(by="Initial Approval", ascending=False).head(5)

    if top.empty:
        await ctx.send("❌ No healthcare companies found.")
        return

    for _, row in top.iterrows():
        msg = (
            f"🏥 **{row['Employer (Petitioner) Name']}**\n"
            f"📍 {row['Petitioner City']}, {row['Petitioner State']}\n"
            f"📊 Initial Approvals: {row['Initial Approval']}"
        )
        await ctx.send(msg)

# 🏆 Command: !topcompanies
@bot.command()
async def topcompanies(ctx):
    top = df.sort_values(by="Initial Approval", ascending=False).head(5)

    for _, row in top.iterrows():
        msg = (
            f"🏢 **{row['Employer (Petitioner) Name']}**\n"
            f"🏷️ Industry: {row['Industry (NAICS) Code'].title()}\n"
            f"📍 {row['Petitioner City']}, {row['Petitioner State']}\n"
            f"📊 Initial Approvals: {row['Initial Approval']}"
        )
        await ctx.send(msg)

# 🔎 Command: !industry <keyword>
@bot.command()
async def industry(ctx, *, keyword):
    keyword = keyword.lower()
    subset = df[df["Industry (NAICS) Code"].str.contains(keyword)]
    top = subset.sort_values(by="Initial Approval", ascending=False).head(5)

    if top.empty:
        await ctx.send(f"❌ No companies found in industry: {keyword}")
        return

    for _, row in top.iterrows():
        msg = (
            f"🏢 **{row['Employer (Petitioner) Name']}**\n"
            f"📍 {row['Petitioner City']}, {row['Petitioner State']}\n"
            f"📊 Initial Approvals: {row['Initial Approval']}"
        )
        await ctx.send(msg)

# ▶️ Run the bot
async def start_bot():
    await bot.start(DISCORD_TOKEN)

await start_bot()
