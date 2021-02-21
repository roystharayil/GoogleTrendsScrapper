import trends

with open('keywords.csv', 'r') as f:
    keywords = f.readlines()

    for keyword in keywords:
        trends.trends(keyword)