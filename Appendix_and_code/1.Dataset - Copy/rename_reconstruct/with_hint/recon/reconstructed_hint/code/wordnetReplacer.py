import nltk
# nltk.download('wordnet')
# nltk.download('punkt')
from nltk.corpus import wordnet
from nltk import word_tokenize
from nltk.corpus import words
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
# from pattern.en import pluralize
from pattern.text.en import pluralize
# nltk.download('popular')
import random
import inflection
from camel_converter import to_camel
from inflection import camelize
import requests
import urllib3
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL:@SECLEVEL=2'
proxies={
    "https":"127.0.0.1:8234"
}
import json
import pandas as pd

def replace_word_with_conceptnet5(word):
    word=word.lower()
    related_dict=requests.get("http://api.conceptnet.io/related/c/en/"+word,proxies=proxies).json()
    # print(related_dict.keys())
    en_related={}
    for d in list(related_dict['related']):
        if '/c/en' in d['@id']:
            if d['weight']<1.0:
                # print(d['@id'])
                en_related[d['@id'].split('/')[-1]]=d['weight']
    # print(list(en_related.keys()))
    return list(en_related.keys())

def syn_dict():
    df=pd.read_csv('synonyms_dict.csv')
    syn_dict1={}
    syn_dict2={}
    for index in df.index:
        item=df.loc[index]
        key=str(item[0]).lower()
        value=str(item[1]).lower()
        syn_dict1[key]=value
        syn_dict2[value]=key
    return syn_dict1,syn_dict2
# replace_word_with_conceptnet5('rs')
# syn_dict()
def replace_word(word):
    synonyms = []
    synonyms1=[]
    # print("-------new_word-------"+word)
    dict_syn=[]
    if len(word)>3 and len(wordnet.synsets(word)) != 0:
        for syn in wordnet.synsets(word):
            # print("*********************")
            # print(syn.lemmas())
            # print("*********************")
            for l in syn.lemmas():
                # print("*********************")
                # print(syn)
                # print(l.name())
                # print("*********************")
                if l.name()!=word:
                    synonyms.append(l.name())

    # if word in list(dict1.keys()):
    #     dict_syn.append(dict1[word])
    # if word in list(dict2.keys()):
    #     dict_syn.append(dict2[word])
    # dict_syn=list(set(dict_syn))
    synonyms1=[]
    # if dict_syn!=[]:
    #     word=dict_syn[0]
    if synonyms!=[]:
        synonyms=sorted(synonyms, key=len)
        shortest=synonyms[0]
        word=shortest
    elif synonyms==[]:
        synonyms1=replace_word_with_conceptnet5(word)
        if synonyms1!=[]:
            word=synonyms1[0]
    return word
    # if len(synonyms) > 0:
    #     synonyms=sorted(synonyms, key=len)
    #     shortest=synonyms[0]
    #     return shortest
    # elif len(synonyms) == 0 and len(synonyms1) > 0:
    #     return synonyms1[0]
    # elif len(synonyms) == 0 and len(synonyms1) ==0  and len(dict_syn)==0:
    #     return word
    # elif len(synonyms) > 0 and len(synonyms1) > 0 and len(dict_syn) > 0:
        # return set(dict_syn)[0]



def join_new_word(t_words,case):
    new_word=None
    # print('------')
    # print(t_words)
    t_words = [i for i in t_words if i is not None]
    if len(t_words)==1 and case=='normal':
        new_word=t_words[0]
    elif len(t_words)>1 and case=='camel':
        new_word='_'.join(t_words)
        new_word = to_camel(new_word)
    elif len(t_words)>1 and case=='snake':
        new_word='_'.join(t_words)
    return new_word

def isplural(word):
    Lem = WordNetLemmatizer()
    lemma = Lem.lemmatize(word, 'n')
    plural = True if word is not lemma else False
    return plural, lemma


