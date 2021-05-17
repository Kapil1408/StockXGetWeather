#GetWeather

This document provides the directions to this project and explains its execution.

## Contents of the repository
The Git repository StockXGetWeather contains the following files:
  1. AWS S3 bucketinfo.rtf - Contains info about the AWS bucket used in this project to upload weather data as well as the login info for the IAM user created for StockX.
  2. GetWeather.py - Python script that leverages OpenWeatherMap API to pull in current weather data for two locations(Dallas and Detroit) and appends it to the file Weather.csv. It also uploads the file to the S3 bucket.
  3. Weather.csv - This is the output file that contains the weather data for the above two cities. The GetWeather.py script has been ran once for the last 7 days, so this file contains weather data for the last 7 days.
  4. secret_key.py - Contains secret key to access S3 through the code to upload the Weather.csv file
  5. requirements.txt - Contains the packages leveraged in the GetWeather.py script. These would need to be installed for successful execution of this script.

## Installation & Execution & Verification Steps
  1. Clone the Git repository into a folder on your local machine
  2. On your local machine, navigate to that folder and open the Weather.csv file to check the contents in it. Note that it contains last 7 days of weather data for Dallas and Detroit.
      **NOTE:** Do not alter or change the contents of Weather.csv file.
  3. Log in to AWS Management Console using the IAM credentials provided in the AWS S3 bucketinfo.rtf file. Check the contents of the Weather.csv file in the bucket(weatherbucket1408) matches the contents of the file on your local machine.
  4. Open terminal and navigate to the folder in which the repository has been cloned
  5. Install the packages required to run the script GetWeather.py using the below command:
        pip install -r requirements.txt
  6. Run the GetWeather.py script using the below command:
        python GetWeather.py
  7. Verify that 2 more rows have been appended to the Weather.csv file in both the places(your local machine & AWS S3 bucket) with the current weather data for both the cities.

## DDL for AWS Aurora MySQL table
  CREATE TABLE Weather(
  Location VARCHAR(100) NOT NULL,
  Temperature(in Kelvin) FLOAT(3,2) NOT NULL,
  Pressure(in hPa) FLOAT(3,2) NOT NULL,
  Humidity(in Percentage) FLOAT(3,2) NOT NULL,
  Weather VARCHAR(100) NOT NULL,
  Date DATE NOT NULL
  );

## Command to load from S3 to SQL
  LOAD DATA FROM S3 'https://weatherbucket1408.s3.us-east-2.amazonaws.com/python3/Weather.csv'
    INTO TABLE Weather
    FIELDS TERMINATED BY ','
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (Location, Temperature(in Kelvin), Pressure(in hPa), Humidity(in Percentage), Weather, Date);
