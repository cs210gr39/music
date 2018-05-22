import requests
import json


#TAKING THE SONG INFORMATION FROM SPOTIFY API
myBearer ='Bearer BQAQ2Sii7zRZRMPqWRJEjE-2hJjCcDV3hMXb6GMmZL9tFiuQoyCL1ru7qkhyldn2LqOvmMto7KLu82i-iWA'
file=open("results.txt","w",encoding="utf8")
with open("toApi.txt", "r",encoding="utf8") as ins:
    array = []
    cnt = 0;
    for line in ins:
        array.append(line)
    for i in range(0,54*600,600) :
        subArr = array[i:i+600]
        tempoSum=0;
        countryName=""
        for line in subArr :
            splittedArray = line.split(" ")
            countryName=splittedArray[2]
            url = splittedArray[0]
            splittedUrl=url.split("/")
            length=len(splittedUrl)
            trackID =splittedUrl[length-1]
            response = requests.get("https://api.spotify.com/v1/audio-features/"+trackID,headers={'Authorization': myBearer})
            #print(response)
            songinfo = response.content
            j = json.loads(songinfo)
            tempoOfSong =j['tempo']
            tempoSum = tempoSum + int(tempoOfSong)
        tempoAvg=(1.0*tempoSum)/600.0
        print(countryName[:-1] + "," +str(tempoAvg))
        toWrite=countryName[:-1] + "," +str(tempoAvg) +"\n"
        file.write(toWrite)

#SPLITTING DATA     
     print(len(array))
    outputArray =[]
    for el in array :
    	alArr=el.split(" ")
    	length=len(alArr)
    	myStr=alArr[length-3] + " " + alArr[length-1]
    	outputArray.append(myStr)
    print(len(outputArray))
    file=open("output.txt","w")
    for outLine in outputArray :
    	file.write(outLine)



#TAKING THE AUTHORIZATION KEY
countries = ['ec' ,'fr' ,'ar', 'fi', 'no', 'it', 'lt', 'ph' ,'tw', 'nz', 'ee', 'tr', 'us', 'sv','cr', 'de', 'cl', 'jp', 'br', 'hn', 'gt', 'ch', 'hu', 'ca', 'pe', 'be', 'my', 'dk',
 'bo', 'pl', 'at', 'pt', 'se', 'mx', 'pa', 'uy', 'is', 'es', 'cz', 'ie', 'nl', 'sk',
 'co' ,'sg' ,'id' ,'do' ,'lu' ,'gb' ,'global' ,'py' ,'au' ,'lv' ,'gr', 'hk']
print(len(countries))





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

