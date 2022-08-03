import pandas as pd
from util import add_surrogate_key, get_country_key, get_year_key, get_education_key, get_health_key, get_quality_of_life_key, get_population_key, get_event_key, get_quality_of_life_index_vals, get_development_index_val, get_human_development_index_vals
from constant import COUNTRIES, YEAR, INDICATORS


def preprocess_country(data):
    columns = [
        'name',
        'code',
        'capital',
        'continent',
        'region',
        'currency',
        'income_group',
        'gdp',
        'area',
        'population',
        'birth_rate',
        'death_rate'
    ]

    df = pd.DataFrame(data=data.values, columns=columns)

    add_surrogate_key('country', df)

    return df


def preprocess_year():
    data = []

    columns = [
        'year',
        'decade'
    ]

    for year in range(YEAR['start'], YEAR['end'] + 1):
        row = {}

        row['year'] = year
        row['decade'] = year - year % 10

        data.append(row)

    df = pd.DataFrame(data=data, columns=columns)

    add_surrogate_key('year', df)

    return df


def preprocess_indicator(indicator, indicator_data):
    data = []

    columns = ['country', 'year'] + list(INDICATORS[indicator].keys())

    for country in COUNTRIES:
        for year in range(YEAR['start'], YEAR['end'] + 1):
            row = {}

            row['country'] = country
            row['year'] = year

            for col, lbl in INDICATORS[indicator].items():
                val = indicator_data.loc[(indicator_data['Series Name'] == lbl) & (
                    indicator_data['Country Code'] == country), '{year} [YR{year}]'.format(year=year)].values[0]

                if val != '..':
                    row[col] = val

            data.append(row)

    df = pd.DataFrame(data=data, columns=columns)

    df.dropna(thresh=len(df.columns) // 2)

    add_surrogate_key(indicator, df)

    return df


def preprocess_event(data):

    columns = [
        'country',
        'type',
        'description',
        'start_year',
        'start_month',
        'start_day',
        'end_year',
        'end_month',
        'end_day',
        'outcome',
        'source'
    ]

    df = pd.DataFrame(data=data.values, columns=columns)

    add_surrogate_key('event', df)

    return df


def preprocess_fact(country_df, year_df, education_df, health_df, quality_of_life_df, population_df, event_df, quality_of_life_index_data, development_index_data, human_development_index_data):
    data = []

    columns = [
        'country',
        'year',
        'education',
        'health',
        'quality_of_life',
        'population',
        # 'event',
        'quality_of_life_index',
        'development_index',
        'human_development_index'
    ]

    for country in COUNTRIES:
        for year in range(YEAR['start'], YEAR['end'] + 1):
            row = {}

            row['country'] = get_country_key(country, country_df)
            row['year'] = get_year_key(year, year_df)

            row['education'] = get_education_key(country, year, education_df)
            row['health'] = get_health_key(country, year, health_df)
            row['quality_of_life'] = get_quality_of_life_key(
                country, year, quality_of_life_df)
            row['population'] = get_population_key(
                country, year, population_df)
            # row['event'] = get_event_key(country, year, event_df)

            row['quality_of_life_index'] = get_quality_of_life_index_vals(
                country, year, quality_of_life_index_data)
            row['development_index'] = get_development_index_val(
                country, development_index_data)
            row['human_development_index'] = get_human_development_index_vals(
                country, year, human_development_index_data)

            data.append(row)

    df = pd.DataFrame(data=data, columns=columns)

    return df
