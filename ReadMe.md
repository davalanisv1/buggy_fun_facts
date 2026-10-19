# Buggy Fun Facts

A small Flask-powered website that displays the insect of the day from the [Daily Insect blog](https://dailyinsect.wordpress.com/), including its common name, scientific name, image, and a fun fact. The page also has responsive styling and occasional glitch effects.

## Requirements

- Python 3
- Internet access, so the scraper can retrieve the source website

## Run locally

From the project root, create and activate a virtual environment, install the dependencies, and start Flask:

### Linux or macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m assets.PY.app
```

### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m assets.PY.app
```

Open <http://127.0.0.1:5000> in a browser. Keep the terminal process running while using the site; stop it with Ctrl+C.

> `index.html` uses `/api/insect` to retrieve data, so run it through Flask rather than opening the HTML file directly.

## Build a standalone Linux executable

The PyInstaller spec bundles the app, scraper dependencies, HTML, CSS, JavaScript, and local assets into a single Linux executable. Build it on Linux for the same CPU architecture as the computer where it will run.

```bash
source .venv/bin/activate
python -m pip install pyinstaller
pyinstaller --clean --noconfirm buggy-fun-facts.spec
```

Run the resulting `dist/BuggyFunFacts` executable. It starts the local web server and opens the website in your default browser. Keep the process running while using the site; press Ctrl+C in its terminal to stop it. The executable still needs internet access to retrieve the daily insect and its image.

This produces a standalone executable, not an AppImage. It bundles Python and project assets, but Linux systems may still need compatible system libraries and a browser.

## API
a
`GET /api/insect` returns JSON with these fields:

- `name` — common insect name
- `scientific_name` — scientific name
- `fun_fact` — short fact
- `image_url` — image URL, or `null` when one could not be found

If the source cannot be retrieved or parsed, the endpoint responds with an error status and message.

## Project layout

```text
.
├── index.html
├── requirements.txt
└── assets/
    ├── CSS/style.css
    ├── JS/app.js
    ├── JS/glitch.js
    ├── PY/app.py
    ├── PY/code.py
    ├── icons/
    └── images/
```

- `assets/PY/code.py` scrapes the Daily Insect page.
- `assets/PY/app.py` serves the website and JSON API.
- `assets/JS/app.js` loads the insect data into the page.
- `assets/JS/glitch.js` adds randomized visual effects. Effects are disabled when reduced motion is requested by the operating system or browser.
- `assets/CSS/style.css` contains the layout, appearance, and animation styles. The comments labeled **POSITION CONTROL** identify the CSS variables for adjusting the desktop panel positions.

## Notes

- The scraper depends on the Daily Insect website's current HTML structure; changes to that site may require updates to its selectors in `assets/PY/code.py`.
- Flask's built-in server is intended for local development, not production deployment.
