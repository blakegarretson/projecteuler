#data = {1900:[]}
years = [x for x in range(1900, 2001)]
print(years)
#days_in_years = {x:366 if (((x % 4) == 0) and (x != 1900)) else x:365 for x in years }
leap_years = [True if (((x % 4) == 0) and (x != 1900)) else False for x in years ]
print(leap_years)

answer = 0

daysofweek = {
    'mo':'tu',
    'tu':'we',
    'we':'th',
    'th':'fr',
    'fr':'sa',
    'sa':'su',
    'su':'mo',
}

current_day = 'mo'

months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

daysinmonth = {
    'jan': 31,
    'feb': 28,
    'feb_leap': 29,
    'mar': 31,
    'apr': 30,
    'may': 31,
    'jun': 30,
    'jul': 31,
    'aug': 31,
    'sep': 30,
    'oct': 31,
    'nov': 30,
    'dec': 31,
}

for year, leap in zip(years, leap_years):
    print(year)
    for month in months:
        print("  ",month)
        if leap and month == 'feb': month = 'feb_leap'
        days = daysinmonth[month]
        print("      First day of month:", current_day)
        if current_day == 'su' and year > 1900: answer += 1
        for x in range(0, days):
            current_day = daysofweek[current_day]
            
            
print("Answer:", answer)