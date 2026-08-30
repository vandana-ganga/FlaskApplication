# Flask Application

A simple web application that runs on your own computer and responds to visitors through a web browser.
It has two pages: a welcome page that greets anyone who opens the site, and a health page that confirms
the app is switched on and working properly. The health page is the kind of check a monitoring tool would
use to make sure a website has not gone down. Everything runs locally, so nothing is sent over the internet.

---

## Installation and Setup

Follow these steps in order. Every command is written out in full.

### 1. Download the project

```bash
git clone https://github.com/vandana-ganga/FlaskApplication.git
cd FlaskApplication
```

### 2. Create a virtual environment

A virtual environment keeps this project's packages separate from the rest of your computer.

**Windows (PowerShell):**

```powershell
py -m venv venv
```

**macOS / Linux:**

```bash
python3 -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
source venv/bin/activate
```

Your command prompt will now start with `(venv)`.

> **If Windows blocks the activation** with the message *"running scripts is disabled on this system"*,
> run this once, then try activating again:
>
> ```powershell
> Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
> ```

### 4. Install the required packages

```bash
pip install -r requirements.txt
```

### 5. Start the application

```bash
python app.py
```

You should see output ending with:

```
* Running on http://127.0.0.1:5000
```

### 6. Open it in your browser

Visit **http://localhost:5000/** and **http://localhost:5000/health**

To stop the server, press `Ctrl + C` in the terminal. To leave the virtual environment, type `deactivate`.

---

## API Endpoint Reference

| Endpoint | URL | Method | Description | Example Response |
|----------|-----|--------|-------------|------------------|
| Home | `http://localhost:5000/` | `GET` | Returns the welcome page shown to any visitor who opens the site. | `200 OK` — an HTML page displaying **Welcome to the App** |
| Health check | `http://localhost:5000/health` | `GET` | Reports whether the application is up and responding. Used to confirm the server is alive. | `200 OK` — an HTML page displaying **App is running** |

### Testing with Postman

1. Open Postman and create a new request.
2. Set the method to `GET`.
3. Enter `http://localhost:5000/` and press **Send** — you should get status `200 OK`.
4. Repeat with `http://localhost:5000/health`.

---

## Git Workflow

This project uses two branches to keep finished work separate from work in progress.

**`dev`** is the working branch. Every change gets built and committed here first, so mistakes never touch
the released version. **`main`** is the release branch. It only receives code from `dev` once that code has
been tested and confirmed working, which means `main` is always safe to download and run.

The cycle for each release is the same: build the feature on `dev`, commit it, push `dev` to GitHub, then
switch to `main` and merge `dev` into it. That way `main` moves forward one tested release at a time.

```
dev    ──●────────●──────────────●────────●─────────▶
         │        │              │        │
      initial   endpoints     README   version 2
      commit    added         added     features
                  │                       │
                  │ merge                 │ merge
                  ▼                       ▼
main   ───────────●───────────────────────●─────────▶
                Version 1              Version 2
```

### Commands used

```bash
git init                       # start version control in the project folder
git checkout -b dev            # create the dev branch and switch to it
git add .                      # stage the files
git commit -m "message"        # save a snapshot with a description
git push origin dev            # upload dev to GitHub

git checkout main              # switch to the release branch
git merge dev                  # bring the tested work across
git push origin main           # upload main to GitHub
```

---

## Version History

| Version | Branch merged | What it included |
|---------|---------------|------------------|
| **Version 1** | `dev` → `main` | Initial project setup with a virtual environment and `.gitignore`. Flask application (`app.py`) serving two working endpoints: `/` returning **Welcome to the App** and `/health` returning **App is running**. HTML templates for both pages. `requirements.txt` listing all dependencies. |
| **Version 2** | `dev` → `main` | _To be completed._ |

---

## Screenshots

### Application running in the browser

![The Flask app running at localhost:5000](screenshots/app-running.png)

### GitHub repository showing the dev and main branches

![The repository branch list showing both dev and main](screenshots/branches.png)

### Commit and merge history for Version 1 and Version 2

![Commit history showing the Version 1 and Version 2 merges](screenshots/commit-history.png)

---

## Project Structure

```
FlaskApplication/
├── app.py                 # the application and its two endpoints
├── requirements.txt       # list of packages needed to run it
├── templates/
│   ├── index.html         # the welcome page
│   └── health.html        # the health check page
├── screenshots/           # images used in this README
├── .gitignore             # files Git should ignore
└── README.md              # this file
```

---

## Built With

- **Python 3.11**
- **Flask 3.1.3** — the web framework that handles the endpoints
