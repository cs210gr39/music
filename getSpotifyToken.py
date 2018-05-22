import requests

client_id = 'efa8187291b04510a42a219b0d49efcc'
client_secret = '3e0fb3823d0045239c250db2a91f4054'

grant_type = 'client_credentials'

#Request based on Client Credentials Flow from https://developer.spotify.com/web-api/authorization-guide/

#Request body parameter: grant_type Value: Required. Set it to client_credentials
body_params = {'grant_type' : grant_type}

url='https://accounts.spotify.com/api/token'

response=requests.post(url, data=body_params, auth = (client_id, client_secret)) 
print(response.content)