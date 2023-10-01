import pygsheets as sheets

client = sheets.authorize(
    client_secret='/Users/herrn/Documents/keys/fpl-enhanced.json'
)

ss = client.open('FPL Data Enhanced')


