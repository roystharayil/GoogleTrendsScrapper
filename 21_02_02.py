import 21_02_01

with open('keywords.csv', 'r') as f:
    keywords = f.readlines()

    for keyword in keywords:
        trends(keyword)