def replacer(word):
    words=[]
    case=''
    # porter = PorterStemmer()
    # word= porter.stem("stolen")
    # print('------'+word)
    # Lem = WordNetLemmatizer()
    # word = Lem.lemmatize("what")
    # print('----original----'+word)
    plural, singular=isplural(word)
    if len(word)>2 and plural==True:
        word=singular
    else:
        word=word
    print('----camel----')
    print(word)
    print(camelize(word))
    print(camelize(word, False))
    if camelize(word) == word or camelize(word, False) != word:
        case='camel'
        word=inflection.underscore(word)
        # word=word.replace('_','&')
        words=word.split('_')
        # print(words)
    if '_' in word:
        words=word.split('_')
        case='snake'
    else:
        words.append(word)
        case='normal'

    transformed_words=[]
    # print("original word")
    # print(words)
    for w in words:
        if 'error' in w.lower():
            transformed_words.append(w)
        elif len(w)<=2 and len(w)>0:
            # print('---short word---'+w+"---")
            transformed_words.append(w[0])
        else:
            transformed_words.append(replace_word(w))

    transformed_words = [i for i in transformed_words if i is not None]
    if len(transformed_words)!=0:
        transformed_word=join_new_word(transformed_words,case)
    else:
        transformed_word=word
    if len(word)>2 and plural==True:
        transformed_word=pluralize(transformed_word)
    # print("wordword and transformed_word")
    print(word)
    print(transformed_word)
    return  transformed_word

# replacer("sites")
# replacer("goodFood")
# replacer("good_food")
# replacer("sa_sites")
# replacer("saSites")


def replacer_final(word):
    print("------New------")
    print(word)
    case=''
    words=[]
    camelized_word=camelize(word)
    f_camelize_word=camelized_word[0].lower()+camelized_word[1:]
    if f_camelize_word==word or camelized_word==word:
        case='camel'
        ww=inflection.underscore(word)
        words=ww.split('_')
    elif '_' in word:
        words=word.split('_')
        case='snake'
    else:
        case='normal'
        words.append(word)
    print("------words------")
    print(words)
    dict1,dict2=syn_dict()
    transformed_words=[]
    unchanged=''
    for w in words:
        print(w)
        if 'error' in word.lower() or 'exception' in word.lower() or 'logging' in word.lower() or 'log' in word.lower() or 'logger' in word.lower():
            # print("------unchanged------")
            unchanged=word
        elif len(w)<=3 and len(w)>0:
            # print("------short word------")
            new_word=w
            transformed_words.append(new_word)
        elif w in list(dict1.keys()) or w in list(dict2.keys()):
            # print("------dict word------")
            if w in list(dict1.keys()):
                if dict1[w] != w:
                    transformed_words.append(dict1[w])
                    print(dict1[w])
            elif w in list(dict2.keys()):
                if dict2[w] !=w:
                    transformed_words.append(dict2[w])
                    # print(dict2[w])
        else:
            # print("------replacer word------")
            plural, singular=isplural(w)
            if len(w)>3 and plural==True:
                w=singular
                new_word=replace_word(w)
                re_pluralize=pluralize(new_word)
                transformed_words.append(re_pluralize)
            elif len(w)!=0 and plural==False:
                new_word=replace_word(w)
                transformed_words.append(new_word)


    transformed_words = [i for i in transformed_words if i is not None and i !=word]
    # print("------transformed_words------")
    # print(transformed_words)
    if len(transformed_words)>=2:
        final_new_word=join_new_word(transformed_words,case)
    elif len(transformed_words)==1:
        final_new_word=transformed_words[0]
    else:
        final_new_word=unchanged

    if final_new_word=='' or final_new_word==None:
        final_new_word=word
    # print("------final_new_word------")
    # print(final_new_word)
    return final_new_word

# replacer_final("aaa_Have")
# replacer_final("abABC")
# replacer_final("sites")
# replacer_final("goodFood")
# replacer_final("good_food")
# replacer_final("sa_sites")
# replacer_final("saSites")
# replacer_final("error")
# replacer_final("errorABC")
# replacer_final("abException")
