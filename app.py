from urllib import response
from flask import Flask, render_template, request, redirect,url_for,flash,jsonify
import requests
import json




app=Flask(__name__)
@app.route('/wether', methods =['GET','POST'])
def Index():
  url = "http://community-open-weather-map.p.rapidapi.com/weather"

  querystring = {"q":"eskisehir,tr","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"imperial","mode":"xml"}

  headers = {
	"X-RapidAPI-Key": "3c9c612023mshf6a56703440bce7p191ef7jsn762b115dd251",
	"X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com"
   }

  response = requests.request("GET", url, headers=headers, params=querystring,verify=False)
 
  return render_template('index.html', title="page", context=response.text)


@app.route('/', methods =['GET','POST'])
def weather():
    url = ('https://newsapi.org/v2/everything?'
       'q=Gold&'
       'from=2022-06-10&'
       'sortBy=popularity&'
       'language=en&'
       'apiKey=2fa1ddd1e3b349639d3e63cc6fbdeef2')

    response = requests.get(url,verify=False)
    listofResponse=response.json()
    
    articles=listofResponse["articles"]
    
    desc = []
    news = []
    img = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
 
    mylist = zip(news, desc, img)
 
   
    
    return render_template('index.html', title="page", context=mylist)

if(__name__ == "__main__"):
 app.run(debug=True)