#!/usr/bin/env python
# coding: utf-8

BEGIN = '__BEGIN__'
END = '__END__'


#============================================================================
# STEP 1
#============================================================================
def step1():

    print("STEP1: Start")

    import requests
    import re
    from bs4 import BeautifulSoup

    def get_tweet_info(twilog_month_url):
        """月単位のツィート一覧からツィート部分のみを抽出してリストで返す"""
        
        res = requests.get(twilog_month_url)
        html_doc = res.text
        soup = BeautifulSoup(html_doc,  'html.parser')
        
        #ツィートのブロックで絞り込む
        tltweets_all = soup.find_all('section', class_ = 'tl-tweets')

        month_tweets = []

        #除外パターン(@で始まる)
        pattern = r"^@.*$"
        repattern = re.compile(pattern)
        
        for tltweets in tltweets_all:
            #ツィート内容
            tltext_all = tltweets.find_all('p', class_='tl-text')
            for tag in tltext_all:
                # 除外パターンにマッチしなければ追加する
                tweet = tag.get_text().strip()
                if not repattern.match(tweet):
                    month_tweets.append(tweet)

        return month_tweets



    ################################
    # ツィートアーカイブ一覧から全てのツィートを取得
    ################################
    res = requests.get('https://twilog.org/yuna8313/archives/nort')
    html_doc = res.text
    soup = BeautifulSoup(html_doc,  'html.parser')

    #年ブロックの一覧取得
    year_box_list = soup.find_all('section', class_ = 'main-list-box1')


    tweet_all = []

    #年ブロックでループ
    for year_box in year_box_list:
        
        #--------------------------------------------
        #月毎ツィート一覧のURLリストを取得
        #--------------------------------------------
        month_urls = []
        a_tags = year_box.find_all('a')

        #nortのURLのみ抽出
        for a_tag in a_tags:
            if 'nort' in a_tag['href']:
                month_urls.append(a_tag['href'])

        #-------------------------------------
        # 月毎ツィート一覧からスクレイピング
        #-------------------------------------
        import time
        #月毎URLでループ
        for month_url in month_urls:
            print('スクレイピング中: ', month_url)
            tweet_all.append(get_tweet_info(month_url))
            time.sleep(0.5)
            
    print('完了')


    ################################
    # 取得したツィートをファイルに書き込む
    ################################
    with open('yuna8313_tweets.txt', 'w', encoding='utf-8') as f:
        for tweet in tweet_all:
            f.write('\n'.join(tweet))


    print("STEP1: End")

#============================================================================
# STEP 2
#============================================================================
def step2():
    print("STEP2: Start")

    #########################################
    # ツィートファイルを読み込んで前処理実施
    #########################################
    import re

    with open('yuna8313_tweets.txt', 'r', encoding='utf-8') as fr:
        rlines =  fr.readlines()

    sentences = []
    for rline in rlines:
        rline = re.sub('http.+…', '', rline)
        rline = re.sub('http[a-zA-Z0-9:/¥.]+', '', rline)
        rline = rline.replace('\r', '').replace('\n', '')
        rline = rline.replace(' ', '')
        rline = rline.replace('→', '')
        rline = rline.replace('>RT', '')
        rline = rline.replace('(続き）', '').replace('続き）', '').replace('（続く)', '').replace('（続く', '')
        rline = re.sub('[、「」？]', '', rline)
        lines = rline.split('。')
        for sentence in lines:
            if not sentence == '':
                sentences.append(sentence)

    # for sentence in sentences:
    #     print(sentence)




    from janome.tokenizer import Tokenizer
    from itertools import chain


    def get_three_words_list(sentence):
        """文章を3単語の組にして返す"""
        t = Tokenizer()
        words = t.tokenize(sentence, wakati=True)
        #words = [BEGIN] + words + [END]
        words = list(chain([BEGIN],words,[END]))
            
        three_words_list = []
        for i in range(len(words) - 2):
            three_words_list.append(tuple(words[i:i+3]))
        return three_words_list




    # #########################################
    # # 3ワードリストを作成しカウントする
    # #########################################
    from tqdm import tqdm
    from collections import Counter

    three_words_list = []
    for sentence in tqdm(sentences):
        three_words_list += get_three_words_list(sentence)

    three_words_count = Counter(three_words_list)
    #len(three_words_count)


    #　3ワードリストカウントをダンプ
    import pickle

    with open('yuna8313_threewords.pickle', 'wb') as f:
        pickle.dump(three_words_count, f)


    print("STEP2: End")


#============================================================================
# STEP 3
#============================================================================
def step3():
    print("STEP3: Start")

    #　3ワードリストカウントのダンプを復元
    import pickle

    with open('yuna8313_threewords.pickle', 'rb') as f:
        three_words_count = pickle.load(f)



    def generate_markov_dict(three_words_count):
        """マルコフ連鎖での文章生成用の辞書データを生成する"""
        markov_dict = {}
        for three_words, count in three_words_count.items():
            two_words = three_words[:2]
            next_word = three_words[2]
            if two_words not in markov_dict:
                markov_dict[two_words] = {'words': [], 'weights': []}
            markov_dict[two_words]['words'].append(next_word)
            markov_dict[two_words]['weights'].append(count)
        return markov_dict

    #markov_dict = generate_markov_dict(three_words_count)
    #markov_dict


    #########################################
    # 3ワードカウントリストからマルコフ連鎖辞書を作成
    #########################################
    markov_dict = generate_markov_dict(three_words_count)

    #print("markov_dict = " + str(len(markov_dict)))


    from collections import defaultdict

    def get_first_word_and_count(three_words_count):
        """最初の単語を選択するための辞書データを作成する"""
        first_word_count = defaultdict(int)
        
        for three_words, count in three_words_count.items():
            if three_words[0] == BEGIN:
                next_word = three_words[1]
                first_word_count[next_word] += count
                
        return first_word_count




    def get_first_words_weights(three_words_count):
        """最初の単語と重みのリストを作成する"""
        first_word_count = get_first_word_and_count(three_words_count)
        words = []
        weights = []
        for word, count in first_word_count.items():
            words.append(word)
            weights.append(count)
            
        return words, weights

    #first_words, first_weights = get_first_words_weights(three_words_count)
    #first_words, first_weights



    #########################################
    # ツィートの出だしを重み付けして取得
    #########################################
    first_words, first_weights = get_first_words_weights(three_words_count)
    print("first_words = " + str(len(first_words)))



    import random

    def generate_text(first_words, first_weights, markov_dict):
        """入力された辞書データを元に文章を生成する"""
        first_word = random.choices(first_words, weights=first_weights)[0]
        generate_words = [BEGIN, first_word]
        while True:
            pair = tuple(generate_words[-2:])
            words = markov_dict[pair]['words']
            weights = markov_dict[pair]['weights']
            next_word = random.choices(words, weights=weights)[0]
            if next_word == END:
                break
            generate_words.append(next_word)
            
        return ''.join(generate_words[1:])


    #########################################
    # ツィートを生成
    #########################################
    for _ in range(20):
        sentence = generate_text(first_words, first_weights, markov_dict)
        print(sentence + '。')


    print("STEP3: End")

#============================================================================
# MAIN
#============================================================================
step1()
step2()
step3()

