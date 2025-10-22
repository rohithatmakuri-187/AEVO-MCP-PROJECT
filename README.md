# Aevo Trading Terminal Practice Tool

Hey there! 👋 Welcome to this practice version of the Aevo Trading Terminal.

## What's This All About?

Think of this as a flight simulator for Aevo trading! It's a website I built that looks and feels like the real Aevo platform, letting you get a feel for trading without using real money. You can check out market info, look at price charts, and pretend to place buy and sell orders.

## Cool Things You Can Do:

* **See Market Info:** Check out stats like price, volume, and daily change for cryptos like ETH, BTC, SOL, etc., fetched from a practice backend.
* **Watch Charts:** Look at interactive price charts for different assets.
* **Practice Trading:** Log in with any username to start a demo session. Place simulated "Limit" buy or sell orders using the easy form.
* **Track Your (Fake) Money:** See how your trades affect your starting balance and what assets you hold on the Portfolio page. There's even a pie chart to show how your fake money is split!
* **Looks Good Everywhere:** The layout changes automatically to fit your screen, whether you're on a big monitor or your phone.
* **Switch Styles:** Prefer light mode? You can toggle between light and dark themes on the Portfolio page.
* **(Bonus) See Fake Trades:** The "Recent Trades" panel shows randomly generated trades to make it feel more alive.

## Want to Try It?

1.  **Download the Code:** Get all the files from this GitHub repository.
2.  **Start the Backend:**
    * You'll need Python installed.
    * Open your computer's terminal (like Command Prompt or Terminal app).
    * Go into the project folder (`cd your-project-folder-name`).
    * It's best to set up a Python virtual spot: `python3 -m venv venv` then `source venv/bin/activate` (or `venv\Scripts\activate` on Windows).
    * Install the needed bits: `pip install -r requirements.txt`.
    * Run the server: `python aevo_bridge.py`. You should see messages that it's running.
3.  **Open the Website:** Just double-click the `index.html` file to open it in your web browser.

## ⚠️ Heads Up - Important Note!

* **It's a Simulation:** This practice tool uses a **pre-built backend** (`server.py`) with **fake, static data**. It doesn't connect to the *real* Aevo or use live market prices.
* **No Real Trading/Blockchain:** When you "place an order," it sends a request to the fake backend and *pretends* it went through. **No actual trades happen on the blockchain**, and no real money is involved.
* **No Transaction Hashes:** Because there are no real blockchain actions, **there won't be any transaction hashes** to show for the submission. I'll be providing screenshots of the website working and talking to the fake backend instead, as requested for non-blockchain tools.

## Built With:

* **Frontend:** HTML, CSS, JavaScript (with Chart.js)
* **Backend:** Python, FastAPI, FastMCP

Thanks for checking it out!