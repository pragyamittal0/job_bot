
# 🧠 Company Intelligence Discord Bot

A smart Discord bot that searches a dataset of U.S. employers and provides insights like:

- 🔍 Top companies in a specific industry
- 🏥 Employers in the healthcare sector
- 🏆 Companies with the most initial approvals
- 🧠 Industry-based keyword search (e.g. `education`, `retail`, etc.)

Built using Python, Discord.py, and Pandas, this bot lets users explore real-world company data directly from Discord.

---

## 📦 Features

| Command              | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `!healthcare`        | Show top healthcare companies by initial approvals           |
| `!topcompanies`      | List top companies across all industries                     |
| `!industry <keyword>`| Find top companies in any industry (e.g., `education`, etc.) |

Example output:
```

🏥 MedStar Health
📍 Columbia, MD
📊 Initial Approvals: 1875

````

---

## 🧰 Tech Stack

- `discord.py` – Discord bot framework
- `pandas` – Data analysis
- `nest_asyncio` – For async compatibility (e.g., Jupyter or Colab)
- Data Source: Custom CSV file (`Employer Information-2.csv`)

---

## 📁 Dataset

> `Employer Information-2.csv`

This dataset includes:
- Employer names
- City/State
- Industry (NAICS Code)
- Approval counts

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/company-discord-bot.git
cd company-discord-bot
````

### 2. Install dependencies

```bash
pip install discord.py pandas nest_asyncio
```

### 3. Add your bot token

In the script, update:

```python
DISCORD_TOKEN = "YOUR_DISCORD_BOT_TOKEN"
```

> 🔒 Never share your token publicly.

### 4. Upload the dataset

Make sure `Employer Information-2.csv` is in the same directory as the Python script.

### 5. Run the bot

```bash
python bot.py
```

---

## 🛠️ Example Use Cases

* 📈 Market research in specific industries
* 🏥 Healthcare hiring trends
* 🎓 Education sector analysis
* 📊 Fast insights from raw employer data — inside Discord

---

## 📌 To-Do / Ideas

* [ ] Add support for denial stats
* [ ] Slash commands (`/industry <keyword>`)
* [ ] Interactive dropdowns in Discord UI
* [ ] Web version of the same insights

---

## 🤝 Contribute

Feel free to open issues or submit pull requests for feature improvements, bug fixes, or UI enhancements!

```

---

Would you like me to generate:
- A `requirements.txt`?
- GitHub badges or images for the README?
- A deploy guide (e.g. Railway, Replit)?

Let me know — happy to complete the setup!
```
