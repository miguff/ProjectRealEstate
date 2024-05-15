import requests

url = "https://ingatlan.com/lista/elado+lakas+10-mFt-tol"

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "hu,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,af;q=0.6",
    "Cache-Control": "max-age=0",
    "Cookie": "advCC=2405143851533583471220; _cfuvid=lCiLovpx.dbfPj_tXwc55WL2w7gy90yhiAFWn2aNfNw-1715723717400-0.0.1.1-604800000; CookieConsent={stamp:%27bsbAh0S+8GJxApxrZ0vTRlMm4vdAjbb28/R2BJ1175X//1yp8tvPYg==%27%2Cnecessary:true%2Cpreferences:false%2Cstatistics:false%2Cmarketing:false%2Cmethod:%27explicit%27%2Cver:2%2Cutc:1715723726358%2Ciab2:%27CP-mp8AP-mp8ACGABBENAzEgAAAAAEPgAAAAAAAUVALMNCogDrAkJCDQMIoEAKgrCAigQAAAAkDRAQAmDAp2BgEusJEAIAUAAwQAgABRkACAAACABCIAIACgQAAQCBQAAgAQCAQAEDAACACwEAgABAdAhTAggUCwASMyIhTAhCgSCAlsqEEgCBBXCEIs8ACAREwUAAAAABWAAICwWBxJICVCQQJcQbQAAEACAQQgVCCTkwABAkbLUHgibRlaQBoacJAA.YAAAAAAAAAAA%27%2Cgacm:%272~AA==fmR2Lg==AAAAAAAAAABCAABAAAgAIAAABAAAAAAACAAAAAAAAAAQAAAAAAABABAAAAAAAAAAAAAAAQAAAAAAAAAAAgMAAAAAAAgAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAQAAAAAAFAAAAAAAAAAAAAAAAABAAAAAAAAAAACAAABAAAAAAAAAAAAAAAAAABAQAAAEAAAAAAAAAAAAAAAAAAACBAAAAAAAAAAAAQAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAACAgBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAgAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAkQAAAAAAAAAAAAAAAAQ=%27%2Cregion:%27pt%27}; g_state={'i_p':1715730926848,'i_l':1}; cf_clearance=QooNs95VRbgoEXmiYoi99QfM3eigTAd1yBuCAvJ3bFw-1715723749-1.0.1.1-RSAk2Tj6sk4vj6CtxBoxLP37t1jOMdWkxNxCYmb3GBdGlCndJ8Scz2yXO9o218GqfDMM9TML5szt30EbS5MuUQ; _goa3=eyJ1IjoiMjQwNTE0ODI5OTQxNDUyMzk3NzIyNSIsImgiOiJhODktMTU1LTE3My0xOTUuY3BlLm5ldGNhYm8ucHQiLCJzIjoxNzE1NzIzNzYyODA3fQ==; _goa3TC=e30=; _goa3TS=e30=; bbid=9138794815725923; last_location=Budapest V. kerület; PHPSESSID=e7d49bb463af993d87e3119c2aba11f9; _goa3B=eyJjaHJvbWUiOnRydWUsInZlcnNpb24iOiI5OS4wLjAuMCIsIndlYmtpdCI6dHJ1ZSwiZnVsbFZlcnNpb25zIjpbeyJicmFuZCI6IkNocm9taXVtIiwidmVyc2lvbiI6IjEyNC4wLjYzNjcuMjAxIn0seyJicmFuZCI6Ik1pY3Jvc29mdCBFZGdlIiwidmVyc2lvbiI6IjEyNC4wLjI0NzguOTcifSx7ImJyYW5kIjoiTm90LUEuQnJhbmQiLCJ2ZXJzaW9uIjoiOTkuMC4wLjAifV0sImFyY2hpdGVjdHVyZSI6Ing4NiIsImJpdG5lc3MiOiI2NCIsIm1vZGVsIjoiIiwicGxhdGZvcm0iOiJXaW5kb3dzIiwicGxhdGZvcm1WZXJzaW9uIjoiMTUuMC4wIn0=; _goa3GDPR=eyJnIjp0cnVlLCJjIjoiQ1AtbXA4QVAtbXA4QUNHQUJCRU5BekVnQUFBQUFFUGdBQUFBQUFBVVZBTE1OQ29nRHJBa0pDRFFNSW9FQUtnckNBaWdRQUFBQWtEUkFRQW1EQXAyQmdFdXNKRUFJQVVBQXdRQWdBQlJrQUNBQUFDQUJDSUFJQUNnUUFBUUNCUUFBZ0FRQ0FRQUVEQUFDQUN3RUFnQUJBZEFoVEFnZ1VDd0FTTXlJaFRBaENnU0NBbHNxRUVnQ0JCWENFSXM4QUNBUkV3VUFBQUFBQldBQUlDd1dCeEpJQ1ZDUVFKY1FiUUFBRUFDQVFRZ1ZDQ1Rrd0FCQWtiTFVIZ2liUmxhUUJvYWNKQUEuWUFBQUFBQUFBQUFBIiwidCI6MTcxNTcyODIyMzc2MX0=; AWSALB=hySd9xtyhDVpq8Y+SzmTIeWGgt6HK5JJBUxGm/XeuqDZJ0JLVz/B6rlJt/EAGkV5w6tSeEy2KW3QFN6q7Tt3KloMqilerPTHoCaTUYs/0OIlzjel5BAEr+7++ce5; AWSALBCORS=hySd9xtyhDVpq8Y+SzmTIeWGgt6HK5JJBUxGm/XeuqDZJ0JLVz/B6rlJt/EAGkV5w6tSeEy2KW3QFN6q7Tt3KloMqilerPTHoCaTUYs/0OIlzjel5BAEr+7++ce5; __eoi=ID=e4f9c6cfbf7e5168:T=1715723763:RT=1715728226:S=AA-AfjYKjSM2yH9FXXqbHH2bSTHu",
    "Referer": "https://ingatlan.com/?gad_source=1&gclid=CjwKCAjwl4yyBhAgEiwADSEjeDojCP-vNU4AEuQ82eeCOi8AzBZCD2Ow-C7xeEs5BY1QOz7Z2Qt7HBoCj7QQAvD_BwE",
    "Sec-Ch-Ua": "\"Chromium\";v=\"124\", \"Microsoft Edge\";v=\"124\", \"Not-A.Brand\";v=\"99\"",
    "Sec-Ch-Ua-Arch": "\"x86\"",
    "Sec-Ch-Ua-Bitness": "\"64\"",
    "Sec-Ch-Ua-Full-Version": "\"124.0.2478.97\"",
    "Sec-Ch-Ua-Full-Version-List": "\"Chromium\";v=\"124.0.6367.201\", \"Microsoft Edge\";v=\"124.0.2478.97\", \"Not-A.Brand\";v=\"99.0.0.0\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Model": "\"\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Ch-Ua-Platform-Version": "\"15.0.0\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0"
}



with open("this_is_a_test.html", "wb") as f:
    r = requests.get(url, headers=headers)
    f.write(r.content)
    print(r.ok)