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

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```
2.  **Set up Backend Environment (Recommended):**
    ```bash
    # Make sure you have Python 3 installed
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
3.  **Install Backend Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Backend Bridge Server:**
    ```bash
    python aevo_bridge.py
    ```
    *(This script runs the FastAPI bridge which in turn manages the FastMCP server defined in `server.py`. Ensure `config.py` has the correct settings if modified.)*
    The server should now be running, likely at `http://127.0.0.1:8081`.

5.  **Open the Frontend:**
    * Open the `index.html` file directly in your web browser. The page should load showing data for ETH.

## ⚠️ Important Note Regarding Submission Requirements

* **Static Backend:** This project utilizes a **static backend simulation** (`server.py` using predefined data) primarily to demonstrate the front-end functionality and its ability to communicate with an API.
* **No Blockchain Interaction:** The backend **simulates** order placement responses but **does not interact with the actual Aevo Testnet or Mainnet blockchain**.
* **No Transaction Hashes:** Consequently, **no real blockchain transaction hashes are generated** or available for submission (addressing Submission Requirement 1).
* **Inspector Screenshots:** As per Submission Requirement 2 for tools without blockchain transactions, proof of functionality will be provided via **inspector/console screenshots** demonstrating the front-end sending requests to the backend API and receiving simulated confirmations.

## Technologies Used

* **Frontend:** HTML, CSS, JavaScript, Chart.js
* **Backend:** Python, FastAPI, FastMCP, Uvicorn

Thanks for checking it out!
