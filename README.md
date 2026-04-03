<h1 align="center">
  🚀 Facebook Auto Poster (Python + Selenium)
</h1>

<p align="center">
  <strong>A safe, anti-ban, intelligent Command-Line Interface (CLI) to automatically post texts and images across multiple Facebook Groups mimicking human behavior!</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue.svg?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Selenium-WebDriver-green.svg?logo=selenium" alt="Selenium">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg" alt="Maintained">
</p>

## 🌟 Why this Tool?
Unlike fully automated legacy scripts, this tool operates on an **Anti-Ban Concept** using a "Semi-Automated" workflow and random execution delays. 
- You manually login to build genuine browsing cache.
- The tool navigates and interacts securely via Selenium WebDriver.
- Randomized dynamic delays (5-15s) are injected between specific actions.
- The user gives the final posting confirmation directly from the terminal.

This significantly diminishes the probability of your Facebook Account being shadow-banned or locked!

## ✨ Features
- **Upload Text and Images** seamlessly into Facebook groups.
- **Queue System**: Pre-load multiple groups and let the bot navigate individually.
- **Smart Element Detection**: Targets dynamic Facebook DOM classes robustly.
- **Save Groups Engine**: Easily stores your groups locally in `groups.json`.
- **Lightweight CLI**: Completely sidesteps OS-level GUI crashing (No Tkinter issues).
- **Anti-Ban Safety Measures**: Respects Facebook rate-limiting policies.

## 🛠️ Installation

**1. Clone the repository**
```bash
git clone https://github.com/YourUsername/Facebook-Group-Auto-Poster.git
cd Facebook-Group-Auto-Poster
```

**2. Install Prerequisites**
Make sure you have [Python 3](https://www.python.org/) installed along with Chrome. Then, install the only required external package (`selenium`).
```bash
pip install -r requirements.txt
```
*(If pip fails, use `pip3 install -r requirements.txt` or `python3 -m pip install -r requirements.txt`)*

## 🚀 Usage

Execute the core script directly in your terminal:
```bash
python3 fb_poster.py
```

**Follow the Interactive the Terminal Constraints:**
1. **Supply URLs:** Hit `Enter` to input URLs, type zero characters and hit `Enter` to complete the list.
2. **Add Content:** Type your marketing copy. Type `END` on a new line when done.
3. **Select Media:** Drag your photo from the file-explorer and drop it into the terminal (optional).
4. **Manual Login phase:** A Chrome Instance will launch. Login manually in the browser, wait until the feed loads, and press `ENTER` back in the terminal.
5. **Confirmation Action:** A `✨ READY TO POST ✨` prompt secures the submission phase.

## ⚠️ Disclaimer
This tool is for educational purposes. Use it responsibly and do not use it to Spam. Ensure your interactions are compliant with [Facebook's Terms of Service](https://www.facebook.com/terms.php). 

## 🌐 Tags & SEO (For Developers)
`facebook-auto-poster` `python-facebook-bot` `selenium-python` `facebook-group-poster` `social-media-automation` `anti-ban` `python3`
