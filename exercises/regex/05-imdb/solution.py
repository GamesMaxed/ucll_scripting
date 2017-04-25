import re


def find_episode_titles(series):
    regex = re.compile( r'"{}".*\{{(.*) \(#(\d+)\.(\d+)\)\}}'.format(series) )

    results = []
    
    with open("ratings.txt", "r") as file:
        for line in file:
            match = regex.search(line)

            if match:
                title = match.group(1)
                season = int(match.group(2))
                episode = int(match.group(3))

                results.append( (season, episode, title) )

    results.sort()

    return [ title for (season, episode, title) in results ]


def best_movie_from_year(year, minimum_count = 10000):
    regex = re.compile( r'^\s+[0-9.]{{10}}\s+(\d+)   (\d{{1,2}}\.\d)  ([^"]+) \({}\)$'.format(year) )

    best_score = 0
    best_title = None
    
    with open("ratings.txt", "r") as file:
        for line in file:
            match = regex.search(line)

            if match:
                count = int(match.group(1))
                score = float(match.group(2))
                title = match.group(3)

                if score > best_score and count > minimum_count:
                    best_score = score
                    best_title = title

    return (best_title, best_score)


def series_average_ratings():
    regex = re.compile( r'^\s+[0-9.]+\s+\d+\s+(\d{1,2}\.\d)\s+"([^"]+)"' )
    results = {}

    with open("ratings.txt", "r") as file:
        for line in file:
            match = regex.search(line)

            if match:
                rating = float(match.group(1))
                title = match.group(2)

                if not title in results:
                    results[title] = []

                results[title].append(rating)

    return sorted([(title, sum(ratings) / len(ratings)) for title, ratings in results.items()], key=lambda pair: pair[1])
