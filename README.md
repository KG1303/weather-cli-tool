# weather-cli-tool
Lightweight Python CLI tool to get instant weather reports via wttr.in. Supports, multiple languages and cities.
## Key features
* **Weather forecast:** real-time weather forecast.
* **Simple use:** you can use it by 1 line in terminal.
## Tech Stack
* Python 3.12
* Requests
* Argparse
## Installation(option 1: Direct run)
1. **Clone the repository:**
``` bash
git clone https://github.com/KG1303/weather-cli-tool.git [<directory-name>]
cd <directory-name>
```
2. **Set up virtual environment:**
``` bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```
3. **Install requirements:**
``` bash
pip install -r requirements.txt
```
4. **Run it:**
``` bash
python main.py
```
## Installation(option 2: Global Command)
1. **Do the installation(option 1), but don't run the file**
2. **In the project folder open terminal and run this command:**
``` bash
pip install .
```
*P.S. You need to install git and python 3.x before installing.*  

## Use
By default it shows weather in Barcelona in English. But with adding `--city` and `--lang`(after these you put language and city name) you can get weather in different cities and in different languages.
## Licence
MIT Licence. Created for educational purposes.