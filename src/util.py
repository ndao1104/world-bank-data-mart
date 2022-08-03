def add_surrogate_key(development_indexmension, df):
    key = '{development_indexmension}_key'.format(
        development_indexmension=development_indexmension)

    df[key] = df.index + 1
    df.insert(0, key, df.pop(key))

# def get_sql_col_str(col, dtype) {
#     sql_col_str = '{col} {sqltype}'
#     return
# }


def get_country_key(country, country_df):
    country_key = country_df.loc[(
        country_df['code'] == country), 'country_key'].values[0]

    return country_key


def get_year_key(year, year_df):
    year_key = year_df.loc[(
        year_df['year'] == year), 'year_key'].values[0]

    return year_key


def get_education_key(country, year, education_df):
    education_key = education_df.loc[(education_df['country'] == country) & (
        education_df['year'] == year), 'education_key'].values[0]

    return education_key


def get_health_key(country, year, health_df):
    health_key = health_df.loc[(health_df['country'] == country) & (
        health_df['year'] == year), 'health_key'].values[0]

    return health_key


def get_quality_of_life_key(country, year, quality_of_life_df):
    quality_of_life_key = quality_of_life_df.loc[(quality_of_life_df['country'] == country) & (
        quality_of_life_df['year'] == year), 'quality_of_life_key'].values[0]

    return quality_of_life_key


def get_population_key(country, year, population_df):
    population_key = population_df.loc[(population_df['country'] == country) & (
        population_df['year'] == year), 'population_key'].values[0]

    return population_key


def get_event_key(country, year, event_df):
    event_vals = event_df.loc[(event_df['country'] == country) & (
        event_df['start_year'] == year), 'event_key'].values

    if len(event_vals) != 0:
        event_val = int(event_vals[0])
    else:
        event_val = None

    return event_val

def get_quality_of_life_index_vals(country, year, quality_of_life_index_data):
    quality_of_life_index_vals = quality_of_life_index_data.loc[(quality_of_life_index_data['Code'] == country) & (
        quality_of_life_index_data['Year'] == year), 'Quality of Life Index'].values

    if len(quality_of_life_index_vals) != 0:
        if quality_of_life_index_vals[0] >= 175:
            quality_of_life_index_val = 1
        elif quality_of_life_index_vals[0] >= 150:
            quality_of_life_index_val = 2
        elif quality_of_life_index_vals[0] >= 125:
            quality_of_life_index_val = 3
        elif quality_of_life_index_vals[0] >= 100:
            quality_of_life_index_val = 4
        else:
            quality_of_life_index_val = 5

        quality_of_life_index_val = int(quality_of_life_index_val)
    else:
        quality_of_life_index_val = None

    return quality_of_life_index_val


def get_development_index_val(country, development_index_data):
    development_index_vals = development_index_data.loc[(development_index_data['Code'] == country),
                                                      'Development Index'].values

    if development_index_vals[0] == 'developed':
        development_index_val = 1
    elif development_index_vals[0] == 'developing':
        development_index_val = 2
    else:
        development_index_val = 3

    return int(development_index_val)


def get_human_development_index_vals(country, year, human_development_index_data):
    human_development_index_vals = human_development_index_data.loc[(human_development_index_data['Code'] == country) & (
        human_development_index_data['Year'] == year), 'Human Development Index'].values

    if len(human_development_index_vals) != 0:
        if human_development_index_vals[0] >= 0.8 and human_development_index_vals[0] <= 1:
            human_development_index_val = 1
        elif human_development_index_vals[0] >= 0.7:
            human_development_index_val = 2
        elif human_development_index_vals[0] >= 0.55:
            human_development_index_val = 3
        else:
            human_development_index_val = 4
    else:
        human_development_index_val = 5

    return int(human_development_index_val)
