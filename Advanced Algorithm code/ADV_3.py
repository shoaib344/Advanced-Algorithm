import newspaper
from newspaper import Article
import concurrent.futures
import timeit


def get_headlines(url): # Function to get headlines from a single URL
    headlines = []
    paper = newspaper.build(url, memoize_articles=False) # build an article object with the url passed as argument
    for article in paper.articles[:5]: #  getting first five articles of each news source
        article.download()
        article.parse()
        headlines.append(article.title)
    return url, headlines


def get_headlines_concurrent(): # Concurrent version of the get_headlines function
    URLs = [
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',
    ]
    
    with concurrent.futures.ThreadPoolExecutor() as executor: # Sets up a ThreadPoolExecutor as the thread management context manager
        futures = [executor.submit(get_headlines, url) for url in URLs]  # call get_headlines, which iterates through the list of urls, with the parameter url
        for future in concurrent.futures.as_completed(futures): # 
            url, headlines = future.result() #  Wait until all threads finish and then retrieve results
            print(f'\nThe headlines from {url} are\n')
            for headline in headlines: #   Printing out each headline on its own line
                print(headline)


def get_headlines_non_concurrent(): # Non-concurrent version of the get_headlines function
    URLs = [
        'http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://www.derspiegel.de/',
        'http://www.bbc.co.uk/',
        'https://theguardian.com',
    ]
    
    for url in URLs: #  For each URL in the list
        paper = newspaper.build(url, memoize_articles=False) 
        print(f'\nThe headlines from {url} are\n')
        for article in paper.articles[:5]:
            article.download()
            article.parse()
            print(article.title)
if __name__ == '__main__':
    import timeit
    elapsed_time_non_concurrent = timeit.timeit("get_headlines_non_concurrent()", setup="from __main__ import get_headlines_non_concurrent", number=2)/2 # Timing the non-concurrent version
    elapsed_time_concurrent = timeit.timeit("get_headlines_concurrent()", setup="from __main__ import get_headlines_concurrent", number=2)/2 # Timing the concurrent version
 
    print(f"\nNon-concurrent version elapsed time: {elapsed_time_non_concurrent:.2f} seconds") 
    print(f"Concurrent version elapsed time: {elapsed_time_concurrent:.2f} seconds")
    print(f"Speedup: {elapsed_time_non_concurrent / elapsed_time_concurrent:.2f}x")
if elapsed_time_concurrent < elapsed_time_non_concurrent: # Comparing the timing of both versions
    print('Concurrent version is faster!')
else:
    print('Concurrent version is not faster.')

