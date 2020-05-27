import Tools
import Validations
import Data_visaulisation as plot

dates = Tools.get_dates_vector()

def get_all_info_by_country():
    country_name = input('Ingrese el nombre del pais que desea consultar:')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()

    raw_confirmed, raw_recovered, raw_deaths       = Tools.get_info_by_country_name(country_name)
    confirmed_cases, recovered_cases, deaths_cases = Tools.get_clear_vector_info(raw_confirmed, raw_recovered, raw_deaths)

    first_index, last_index = Tools.indexes_to_remove_zeros(confirmed_cases)
    confirmed_cases = confirmed_cases[ first_index:last_index ]
    recovered_cases = recovered_cases[ first_index:last_index ]
    deaths_cases    = deaths_cases[ first_index:last_index ]
    dates           = dates[ first_index:last_index ]

    plot.show_all_country_info(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)

def get_confirmed_cases_by_country():
    country_name = input('Ingrese el nombre del pais que desea consultar:')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    confirmed_cases = Tools.get_confirmed_cases(country_name)
    plot.show_country_confirmed_cases(dates, confirmed_cases, country_name)

def get_recovered_cases_by_country():
    country_name = input('Ingrese el nombre del pais que desea consultar:')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    recovered_cases = Tools.get_recovered_cases(country_name)
    plot.show_country_recovered_cases(dates, recovered_cases, country_name)
    
def get_deaths_cases_by_country():
    country_name = input('Ingrese el nombre del pais que desea consultar:')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    deaths_cases = Tools.get_deaths_cases(country_name)
    plot.show_country_deaths_cases(dates, deaths_cases, country_name)

def get_active_cases_by_country():
    country_name = input('Ingrese el nombre del pais que desea consultar:')

    # Si el nombre del pais no empiza con mayuscula o el campo esta vacio
    if Validations.capital_letter(country_name) and Validations.check_empty_country_name(country_name): 
        country_name = country_name.capitalize()    

    confirmed_cases, recovered_cases, deaths_cases = Tools.get_info_by_country_name(country_name)
    confirmed_cases                                = Tools.clear_vector(confirmed_cases)
    recovered_cases                                = Tools.clear_vector(recovered_cases)
    deaths_cases                                   = Tools.clear_vector(deaths_cases)

    plot.show_country_active_cases(dates, confirmed_cases, recovered_cases, deaths_cases, country_name)

print(""" Bienvenido. Aqui puedes consulatr información acerca del COVID-19,
como casos confirmados, recuperaciones, decesos y casos activos en 
en el país que gustes consultar. O si lo prefieres, Contrastar la
información entre 2 paises. Este programa se alimenta de la información
proporsionada y recolectada por  the Johns Hopkins University Center 
for Systems Science and Engineering (JHU CCSE) de diversas fuentes 
como the World Health Organization (WHO), DXY.cn, BNO News, National 
Health Commission of the People’s Republic of China (NHC), China CDC (CCDC), 
Hong Kong Department of Health, Macau Government, Taiwan CDC, US CDC, 
Government of Canada, Australia Government Department of Health, European 
Centre for Disease Prevention and Control (ECDC), Ministry of Health Singapore (MOH), 
entre otros. 

Puedes consultar las fuentes aqui: 
https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports 
o en el sitio web: https://data.humdata.org/dataset/novel-coronavirus-2019-ncov-cases 

# --- --- MENU PRINCIPAL --- --- #
1 - Listado de todos los paises 
2 - Toda la información referente a un país 
3 - Casos confirmados de un país
4 - Casos recuperados de un país
5 - Decesos de un país
6 - Casos activos de un país
7 - Comparar casos confirmados entre 2 paises
8 - Comparar casos recuperados entre 2 paises 
9 - Comparar decesos entre 2 paises 
10 - Comparar casos activos entre 2 paisescle
11 - Salir """)

options = {
    '1': Tools.show_all_countrys,
    '2': get_all_info_by_country,
    '3': get_confirmed_cases_by_country,
    '4': get_recovered_cases_by_country,
    '5': get_deaths_cases_by_country,
    '6': get_active_cases_by_country,
    '7': 'Tools.siete',
    '8': 'Tools.ocho',
    '9': 'Tools.nueve',
    '10': 'Tools.diez',
    '11': 'Exit'
}

option_selected = input('Elige una opción: ')
options[option_selected]()

# active_cases = confirmed_cases[ len(confirmed_cases)-1 ] - recovered_cases[ len(recovered_cases)-1 ]
# print(str(active_cases) + ' casos activos en ' + country_name)
