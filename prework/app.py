

success_estimates = {
    'Australia': [0.6, 0.33, 0.11, 0.14],
    'France': [0.66, 0.78, 0.98, 0.2],
    'Italy': [0.6],
    'Brazil': [0.22, 0.22, 0.43],
    'USA': [0.2, 0.5, 0.3],
    'England': [0.45],
    'Canada': [0.25, 0.3],
    'Argentina': [0.22],
    'Greece': [0.45, 0.66, 0.75, 0.99, 0.15, 0.66],
    'Morocco': [0.29],
    'Tunisia': [0.68, 0.56],
    'Egypt': [0.99],
    'Jamaica': [0.61, 0.65, 0.71],
    'Switzerland': [0.73, 0.86, 0.84, 0.51, 0.99],
    'Germany': [0.45, 0.49, 0.36]
}


for country in success_estimates:

    array_country =  success_estimates[country]

    array_country.sort()

    minimous = min(array_country)
    maximous = max(array_country)
    number_of_estimates = len(array_country)
    average = sum(array_country)/number_of_estimates
    meets_policy = False
    if number_of_estimates > 3:
        meets_policy = True

    
    print("Country {0:s}  Min: {1:.2f} Max: {2:.2f} Average: {3:.2f} Number Of Estimates: {4:.2f} MeetsPolicy  {5}".format(country, minimous, maximous, average, number_of_estimates, meets_policy))
 



   

