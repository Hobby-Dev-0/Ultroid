import os
DEV = os.environ.get("UPSTREAM_REPO", None)
SED = "Dev" or "DEV" or "dev"
if DEV == SED:
  import os
  os.system("git clone -b dev https://github.com/InternetAmethyst/Ultroid.git && cd Ultroid && pip3 install py-Ultroid==62.0b0 && python3 -m pyUltroid")
else:
  import os
  os.system("git clone https://github.com/InternetAmethyst/Ultroid && cd Ultroid && python3 -m pyUltroid")
