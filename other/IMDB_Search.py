import requests


def IMDB_Search(keyword):
    """
    Base on the name of the movie return the information about the movie

    :param keyword: name of the movie
    :return: information dict
    """

    url = "https://v2.sg.media-imdb.com/suggests/"
    first_letter = keyword[0]
    json_path = "/" + keyword + ".json"

    response = requests.get(url+first_letter+json_path)
    print(response.text)
    

# response = requests.get("https://v2.sg.media-imdb.com/suggests/h/hello.json")
# print(response.text)

IMDB_Search("hello")
