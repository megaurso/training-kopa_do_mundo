from teams.exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError

data = {
    "name": "França",
    "titles": 9,
    "top_scorer": "Zidane",
    "fifa_code": "FRA",
    "first_cup": "2002-10-18",
}


def data_processing(times):

    year = int(times["first_cup"][0:4])
    list_years = []
    how_many_years = []

    for list_year in range(1930, 2023, 4):
        list_years.append(list_year)

    for how_many in range(year, 2023, 4):
        how_many_years.append(how_many)

    if times["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")

    if year not in list_years:
        raise InvalidYearCupError("there was no world cup this year")

    if len(how_many_years) < times["titles"]:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")


