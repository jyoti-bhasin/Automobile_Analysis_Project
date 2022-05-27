from bs4 import BeautifulSoup
import requests
import pandas as pd

#store website in variable
website = "https://www.cars.com/shopping/results/?stock_type=cpo&makes%5B%5D=&models%5B%5D=&list_price_max=&maximum_distance=20&zip="

#get request
response = requests.get(website)
response.status_code

soup = BeautifulSoup(response.content, 'html.parser')

results = soup.find_all('div', {'class' : 'vehicle-card'})

#target necessary details
results[0].find('h2').get_text()
results[0].find('div', {'class': 'mileage'}).get_text()
results[0].find('div', {'class':'dealer-name'}).get_text().strip()
results[0].find('span', {'class':'sds-rating__count'}).get_text()
results[0].find('span', {'class':'sds-rating__link'}).get_text()
results[0].find('span', {'class':'primary-price'}).get_text()
name = []
mileage = []
dealer_name = []
rating = []
review_count = []
price = []

#Putting everything together inside a For-Loop
for result in results:

 # name
 try:
  name.append(result.find('h2').get_text())
 except:
  name.append('n/a')

 # mileage
 try:
  mileage.append(result.find('div', {'class': 'mileage'}).get_text())
 except:
  mileage.append('n/a')

 # dealer_name
 try:
  dealer_name.append(result.find('div', {'class': 'dealer-name'}).get_text().strip())
 except:
  dealer_name.append('n/a')

 # rating
 try:
  rating.append(result.find('span', {'class': 'sds-rating__count'}).get_text())
 except:
  rating.append('n/a')

 try:
  review_count.append(result.find('span', {'class': 'sds-rating__link'}).get_text())
 except:
  review_count.append('n/a')

  # price
 try:
  price.append(result.find('span', {'class': 'primary-price'}).get_text())
 except:
  price.append('n/a')

#Creating Pandas Dataframe

car_dealer = pd.DataFrame({'Name': name, 'Mileage':mileage, 'Dealer Name':dealer_name,
                                'Rating': rating, 'Review Count': review_count, 'Price': price})

#cleaning the data
car_dealer['Review Count'] = car_dealer['Review Count'].apply(lambda x: x.strip('reviews)').strip('('))

#extracting output in excel
car_dealer.to_excel('car_extracted_data.xlsx', index=False)
