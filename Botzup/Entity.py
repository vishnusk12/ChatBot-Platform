'''
Created on 05-Apr-2018

@author: Vishnu
'''

from .views import nlp
from nltk.corpus import names
import re
from .mappings import Date


def PERSON(text):
    text = text.title()
    split_text = text.split()
    doc = nlp(text)
    person = [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    list_person = []
    if len(person) > 1:
        dict_person = {}
        dict_person['person'] = [i.lower() for i in person]
        list_person.append(dict_person)
        return list_person
    elif len(person) == 1:
        dict_person = {}
        dict_person['person'] = [i.lower() for i in person]
        list_person.append(dict_person)
        return list_person
    elif len(person) == 0:
        labeled_names = ([(name, 'male') for name in names.words('male.txt')] + [(name, 'female') for name in names.words('female.txt')])
        for i in labeled_names:
            for j in split_text:
                if i[0] == j:
                    dict_person = {}
                    dict_person['person'] =  [i[0].lower()]
                    list_person.append(dict_person)
        return list_person
    else:
        return list_person
    
def GPE(text):
    doc = nlp(text.title())
    gpe = [ent.text for ent in doc.ents if ent.label_ == 'GPE']
    list_gpe = []
    if len(gpe) > 1:
        dict_gpe = {}
        dict_gpe['gpe'] = [i.lower() for i in gpe]
        list_gpe.append(dict_gpe)
        return list_gpe
    elif len(gpe) == 1:
        dict_gpe = {}
        dict_gpe['gpe'] = [i.lower() for i in gpe]
        list_gpe.append(dict_gpe)
        return list_gpe
    else:
        return list_gpe
    
def NORP(text):
    doc = nlp(text.title())
    norp = [ent.text for ent in doc.ents if ent.label_ == 'NORP']
    list_norp = []
    if len(norp) > 1:
        dict_gpe = {}
        dict_gpe['norp'] = [i.lower() for i in norp]
        list_norp.append(dict_gpe)
        return list_norp
    elif len(norp) == 1:
        dict_norp = {}
        dict_norp['norp'] = [i.lower() for i in norp]
        list_norp.append(dict_norp)
        return list_norp
    else:
        return list_norp
    
def FACILITY(text):
    doc = nlp(text.title())
    facility = [ent.text for ent in doc.ents if ent.label_ == 'FAC']
    list_facility = []
    if len(facility) > 1:
        dict_facility = {}
        dict_facility['facility'] = [i.lower() for i in facility]
        list_facility.append(dict_facility)
        return list_facility
    elif len(facility) == 1:
        dict_facility = {}
        dict_facility['facility'] = [i.lower() for i in facility]
        list_facility.append(dict_facility)
        return list_facility
    else:
        return list_facility
    
def ORG(text):
    doc = nlp(text.title())
    org = [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    list_org = []
    if len(org) > 1:
        dict_org = {}
        dict_org['org'] = [i.lower() for i in org]
        list_org.append(dict_org)
        return list_org
    elif len(org) == 1:
        dict_org = {}
        dict_org['org'] = [i.lower() for i in org]
        list_org.append(dict_org)
        return list_org
    else:
        return list_org
    
def LOC(text):
    doc = nlp(text.title())
    loc = [ent.text for ent in doc.ents if ent.label_ == 'LOC']
    list_loc = []
    if len(loc) > 1:
        dict_loc = {}
        dict_loc['loc'] = [i.lower() for i in loc]
        list_loc.append(dict_loc)
        return list_loc
    elif len(loc) == 1:
        dict_loc = {}
        dict_loc['loc'] = [i.lower() for i in loc]
        list_loc.append(dict_loc)
        return list_loc
    else:
        return list_loc
    
def PRODUCT(text):
    doc = nlp(text.title())
    product = [ent.text for ent in doc.ents if ent.label_ == 'PRODUCT']
    list_product = []
    if len(product) > 1:
        dict_product = {}
        dict_product['product'] = [i.lower() for i in product]
        list_product.append(dict_product)
        return list_product
    elif len(product) == 1:
        dict_product = {}
        dict_product['product'] = [i.lower() for i in product]
        list_product.append(dict_product)
        return list_product
    else:
        return list_product
    
def EVENT(text):
    doc = nlp(text.title())
    event = [ent.text for ent in doc.ents if ent.label_ == 'EVENT']
    list_event = []
    if len(event) > 1:
        dict_event = {}
        dict_event['event'] = [i.lower() for i in event]
        list_event.append(dict_event)
        return list_event
    elif len(event) == 1:
        dict_event = {}
        dict_event['event'] = [i.lower() for i in event]
        list_event.append(dict_event)
        return list_event
    else:
        return list_event
    
def WORK_OF_ART(text):
    doc = nlp(text.title())
    woa = [ent.text for ent in doc.ents if ent.label_ == 'WORK_OF_ART']
    list_woa = []
    if len(woa) > 1:
        dict_woa = {}
        dict_woa['work of art'] = [i.lower() for i in woa]
        return list_woa
    elif len(woa) == 1:
        dict_woa = {}
        dict_woa['work of art'] = [i.lower() for i in woa]
        list_woa.append(dict_woa)
        return list_woa
    else:
        return list_woa
    
def LAW(text):
    doc = nlp(text.title())
    law = [ent.text for ent in doc.ents if ent.label_ == 'LAW']
    list_law = []
    if len(law) > 1:
        dict_law = {}
        dict_law['law'] = [i.lower() for i in law]
        list_law.append(dict_law)
        return list_law
    elif len(law) == 1:
        dict_law = {}
        dict_law['law'] = [i.lower() for i in law]
        list_law.append(dict_law)
        return list_law
    else:
        return list_law

def LANGUAGE(text):
    doc = nlp(text.title())
    language = [ent.text for ent in doc.ents if ent.label_ == 'LANGUAGE']
    list_language = []
    if len(language) > 1:
        dict_language = {}
        dict_language['language'] = [i.lower() for i in language]
        list_language.append(dict_language)
        return list_language
    elif len(language) == 1:
        dict_language = {}
        dict_language['language'] = [i.lower() for i in language]
        list_language.append(dict_language)
        return list_language
    else:
        return list_language
    
def PERCENT(text):
    doc = nlp(text.title())
    percent = [ent.text for ent in doc.ents if ent.label_ == 'PERCENT']
    list_percent = []
    if len(percent) > 1:
        dict_percent = {}
        dict_percent['percent'] = [i.lower() for i in percent]
        list_percent.append(dict_percent)
        return list_percent
    elif len(percent) == 1:
        dict_percent = {}
        dict_percent['percent'] = [i.lower() for i in percent]
        list_percent.append(dict_percent)
        return list_percent
    else:
        return list_percent
    
def MONEY(text):
    doc = nlp(text.title())
    money = [ent.text for ent in doc.ents if ent.label_ == 'MONEY']
    list_money = []
    if len(money) > 1:
        dict_money = {}
        dict_money['money'] = [i.lower() for i in money]
        list_money.append(dict_money)
        return list_money
    elif len(money) == 1:
        dict_money = {}
        dict_money['money'] = [i.lower() for i in money]
        list_money.append(dict_money)
        return list_money
    else:
        return list_money
    
def QUANTITY(text):
    doc = nlp(text.title())
    quantity = [ent.text for ent in doc.ents if ent.label_ == 'QUANTITY']
    list_quantity = []
    if len(quantity) > 1:
        dict_quantity = {}
        dict_quantity['quantity'] = [i.lower() for i in quantity]
        list_quantity.append(dict_quantity)
        return list_quantity
    elif len(quantity) == 1:
        dict_quantity = {}
        dict_quantity['quantity'] = [i.lower() for i in quantity]
        list_quantity.append(dict_quantity)
        return list_quantity
    else:
        return list_quantity
    
def ORDINAL(text):
    doc = nlp(text.title())
    ordinal = [ent.text for ent in doc.ents if ent.label_ == 'ORDINAL']
    list_ordinal = []
    if len(ordinal) > 1:
        dict_ordinal = {}
        dict_ordinal['ordinal'] = [i.lower() for i in ordinal]
        list_ordinal.append(dict_ordinal)
        return list_ordinal
    elif len(ordinal) == 1:
        dict_ordinal = {}
        dict_ordinal['ordinal'] = [i.lower() for i in ordinal]
        list_ordinal.append(dict_ordinal)
        return list_ordinal
    else:
        return list_ordinal
    
def CARDINAL(text):
    doc = nlp(text.title())
    cardinal = [ent.text for ent in doc.ents if ent.label_ == 'CARDINAL']
    list_cardinal = []
    if len(cardinal) > 1:
        dict_cardinal = {}
        dict_cardinal['cardinal'] = [i.lower() for i in cardinal]
        list_cardinal.append(dict_cardinal)
        return list_cardinal
    elif len(cardinal) == 1:
        dict_cardinal = {}
        dict_cardinal['cardinal'] = [i.lower() for i in cardinal]
        list_cardinal.append(dict_cardinal)
        return list_cardinal
    else:
        return list_cardinal

def FULLADDRESS(text):
    text = text.upper()
    regex = "[0-9]{1,3} .+, .+, [A-Z]{1,4} [0-9]{1,7}"
    address = re.findall(regex, text)
    list_address = []
    if len(address) > 1:
        dict_address = {}
        dict_address['full address'] = [i.lower() for i in address]
        list_address.append(dict_address)
        return list_address
    elif len(address) == 1:
        dict_address = {}
        dict_address['full address'] = [i.lower() for i in address]
        list_address.append(dict_address)
        return list_address
    else:
        return list_address
    
def STREETADDRESS(text):
    text = text.lower()
    regex = re.compile("\d{1,4} [\w\s]{1,20}(?:street|st|avenue|ave|road|rd|highway|hwy|square|sq|trail|trl|drive|dr|court|ct|park|parkway|pkwy|circle|cir|boulevard|blvd)\W?(?=\s|$)", re.IGNORECASE)
    address = re.findall(regex, text)
    list_address = []
    if len(address) > 1:
        dict_address = {}
        dict_address['street address'] = [i.lower() for i in address]
        list_address.append(dict_address)
        return list_address
    elif len(address) == 1:
        dict_address = {}
        dict_address['street address'] = [i.lower() for i in address]
        list_address.append(dict_address)
        return list_address
    else:
        return list_address

def PHONENUMBER(text):
    text = text.lower()
    regex = re.compile("((?:(?<![\d-])(?:\+?\d{1,3}[-.\s*]?)?(?:\(?\d{3}\)?[-.\s*]?)?\d{3}[-.\s*]?\d{4}(?![\d-]))|(?:(?<![\d-])(?:(?:\(\+?\d{2}\))|(?:\+?\d{2}))\s*\d{2}\s*\d{3}\s*\d{4}(?![\d-])))")
    phone = re.findall(regex, text)
    list_phone = []
    if len(phone) > 1:
        dict_phone = {}
        dict_phone['phone number'] = [i.lower() for i in phone]
        list_phone.append(dict_phone)
        return list_phone
    elif len(phone) == 1:
        dict_phone = {}
        dict_phone['phone number'] = [i.lower() for i in phone]
        list_phone.append(dict_phone)
        return list_phone
    else:
        return list_phone
    
def EMAIL(text):
    text = text.lower()
    regex = re.compile("([a-z0-9!#$%&'*+\/=?^_`{|.}~-]+@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)", re.IGNORECASE)
    email = re.findall(regex, text)
    list_email = []
    if len(email) > 1:
        dict_email = {}
        dict_email['email'] = [i.lower() for i in email]
        list_email.append(dict_email)
        return list_email
    elif len(email) == 1:
        dict_email = {}
        dict_email['email'] = [i.lower() for i in email]
        list_email.append(dict_email)
        return list_email
    else:
        return list_email
    
def LINKS(text):
    text = text.lower()
    regex = re.compile(u'(?i)((?:https?://|www\d{0,3}[.])?[a-z0-9.\-]+[.](?:(?:international)|(?:construction)|(?:contractors)|(?:enterprises)|(?:photography)|(?:immobilien)|(?:management)|(?:technology)|(?:directory)|(?:education)|(?:equipment)|(?:institute)|(?:marketing)|(?:solutions)|(?:builders)|(?:clothing)|(?:computer)|(?:democrat)|(?:diamonds)|(?:graphics)|(?:holdings)|(?:lighting)|(?:plumbing)|(?:training)|(?:ventures)|(?:academy)|(?:careers)|(?:company)|(?:domains)|(?:florist)|(?:gallery)|(?:guitars)|(?:holiday)|(?:kitchen)|(?:recipes)|(?:shiksha)|(?:singles)|(?:support)|(?:systems)|(?:agency)|(?:berlin)|(?:camera)|(?:center)|(?:coffee)|(?:estate)|(?:kaufen)|(?:luxury)|(?:monash)|(?:museum)|(?:photos)|(?:repair)|(?:social)|(?:tattoo)|(?:travel)|(?:viajes)|(?:voyage)|(?:build)|(?:cheap)|(?:codes)|(?:dance)|(?:email)|(?:glass)|(?:house)|(?:ninja)|(?:photo)|(?:shoes)|(?:solar)|(?:today)|(?:aero)|(?:arpa)|(?:asia)|(?:bike)|(?:buzz)|(?:camp)|(?:club)|(?:coop)|(?:farm)|(?:gift)|(?:guru)|(?:info)|(?:jobs)|(?:kiwi)|(?:land)|(?:limo)|(?:link)|(?:menu)|(?:mobi)|(?:moda)|(?:name)|(?:pics)|(?:pink)|(?:post)|(?:rich)|(?:ruhr)|(?:sexy)|(?:tips)|(?:wang)|(?:wien)|(?:zone)|(?:biz)|(?:cab)|(?:cat)|(?:ceo)|(?:com)|(?:edu)|(?:gov)|(?:int)|(?:mil)|(?:net)|(?:onl)|(?:org)|(?:pro)|(?:red)|(?:tel)|(?:uno)|(?:xxx)|(?:ac)|(?:ad)|(?:ae)|(?:af)|(?:ag)|(?:ai)|(?:al)|(?:am)|(?:an)|(?:ao)|(?:aq)|(?:ar)|(?:as)|(?:at)|(?:au)|(?:aw)|(?:ax)|(?:az)|(?:ba)|(?:bb)|(?:bd)|(?:be)|(?:bf)|(?:bg)|(?:bh)|(?:bi)|(?:bj)|(?:bm)|(?:bn)|(?:bo)|(?:br)|(?:bs)|(?:bt)|(?:bv)|(?:bw)|(?:by)|(?:bz)|(?:ca)|(?:cc)|(?:cd)|(?:cf)|(?:cg)|(?:ch)|(?:ci)|(?:ck)|(?:cl)|(?:cm)|(?:cn)|(?:co)|(?:cr)|(?:cu)|(?:cv)|(?:cw)|(?:cx)|(?:cy)|(?:cz)|(?:de)|(?:dj)|(?:dk)|(?:dm)|(?:do)|(?:dz)|(?:ec)|(?:ee)|(?:eg)|(?:er)|(?:es)|(?:et)|(?:eu)|(?:fi)|(?:fj)|(?:fk)|(?:fm)|(?:fo)|(?:fr)|(?:ga)|(?:gb)|(?:gd)|(?:ge)|(?:gf)|(?:gg)|(?:gh)|(?:gi)|(?:gl)|(?:gm)|(?:gn)|(?:gp)|(?:gq)|(?:gr)|(?:gs)|(?:gt)|(?:gu)|(?:gw)|(?:gy)|(?:hk)|(?:hm)|(?:hn)|(?:hr)|(?:ht)|(?:hu)|(?:id)|(?:ie)|(?:il)|(?:im)|(?:in)|(?:io)|(?:iq)|(?:ir)|(?:is)|(?:it)|(?:je)|(?:jm)|(?:jo)|(?:jp)|(?:ke)|(?:kg)|(?:kh)|(?:ki)|(?:km)|(?:kn)|(?:kp)|(?:kr)|(?:kw)|(?:ky)|(?:kz)|(?:la)|(?:lb)|(?:lc)|(?:li)|(?:lk)|(?:lr)|(?:ls)|(?:lt)|(?:lu)|(?:lv)|(?:ly)|(?:ma)|(?:mc)|(?:md)|(?:me)|(?:mg)|(?:mh)|(?:mk)|(?:ml)|(?:mm)|(?:mn)|(?:mo)|(?:mp)|(?:mq)|(?:mr)|(?:ms)|(?:mt)|(?:mu)|(?:mv)|(?:mw)|(?:mx)|(?:my)|(?:mz)|(?:na)|(?:nc)|(?:ne)|(?:nf)|(?:ng)|(?:ni)|(?:nl)|(?:no)|(?:np)|(?:nr)|(?:nu)|(?:nz)|(?:om)|(?:pa)|(?:pe)|(?:pf)|(?:pg)|(?:ph)|(?:pk)|(?:pl)|(?:pm)|(?:pn)|(?:pr)|(?:ps)|(?:pt)|(?:pw)|(?:py)|(?:qa)|(?:re)|(?:ro)|(?:rs)|(?:ru)|(?:rw)|(?:sa)|(?:sb)|(?:sc)|(?:sd)|(?:se)|(?:sg)|(?:sh)|(?:si)|(?:sj)|(?:sk)|(?:sl)|(?:sm)|(?:sn)|(?:so)|(?:sr)|(?:st)|(?:su)|(?:sv)|(?:sx)|(?:sy)|(?:sz)|(?:tc)|(?:td)|(?:tf)|(?:tg)|(?:th)|(?:tj)|(?:tk)|(?:tl)|(?:tm)|(?:tn)|(?:to)|(?:tp)|(?:tr)|(?:tt)|(?:tv)|(?:tw)|(?:tz)|(?:ua)|(?:ug)|(?:uk)|(?:us)|(?:uy)|(?:uz)|(?:va)|(?:vc)|(?:ve)|(?:vg)|(?:vi)|(?:vn)|(?:vu)|(?:wf)|(?:ws)|(?:ye)|(?:yt)|(?:za)|(?:zm)|(?:zw))(?:/[^\s()<>]+[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019])?)', re.IGNORECASE)
    link = re.findall(regex, text)
    list_link = []
    if len(link) > 1:
        dict_link = {}
        dict_link['url'] = [i.lower() for i in link]
        list_link.append(dict_link)
        return list_link
    elif len(link) == 1:
        dict_link = {}
        dict_link['url'] = [i.lower() for i in link]
        list_link.append(dict_link)
        return list_link
    else:
        return list_link
    
def DATE(text):
    text = text.lower()
    regex = re.compile(u'(?:(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?\s+(?:of\s+)?(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)|(?:jan\.?|january|feb\.?|february|mar\.?|march|apr\.?|april|may|jun\.?|june|jul\.?|july|aug\.?|august|sep\.?|september|oct\.?|october|nov\.?|november|dec\.?|december)\s+(?<!\:)(?<!\:\d)[0-3]?\d(?:st|nd|rd|th)?)(?:\,)?\s*(?:\d{4})?|[0-3]?\d[-\./][0-3]?\d[-\./]\d{2,4}', re.IGNORECASE)
    date = re.findall(regex, text)
    list_date = []
    if len(date) > 1:
        dict_date = {}
        dict_date['date'] = [i.lower() for i in date]
        list_date.append(dict_date)
        return list_date
    elif len(date) == 1:
        dict_date = {}
        dict_date['date'] = [i.lower() for i in date]
        list_date.append(dict_date)
        return list_date
    elif len(date) == 0:
        for key, value in Date.items():
            for i in value:
                match = re.compile(r"\b%s\b"%(i))
                date = match.findall(text)
                if len(date) != 0:
                    dict_date = {}
                    dict_date['date'] = [key.lower()]
                    list_date.append(dict_date)
        return list_date
    else:
        return list_date
    
def TIME(text):
    text = text.lower()
    regex = re.compile('\d{1,2}:\d{2} ?(?:[ap]\.?m\.?)?|\d[ap]\.?m\.?', re.IGNORECASE)
    time = re.findall(regex, text)
    list_time = []
    if len(time) > 1:
        dict_time = {}
        dict_time['time'] = [i.lower() for i in time]
        list_time.append(dict_time)
        return list_time
    elif len(time) == 1:
        dict_time = {}
        dict_time['time'] = [i.lower() for i in time]
        list_time.append(dict_time)
        return list_time
    else:
        return list_time
    
def ZIP(text):
    text = text.lower()
    regex = re.compile(r'\b\d{5,6}(?:[-\s]\d{4})?\b')
    zipcode = re.findall(regex, text)
    list_zipcode = []
    if len(zipcode) > 1:
        dict_zipcode = {}
        dict_zipcode['zip'] = [i.lower() for i in zipcode]
        list_zipcode.append(dict_zipcode)
        return list_zipcode
    elif len(zipcode) == 1:
        dict_zipcode = {}
        dict_zipcode['zip'] = [i.lower() for i in zipcode]
        list_zipcode.append(dict_zipcode)
        return list_zipcode
    else:
        return list_zipcode
    
def BITCOINADDRESS(text):
    text = text.lower()
    regex = re.compile('(?<![a-km-zA-HJ-NP-Z0-9])[13][a-km-zA-HJ-NP-Z0-9]{26,33}(?![a-km-zA-HJ-NP-Z0-9])')
    addr = re.findall(regex, text)
    list_addr = []
    if len(addr) > 1:
        dict_addr = {}
        dict_addr['bitcoin address'] = [i.lower() for i in addr]
        list_addr.append(dict_addr)
        return list_addr
    elif len(addr) == 1:
        dict_addr = {}
        dict_addr['bitcoin address'] = [i.lower() for i in addr]
        list_addr.append(dict_addr)
        return list_addr
    else:
        return list_addr
    
def CREDITCARD(text):
    text = text.lower()
    regex = re.compile('((?:(?:\\d{4}[- ]?){3}\\d{4}|\\d{15,16}))(?![\\d])')
    details = re.findall(regex, text)
    list_details = []
    if len(details) > 1:
        dict_details = {}
        dict_details['credit card details'] = [i.lower() for i in details]
        list_details.append(dict_details)
        return list_details
    elif len(details) == 1:
        dict_details = {}
        dict_details['credit card details'] = [i.lower() for i in details]
        list_details.append(dict_details)
        return list_details
    else:
        return list_details
    
def IP(text):
    text = text.lower()
    regex = re.compile(u'(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', re.IGNORECASE)
    ip = re.findall(regex, text)
    list_ip = []
    if len(ip) > 1:
        dict_ip = {}
        dict_ip['ip'] = [i.lower() for i in ip]
        list_ip.append(dict_ip)
        return list_ip
    elif len(ip) == 1:
        dict_ip = {}
        dict_ip['ip'] = [i.lower() for i in ip]
        list_ip.append(dict_ip)
        return list_ip
    else:
        return list_ip
    
def IPV6(text):
    text = text.lower()
    regex = re.compile(u'\s*(?!.*::.*::)(?:(?!:)|:(?=:))(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)){6}(?:[0-9a-f]{0,4}(?:(?<=::)|(?<!::):)[0-9a-f]{0,4}(?:(?<=::)|(?<!:)|(?<=:)(?<!::):)|(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)(?:\.(?:25[0-4]|2[0-4]\d|1\d\d|[1-9]?\d)){3})\s*', re.VERBOSE|re.IGNORECASE|re.DOTALL)
    ip = re.findall(regex, text)
    list_ip = []
    if len(ip) > 1:
        dict_ip = {}
        dict_ip['ipv6'] = [i.lower() for i in ip]
        list_ip.append(dict_ip)
        return list_ip
    elif len(ip) == 1:
        dict_ip = {}
        dict_ip['ipv6'] = [i.lower() for i in ip]
        list_ip.append(dict_ip)
        return list_ip
    else:
        return list_ip
    
def entities(text):
    response = {}
    response['property'] = []
    try:
        response['property'].extend(PERSON(text))
        response['property'].extend(GPE(text))
        response['property'].extend(NORP(text))
        response['property'].extend(FACILITY(text))
        response['property'].extend(ORG(text))
        response['property'].extend(LOC(text))
        response['property'].extend(PRODUCT(text))
        response['property'].extend(EVENT(text))
        response['property'].extend(WORK_OF_ART(text))
        response['property'].extend(LAW(text))
        response['property'].extend(LANGUAGE(text))
        response['property'].extend(PERCENT(text))
        response['property'].extend(MONEY(text))
        response['property'].extend(QUANTITY(text))
        response['property'].extend(ORDINAL(text))
        response['property'].extend(CARDINAL(text))
        response['property'].extend(FULLADDRESS(text))
        response['property'].extend(STREETADDRESS(text))
        response['property'].extend(PHONENUMBER(text))
        response['property'].extend(EMAIL(text))
        response['property'].extend(LINKS(text))
        response['property'].extend(DATE(text))
        response['property'].extend(TIME(text))
        response['property'].extend(ZIP(text))
        response['property'].extend(BITCOINADDRESS(text))
        response['property'].extend(CREDITCARD(text))
        response['property'].extend(IP(text))
        response['property'].extend(IPV6(text))
        return response
    except:
        return response
