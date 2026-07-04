from secrets import randbits

import requests
from fastapi import FastAPI,Request
from Model import Url,Entry

from fastapi.middleware.cors import CORSMiddleware
from DBQuery import search,insert


import requests

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],allow_methods=["*"],allow_headers=["*"])

def shorten():
    bit = randbits(32)
    temp = bit
    short = ""
    code = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while bit > 0:
        remainder = bit % 62
        short += code[remainder]
        bit //= 62
    while search(short):
        bit = temp+1
        short = ""
        while bit > 0:
            remainder = bit % 62
            short += code[remainder]
            bit //= 62
    return short


# change url
@app.get("/api/short_url")
def short_url():
    return Url(short_url="http://FellowStrawHat/"+shorten())

@app.post("/api/submit_url")
def submit_url(entry:Entry):
    try:
        respond = requests.get(entry.long_url)
    except :
        return {"status": False, "message": "The URL you entered is invalid"}

    if respond.status_code >= 400 :
        return {"status":False, "message":"The URL you entered is invalid"}
    if insert(entry.short_url, entry.long_url, "india"):
        return { "status":True, "message":"The URL you entered is valid"}
    else:
        return { "status":False, "message":"The URL you entered is already present in database"}