# 🐚 MTS Stock Checker

Checks daily if Malaysian Trumpet Snails are back in stock at Superior Shrimp & Aquatics and emails you when they are.

---

## Setup (one-time, ~10 minutes)

### Step 1 — Create this repo on GitHub

1. Go to [github.com](https://github.com) and sign in (or create a free account)
2. Click **+** → **New repository**
3. Name it `mts-stock-checker`, set it to **Private**, click **Create repository**
4. Upload both files (`check_stock.py` and `.github/workflows/check_stock.yml`) using the **Add file → Upload files** button
   - To upload the workflow file, you'll need to first create the `.github/workflows/` folder path manually or use the GitHub web editor

> **Easier upload option:** Use [GitHub Desktop](https://desktop.github.com/) to drag and drop the whole folder.

### Step 2 — Create a Gmail App Password

GitHub needs a way to send email on your behalf. Gmail requires an "App Password" (not your regular password):

1. Go to your Google Account → **Security**
2. Make sure **2-Step Verification** is enabled
3. Search for **App passwords** (or go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords))
4. Create a new app password — name it "MTS Checker"
5. Copy the 16-character password it gives you

### Step 3 — Add secrets to GitHub

1. In your GitHub repo, go to **Settings → Secrets and variables → Actions**
2. Click **New repository secret** and add these two:

| Name | Value |
|------|-------|
| `GMAIL_USER` | Your Gmail address (e.g. `jayolsen@gmail.com`) |
| `GMAIL_APP_PASSWORD` | The 16-character app password from Step 2 |

### Step 4 — Test it

1. Go to the **Actions** tab in your repo
2. Click **MTS Stock Checker** on the left
3. Click **Run workflow** → **Run workflow**
4. Watch the run — it should complete in under 30 seconds
5. You'll only get an email if the snails are in stock; otherwise check the run log for "Still sold out"

---

## Schedule

Runs automatically every day at **8:00 AM Mountain Time**. You'll only receive an email on days when the item is in stock.

To change the time, edit the `cron` line in `.github/workflows/check_stock.yml`.  
Cron format: `minute hour * * *` (times are in UTC; Mountain = UTC−6 in winter, UTC−7 in summer).
