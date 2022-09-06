# Save time by not writing repetitive code across NLP projects! 
Python library that takes a dataset, column name, text-cleaning choice, text pre-processing preference (stem/lemma/both) as input and returns a list of text from the mentioned column after performing basic cleaning/pre-processing/stopwords-removal.
<br>
<h5> Run: </h5>
! git clone https://github.com/ayanatherate/quicktextpre.git <br>
<h4 style='font-family:monospace;'>Example code: <br><br>import pandas as pd <br><br> data = pd.read_csv( r'../reviews.csv' )<br><br>processed_text_from_column= process_text(data ,'Reviews', treatment_type='lemmatization', remove_int=True, drop_na=True)</h4>

<br>
<h2> Does: </h2>
1) Basic Data Cleaning using RegEX<br>
2) Missing Values Treatment <br>
3) Lemmatization/Stemming/both, based on choice<br>
4) Stop-words removal<br>
<br>

<h2>Requirements: </h2>
re<br>
nltk<br>
warnings<br>

<h2>Arguments:</h2>
dataset (dataset should already be accessed with pandas)<br><br>
Column  (Column name on which the pre-processing function would be performed)<br><br>
treatment_type='lemmatization'/'stemming'/'both' (Choice of either lemmatization/stemming or both of the text in the column)  [default: 'lemmatization']<br><br>
remove_int=True/False (Cleans integers present in the text if True, else ignores)  [default: False]<br><br>
drop_na=True/False (Drops rows with missing values if True, else ignores)  [default: False]<br><br>
fill_na=True/False (Replaces missing value with specified value in fill_na_with, if missing value is present)  [default: False]<br><br>
fill_na_with='***character/string/int to replace missing value with, works only if fill_na=True***'  [default: ' ']

<h2>Returns:</h2>
a list containing pre-processed and cleaned text from the column<br><br>

