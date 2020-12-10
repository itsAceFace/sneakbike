from typing import Optional, List
import json

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel  # pylint: disable=no-name-in-module

from hkr_quick_hints import DreamerSpoiler

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class HKRSpoilerUpload(BaseModel):
    files: str


@app.post("/api/hkr/uploadspoiler/")
async def hkr_upload_spoiler(data: HKRSpoilerUpload):
    ds = DreamerSpoiler(data.files)

    payload = {
        "dreamers": ds.dreamers,
        "basic_abilities": ds.basic_abilities,
        "advanced_abilities": ds.advanced_abilities,
        "standard_items": ds.standard_items,
        "other_keys": ds.other_keys,
        "pale_ore": ds.pale_ore,
    }

    return payload

