import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--city', default=None, help='city filtering (default: None)')
args = parser.parse_args()

class Brawery:
	def __init__(self, A):
		self.idd = A[0]
		self.name = A[1]
		self.brewery_type = A[2]
		self.address_1 = A[3]
		self.address_2 = A[4]
		self.address_3 = A[5]
		self.city = A[6]
		self.state_province = A[7]
		self.postal_code = A[8]
		self.country = A[9]
		self.longitude = A[10]
		self.latitude = A[11]
		self.phone = A[12]
		self.website_url = A[13]
		self.state = A[14]
		self.street = A[15]
	
	def __str__(self):
		return f"Browar '{self.name}' typu '{self.brewery_type}' o numerze identyfikacyjnym {self.idd}, o adresie: '{self.address_1}, {self.address_2}, {self.address_3}'. Siedziba zlokalizowana w '{self.city}, {self.state_province}, {self.postal_code}, {self.country}'. Położenie geograficzne: {self.longitude} {self.latitude}. Telefon: {self.phone}. Strona internetowa: {self.website_url}. Stan: '{self.state}', ulica '{self.street}'."

def main(city=args.city):
	if city==None:
		link = 'https://api.openbrewerydb.org/v1/breweries/random?size=20'
	else:
		link = 'https://api.openbrewerydb.org/v1/breweries?by_city='+city.lower()+'&per_page=20'
	f = requests.get(link)
	page = f.json()
	if len(page) < 1 or 'message' in page and page['message']=="Couldn't find Brewery":
		print("Couldn't find Brewery")
		return
	for i in range(min(20,len(page))):
		i = Brawery([page[i][j] for j in page[i]])
		print(i)

if __name__ == '__main__':
	main()
