import os
DEV = os.environ.get("UPSTREAM_REPO", None)

if DEV == "Dev":
  import os
  os.system("git clone -b Dev https://github.com/InternetAmethyst/Ultroid.git && cd Ultroid && python3 -m pyUltroid")
else:
  import os
  os.system("git clone https://github.com/InternetAmethyst/Ultroid && cd Ultroid && python3 -m pyUltroid")
