import bs4 as bs
import urllib.request

source = urllib.request.urlopen('https://forecast.weather.gov/MapClick.php?textField1=38.975318&textField2=-77.480407').read()
soup = bs.BeautifulSoup(source,'lxml')

class current_forcast:
    """Overall class to monitor the forcast"""

    def current_number_numbers():
        current_weather = soup.find('p', class_="myforecast-current-lrg")
        weather_number = current_weather.text
        return(weather_number)

    def current_weather_words():
        current_weather_word = soup.find('p', class_="myforecast-current")
        weather_word = current_weather_word.text
        return(weather_word)

    """def current_weather_time():
        current_weather_time = soup.find_all('td')[-1]
        wordss = current_weather_time.text
        print(wordss)
        wordss.strip()
        return(wordss)"""
