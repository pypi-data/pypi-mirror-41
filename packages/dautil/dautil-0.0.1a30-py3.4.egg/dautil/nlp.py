''' Natural language processing utilities '''
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import pandas as pd
from dautil import data
from dautil import log_api
import os
import datetime


def calc_tfidf(corpus):
    ''' Calculates TF-IDF for a list of text strings and sums it up by term.

    :param corpus: A list of text strings.

    :returns: A pandas `DataFrame` with columns 'term' and 'tfidf'.
    '''
    vectorizer = TfidfVectorizer(ngram_range=(2, 3), stop_words='english')
    matrix = vectorizer.fit_transform(corpus)
    sums = np.array(matrix.sum(axis=0)).ravel()

    ranks = [(word, val) for word, val in
             zip(vectorizer.get_feature_names(), sums)]

    df = pd.DataFrame(ranks, columns=["term", "tfidf"])
    df = df.sort(['tfidf'])

    return df


def select_terms(df, method='q3', select_func=None):
    ''' Select terms based on TF-IDF.

    :param df: A pandas `DataFrame` as produced by `calc_tfidf` function.
    :param method: The selection method, \
        default use the third quartile as cutoff.
    :param  select_func: An optional selection function.

    :returns: A set containing the selected terms.
    '''
    cutoff = 1000

    if method == 'q3':
        cutoff = np.percentile(df['tfidf'], 75)
    else:
        select_func(df)

    cut_df = df[df['tfidf'] > cutoff]

    return set(cut_df['term'])


class WebCorpus():
    ''' A corpus for text downloaded from the Web. '''
    def __init__(self, dir):
        self.dir = os.path.join(data.get_data_dir(), dir)
        self.LOG = log_api.conf_logger(__name__)

        if not os.path.exists(self.dir):
            os.mkdir(self.dir)

        self.csv_fname = os.path.join(self.dir, 'metadata.csv')
        self.url_set = set()
        self.init_url_csv()

    def init_url_csv(self):
        ''' Initialize a CSV containing URLs of downloaded texts. '''

        if os.path.exists(self.csv_fname):
            df = pd.read_csv(self.csv_fname)
            self.url_set = set(df['URL'].values.tolist())
        else:
            with open(self.csv_fname, 'w') as urls_csv:
                urls_csv.write('Added,URL,Title,Author\n')

    def store_text(self, name, txt, url, title, author):
        ''' Stores text in the corpus directory. \
            Also updates a CSV file to avoid downloading the \
            same file again.

        :param name: The name of the file.
        :param txt: The text of the file.
        :param url: The URL of the original document.
        :param title: The title of the original document.
        :param author: The author of the original document.
        '''
        fname = os.path.join(self.dir, name.replace('/', ''))

        with open(fname, 'w') as txt_file:
            txt_file.write(txt)

        clean_title = title.replace(',', ' ')
        clean_title = clean_title.replace('/', '')

        with open(self.csv_fname, 'a') as urls_csv:
            timestamp = datetime.datetime.now().isoformat()
            urls_csv.write('{0},{1},{2},{3}\n'.format(
                timestamp, url, clean_title,
                author.replace(',', ' ')))

        self.url_set.add(url)

    def get_texts(self):
        ''' Gets all the texts of the corpus.

        :returns: The texts as a list.
        '''
        texts = []

        for f in os.listdir(self.dir):
            if not f.endswith('csv'):
                try:
                    with open(os.path.join(self.dir, f), 'r') as txt_file:
                        txt = "".join(txt_file.readlines())
                        texts.append(txt)
                except Exception as e:
                    self.LOG.warning('{0} {1}'.format(f, e))

        return texts

    def get_text(self, name):
        ''' Gets the text for a file in the corpus.
        :param name: The name of the file.
        :param url: The URL of the original document.

        :returns: The text of the file.
        '''
        txt = ''
        fname = os.path.join(self.dir, name)

        with open(fname, 'r') as txt_file:
            txt = "".join(txt_file.readlines())

        return txt

    def get_titles(self):
        df = pd.read_csv(self.csv_fname)
        return set(df['Title'].values.tolist())

    def get_authors(self):
        df = pd.read_csv(self.csv_fname)
        return set(df['Author'].values.tolist())
