from typing import Optional, List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from hkr_quick_hints import HKRQuickHints

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/hkr/uploadspoiler/")
async def hkr_upload_spoiler(files: List[UploadFile] = File(...)):
    spoiler_log = str(await files[0].read())
    dreamer_locs = HKRQuickHints(spoiler_log).dreamer_locs

    return {"data": dreamer_locs}


# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action="/hkr/uploadspoiler/" enctype="multipart/form-data" method="post">
# <input name="files" type="file">
# <input type="submit">
# </form>
# </body>
#     """
#     return HTMLResponse(content=content)
