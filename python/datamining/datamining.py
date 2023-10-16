import scrapy
from scrapy.selector import Selector
import json

lieu_du_taf = []
date_candidature = []
poste1 = []
total = []


class RocheeSpider(scrapy.Spider):
    name = 'rochee'
    allowed_domains = ['roche.com']
    #modifier l'url de début et ajouter la page selon la structure adaptée
    #start_urls = ['http://https://www.emploi.leem.org//'], on peut séparer en str1 + {} + str2 ou {} contient le numéro de page dans un format
    #ajout d'un for i in range(0,pagenumber)
    start_urls = ['https://www.roche.com/toolbox/jobSearch.json?utm_medium=cpc&utm_source=google&utm_campaign=generationext&utm_content=students&type=json&api=jobs&pageLength=15&locale=en&jobLevelCodes=ENTRY_LEVEL&orderByType=desc&orderBy=openDate&offset=1']



    #élément modifiable
    name = 'leem'
    allowed_domains = ['https://www.emploi.leem.org/']

    start_urls = ['http://https://www.emploi.leem.org//']

    total = []
    
    print('\n\n_______________________________\n\n',total)
    
    '''
    lieu_du_taf = []
    date_candidature = []
    poste1 = []'''

    def parse(self, response):
        print('\n nouvelle itération \n')
        #results = json.loads(response)
        #for result in results:
        #    print(result)
        
        nbpost = 1000
        nbpage = 10
            
        urls = []
        total = []
        
               
        for i in range(nbpage):
            urls.append( 'https://www.roche.com/toolbox/jobSearch.json?utm_medium=cpc&utm_source=google&utm_campaign=generationext&utm_content=students&type=json&api=jobs&pageLength=15&locale=en&jobLevelCodes=ENTRY_LEVEL&orderByType=desc&orderBy=openDate&offset={}'.format(i))
        
        for y in range(nbpage):  
            print('\n\n sanofi ' +str(y)+ '    \n\n')            
            yield scrapy.Request(urls[y], callback=self.parse_2)
            print('\n\n sanofi ' +str(y)+ '    \n\n')
            
        print('__________________________________________________________________________________________________________________________')
            
        
        
    def parse_2(self, response):
    
        '''class=\"job-location\"'''
        #obtenir le poste
        poste = response.xpath('//li//h2/text()').extract()
        #obtenir le lieu du job
        response.xpath('').extract
        lieu_du_job_et_date = response.xpath('//li//span/text()').extract()
        #obtenir date du job        
        #tout = 'poste {}  lieu {}  date{}'.format(poste, lieu_du_job, date_candidature)
        
        
        
        nbpost = 100
        
        for i in range(nbpost):
            try:
                lieu_du_taf.append(lieu_du_job_et_date[i*2])
                date_candidature.append(lieu_du_job_et_date[i*2+1])
                poste1.append(poste[i])

            except IndexError:
                pass
        '''
        yield {'lieu': lieu_du_taf[a]
               'date_candidature': date_candidature[a]
               'poste': poste1[a]}'''       
               
        for a in range(len(date_candidature)):
            total.append('lieu du taf {} date de candidature {} pour le poste {}'.format(lieu_du_taf[a], date_candidature[a], poste1[a]))
            #print(list(set(total)))
            #print(len(total)-len(list(set(total))))
            #print('                                              ', len(list(set(total))))
            #print('lieu du taf {} date de candidature {} pour le poste {}'.format(lieu_du_taf[a], date_candidature[a], poste1[a]))
            
            yield {'lieu_du_taf ' : lieu_du_taf[a],
                    'date_candidature' : date_candidature[a],
                    'poste' : poste1[a]}
                
       

        
print('\n\n_______________________________\n\n',total)

            
                
     
        

   
