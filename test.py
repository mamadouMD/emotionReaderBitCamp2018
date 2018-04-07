import indicoio

API_KEY = "86835201fbce14ccf4eb3986da330f5a"
indicoio.config.api_key = API_KEY

print(indicoio.sentiment_hq("I love writing code!"))
print(indicoio.sentiment_hq("I HATE YOU"))

print(indicoio.sentiment([
    "I love writing code!",
    "Alexander and the Terrible, Horrible, No Good, Very Bad Day"
]))