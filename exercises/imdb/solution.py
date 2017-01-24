import re


def findEpisodeTitles(series):
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


def bestMovieFromYear(year, minimumCount = 10000):
    regex = re.compile( r'^\s+[0-9.]{{10}}\s+(\d+)   (\d{{1,2}}\.\d)  ([^"]+) \({}\)$'.format(year) )

    bestScore = 0
    bestTitle = None
    
    with open("ratings.txt", "r") as file:
        for line in file:
            match = regex.search(line)

            if match:
                count = int(match.group(1))
                score = float(match.group(2))
                title = match.group(3)

                if score > bestScore and count > minimumCount:
                    bestScore = score
                    bestTitle = title

    return (bestTitle, bestScore)


def episodeCount():
    regex = re.compile( r'^\s+[0-9.]+\s+\d+\s+\d{1,2}\.\d\s+"([^"]+)"' )
    results = {}

    with open("ratings.txt", "r") as file:
        for line in file:
            match = regex.search(line)

            if match:
                title = match.group(1)

                if not title in results:
                    results[title] = 0

                results[title] += 1

    return sorted(results.items(), key=lambda pair: pair[1])



def seriesAverageRatings():
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
