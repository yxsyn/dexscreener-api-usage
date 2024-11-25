# Dexscreener Discord Bot - Rizzmas Community

This **Python-based Discord bot** fetches real-time token data from the **Dexscreener API** and posts updates to a designated Discord channel. Initially created for the **Rizzmas community**, this bot is now available for anyone who wants to track any token's real-time data in their Discord server. It provides automatic updates on a token's **price (USD)**, **market cap**, and **liquidity**.

## Features

- **Real-time updates** from the **Dexscreener API** for any token.
- Displays key token information:
  - **Price (USD)**
  - **Market Cap**
  - **Liquidity**
- **Automatic updates** sent to a designated Discord channel.
- Runs as a **background task**, fetching data every second.
- **Easy customization**: Change the contract address to track any token.

## Prerequisites

To run this bot, you'll need the following:

- **Python 3.x** installed on your machine.
- A **Discord bot token** (create one in the [Discord Developer Portal](https://discord.com/developers/applications)).
- Required libraries:
  - `discord.py` - for interacting with Discord.
  - `aiohttp` - for making asynchronous HTTP requests.

## Setup & Installation

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/yxsyn/rizzmas-dexscreener-bot.git
cd rizzmas-dexscreener-bot
