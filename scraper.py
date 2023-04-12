#product_code=input('Podaj kod produkry')
from bs4 import BeautifulSoup
import requests
import json

def get_element(ancestor,selector=None,attribute=None,return_list=False):
    try:
        if return_list:
            return [tag.text.strip() for tag in ancestor.select(selector)].copy()
        if not selector and attribute:
            return ancestor[attribute]
        if attribute:
            return ancestor.select_one(selector)[attribute].strip()
        return ancestor.select_one(selector).text.strip()
    except AttributeError:
        return None
    
selectors={
        'opinion_id':[None, 'data-entry-id'],
        'author':['span.user-post__author-name'],
        'recommendation':['span.user-post__author-recomendation>em'],
        'score':['span.user-post__score'],
        'purchased':['div.review-pz'],
        'published_at':['span.user-post__published > time:nth-child(1)','datetime'],
        'purchased_at':['span.user-post__published > time:nth-child(2)','datetime'],
        'thumbs_up':['button.vote-yes>span'],
        'thumbs_down':['button.vote-no>span'],
        'content':['div.user-post__text'],
        'pros':['div.review-feature__col:has(>div.review-feature__title--positives)>div.review-feature__item',None,True],
        'cons':['div.review-feature__col:has(>div.review-feature__title--negatives)>div.review-feature__item',None,True]




    }
product_code='96685108'
page_no=1
all_opinions=[]
while(page_no):
    url=f'https://www.ceneo.pl/{product_code}/opinie-{page_no}'
    print(url)
    respons=requests.get(url,allow_redirects=False)
    print(respons.status_code)
    if respons.status_code==301:
        
        page_no=None
        break
    page=BeautifulSoup(respons.text,'html.parser')
    opinions=page.select('div.js_product-review')
    for opinion in opinions:
        single_opinion={}
        for key,value in selectors.items():
            single_opinion[key]=get_element(opinion,*value)
        all_opinions.append(single_opinion)
    page_no+=1
with open(f'./opinions/{product_code}.json','w',encoding='UTF-8') as jf:
    json.dump(all_opinions,jf,indent=4,ensure_ascii=False) 

    
