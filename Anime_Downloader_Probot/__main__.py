import glob
import logging
from pathlib import Path
from Anime_Downloader_Probot.helper import load_plugins
from Anime_Downloader_Probot import GogoAnime

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

path = "Anime_Downloader_Probot/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Anime Downloader Probot")
print("Now is UP")

if __name__ == "__main__":
    GogoAnime.run_until_disconnected()
