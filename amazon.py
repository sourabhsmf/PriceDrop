from bs4 import BeautifulSoup
from googlesearch import search
from fake_useragent import UserAgent
import requests
import re


class AmazonScrapper():
    ''' AmazonScrapper is class that find the product
       details including availablity, price and quantity
       from amazon.in
    '''

    def __init__(self, productName, countryExtension):

        # Initilizing the product name and country extension
        self.productName = productName.strip()
        self.countryExtension = countryExtension.strip()

        # Initilizing the productDetails to a empty dictonary
        self.productDetails = []

    @staticmethod
    def getUserAgent():
        ''' Returns a string which has information
        about user agent
        '''
        userAgent = ''
        # Useragent need to be specified in every request
        # otherwise amazon may think that the request is
        # made by machine
        try:
            
            ua = UserAgent()
            userAgent = ua.random
            
        except Exception as e:

            userAgent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15'\
                        '(KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'
        return userAgent
    

    def googleResults(self, searchQuery):
        '''(str) --> list

        Returns a generator which consists list
        of amazon link for the searched products

        '''
        amazonLinks = []

        # Compile the regular expression object as
        # it is used multiple time
        # It improves the performance
        pattern = re.compile(r'(https|http):((//)|(\\\\))+www.amazon.in[\w]*')
        
        # Store the top google search result
        # search(query, num,....) return a generator
        googleResults = search(query=searchQuery, stop=10)

        for link in googleResults:
            if re.match(pattern, link) is not None:
                amazonLinks.append(link)
                
        return amazonLinks
    
    def search(self):
        '''() --> dictonary

        search method is used to search for the product
        in the amazon.in

        >>> amazonScrapper = AmazonScrapper('xyz', 'in')
        >>> amazonScapper.search()
        {'productName':'xyz', 'price':'101', 'availablity':True....}
        '''

        # searchQuery is the string that need to be googled
        # to get the different amazon urls of the product
        searchQuery = self.productName + ' amazon.' + self.countryExtension

        try:
            
            # Store the top google search result
            # search(query, num,....) return a generator
            googleResults = search(query=searchQuery, stop=1)
           
            amazonProductURL = next(googleResults)

            userAgent = AmazonScrapper.getUserAgent()
            
            # Set the header with the User-Agent
            header = {'User-Agent': str(userAgent)}


            # GET request to the amazon url
            # and also to store the html DOM from the response
            htmlPage = requests.get(url=amazonProductURL, headers=header).content

            # Create a BeautifulSoup object that can be used
            # for scrapping
            bs = BeautifulSoup(htmlPage, 'html.parser')

            # Store the div with id = resultsCol
            # This div has all the products
            resultsCol = bs.find('div', {'id':'resultsCol'})

            if resultsCol is not None:
                
                # Store unordered list with id = s-results-list-atf
                ul = resultsCol.find('ul', {'id': 's-results-list-atf'})

                # Store all the childrens of unordered list
                ulChild = ul.children

                # Loop over different clildren tags to get the
                # product details including product name,
                # price, discount, etc

                for element in ulChild:
                    product = {}
                    product['url'] = element.select('div div div a')[0]['href']
                    product['product'] = element.h2.get_text()
                    product['price'] = element.find('span', {'class': ['a-size-base', 'a-color-price', 's-price', 'a-text-bold']}).get_text().strip()
                    originalPrice = element.find('span', {'class':'a-text-strike'})
                    
                    if originalPrice is None:
                        product['originalPrice'] = ''
                    else:
                        product['originalPrice'] = originalPrice.get_text().strip()
                        
                    self.productDetails.append(product)

                return self.productDetails
            
            else:
                
                product = {}
                
                # Store the product title
                product['product'] = bs.find('span', {'id' : 'productTitle'}).get_text().strip()
                product['url'] = amazonProductURL
                notAvailability = bs.find('div', {'id' : 'availability'})

                if notAvailability is not None:
                    
                    product['price'] = 'n/a'
                    product['originalPrice'] = 'n/a'
                    
                else:
                    product['originalPrice'] = bs.find('span', {'class' : 'a-text-strike'}).get_text().strip()
                    product['price'] = bs.find('span', {'id' : 'priceblock_ourprice'}).get_text().strip()

                self.productDetails.append(product)

        except Exception as e:
            
            print(e)
            
        return self.productDetails
            
