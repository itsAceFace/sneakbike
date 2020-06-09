import os
import sys
import json
from pathlib import Path

# Make dir if not exists.
obs_path = os.path.expanduser("~/Sneakbike_Profile")
Path(obs_path).mkdir(parents=True, exist_ok=True)

# The IP addr + port.  "xxx.xxx.xxx.xxx:pppp"
ip_addr = sys.argv[1]

# Templates
sneaksnake_ini = """[General]
Name=SneakSnake

[Video]
BaseCX=800
BaseCY=600
OutputCX=800
OutputCY=600
FPSType=0
FPSCommon=60

[SimpleOutput]
VBitrate=1500
StreamEncoder=nvenc
RecEncoder=nvenc
RecQuality=Small

[Output]
Mode=Simple

[AdvOut]
TrackIndex=1
RecType=Standard
RecTracks=1
FLVTrack=1
FFOutputToFile=true
FFFormat=
FFFormatMimeType=
FFVEncoderId=0
FFVEncoder=
FFAEncoderId=0
FFAEncoder=
FFAudioMixes=1

[Audio]
ChannelSetup=Mono"""

service_json = {
    "settings": {
        "bwtest": False,
        "key": "weenis",
        "server": f"rtmp://{ip_addr}/live",
        "use_auth": False
    },
    "type": "rtmp_custom"
}

with open(os.path.join(obs_path, "basic.ini"), "w+") as bi:
    bi.write(sneaksnake_ini)

with open(os.path.join(obs_path, "service.json"), "w+") as sj:
    json.dump(service_json, sj)
