# Import the required libraries
import requests
import json
import csv
import time
import os
import boto3
from secret_key import access_key, secret_access_key

# URL to access the weather API
url1 = "http://api.openweathermap.org/data/2.5/weather?q=Dallas&APPID=1be04b0c33773567284468873f8acc46"
url2 = "http://api.openweathermap.org/data/2.5/weather?q=Detroit,us&APPID=1be04b0c33773567284468873f8acc46"

# Save the response of weather API
response1 = requests.get(url1)
response2 = requests.get(url2)

x1 = response1.json()
x2 = response2.json()

# Extract weather components from the API reponse
y1 = x1["main"]
y2 = x2["main"]

z1 = x1["weather"]
z2 = x2["weather"]

#Append the current weather data for today to the Weather.csv file
with open('Weather.csv', mode='a') as weather_file:

    weather_writer = csv.writer(weather_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n")
    if weather_file.tell() == 3:
        weather_writer.writerow(['Location', 'Temperature(in Kelvin)', 'Pressure(in hPa)', 'Humidity(in Percentage)', 'Weather', 'Date'])
    weather_writer.writerow(['Dallas', str(y1["temp"]), str(y1["pressure"]), str(y1["humidity"]), str(z1[0]["description"]), time.strftime("%d %b %Y", time.localtime(x1["dt"]))])
    weather_writer.writerow(['Detroit', str(y2["temp"]), str(y2["pressure"]), str(y2["humidity"]), str(z2[0]["description"]), time.strftime("%d %b %Y", time.localtime(x2["dt"]))])

# Upload the updated Weather.csv file to S3 bucket
client = boto3.client("s3",
                      aws_access_key_id = access_key,
                      aws_secret_access_key = secret_access_key)

for file in os.listdir():
    if "Weather.csv" in file:
        upload_file_bucket = "weatherbucket1408"
        upload_file_key = "python3/" + str(file)
        client.upload_file(file,upload_file_bucket,upload_file_key)
        print("###SUCCESSFULLY UPLOADED###")
