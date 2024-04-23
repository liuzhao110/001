__author__ = 'liusir'
import requests

url="https://v1.kwaicdn.com/ksc2/n1MDeh6CK6o7TIL2SBgdyOLJITy-DtTtrajxC9RktU0zWMnB8B1bQg9ijsz5GZFXkvYI55XitWbCITgnZf5gQCkMqJGpe8ZqLi0QUYxUsRfGimalf9eTgC8HETVZTos2.mp4?pkey=AAXpoyycfyiP3MCbgSVXH9UxVJNQ8_6kfVwl4qLkxPVsq-jaMegAIkOF1z7KiM_JfVIOEHsH-pEKIjGgF7svWEWDSyivPbNCc_eZJvs-LuhfKqWirUfvMr_MHOx8gP7Tf3g&tag=1-1713793087-unknown-0-tibhtlieoj-057a4d6c7073062f&clientCacheKey=3x9cned4b3v3qkc_64df1dea&di=1cb43b5&bp=14944&tt=hd15&ss=vp"

res = requests.get(url)

open("kuaishou1号.mp4","wb").write(res.content)