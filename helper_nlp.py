





def process_text( data, column_name, treatment_type='lemmatization', remove_int=False, fill_na=False, drop_na=False,fill_na_with=''):
    
    """
    Function that perfroms basic cleaning on text along with 
    stemming/lemmitization(acc. to choice), stopwords removal.
    
    """
    
    import re
    import nltk
    import warnings
    warnings.filterwarnings('ignore')
    nltk.download('stopwords')
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.stem import WordNetLemmatizer 
    from nltk.corpus import wordnet

    ps = PorterStemmer()
    lemmatizer=WordNetLemmatizer()
    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')
    all_stopwords.remove('no')
    all_stopwords.append('the')
    
    
    def get_wordnet_pos(word):
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)
    
    stemmed_reviewlst=[]
    lemmatized_reviewlst=[]
    stemmed_lemmaed_reviewlst=[]
    
    print(f"{data[column_name].isna().sum()} NaN values detected.")
    
    if fill_na==True and drop_na==False:
        data[column_name].fillna(str(fill_na_with),inplace=True)
        print(f"Replacing NaN with {fill_na_with} Change will be reflected on original dataset too!")
    elif fill_na==False and drop_na==True:
        data[column_name].dropna(inplace=True)
        print("Ateempting to drop NaN values from selected column! Change will be reflected on dataset too!")
    elif fill_na==True and drop_na==True:
        print("Invalid operation choice. Skipping missing value treatment!")
    else:
        print("Skipping missing values treatment!")
        
    
    if treatment_type=='lemmatization':
        
        for i in range(len(data)):
            review=str(data[column_name][i])
            if remove_int==True:
                review=re.sub(r'[^a-zA-Z  ]','',review)
            else:
                review=re.sub(r'[^a-zA-Z0-9  ]','',review)
                
            review=review.split()
            review = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in review if not w in set(all_stopwords)]
            review = ' '.join(review)
            lemmatized_reviewlst.append(review)
            
        returns=lemmatized_reviewlst
        
    elif treatment_type=='stemming':
        
        for i in range(len(data)):
            review=str(data[column_name][i])
            if remove_int==True:
                review=re.sub(r'[^a-zA-Z  ]','',review)
            else:
                review=re.sub(r'[^a-zA-Z0-9  ]','',review)
                
            
            review=review.split()
            review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
            review = ' '.join(review)
            stemmed_reviewlst.append(review)
            
        returns=stemmed_reviewlst
        
    elif treatment_type=='both':
        
        for i in range(len(data)):
            review=str(data[column_name][i])
            if remove_int==True:
                review=re.sub(r'[^a-zA-Z  ]','',review)
            else:
                review=re.sub(r'[^a-zA-Z0-9  ]','',review)
                
            
            review=review.split(' ')
            review = [lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in review if not w in set(all_stopwords)]
            review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
            
            review = ' '.join(review)
            review=re.sub('  ',' ',review)
            stemmed_lemmaed_reviewlst.append(review)
            
        returns=stemmed_lemmaed_reviewlst
        
    else:
        returns='Can only apply "lemmatization" / "stemming"/ "both"'
            
        
    return returns
        


