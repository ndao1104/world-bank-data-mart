from preprocessing import *
from db import *
import pandas as pd
import psycopg2
from constant import PATH, TABLES, INDICATORS

country_data = pd.read_csv(PATH['in']['dimension'] + 'country.csv')
event_data = pd.read_csv(PATH['in']['dimension'] + 'event.csv')
education_data = pd.read_csv(PATH['in']['dimension'] + 'education.csv')
health_data = pd.read_csv(PATH['in']['dimension'] + 'health.csv')
quality_of_life_data = pd.read_csv(
    PATH['in']['dimension'] + 'quality_of_life.csv')
population_data = pd.read_csv(PATH['in']['dimension'] + 'population.csv')

quality_of_life_index_data = pd.read_csv(
    PATH['in']['fact'] + 'quality_of_life_index.csv')
development_index_data = pd.read_csv(
    PATH['in']['fact'] + 'development_index.csv')
human_development_index_data = pd.read_csv(
    PATH['in']['fact'] + 'human_development_index.csv')

country_df = preprocess_country(country_data)
year_df = preprocess_year()
education_df = preprocess_indicator('education', education_data)
health_df = preprocess_indicator('health', health_data)
quality_of_life_df = preprocess_indicator(
    'quality_of_life', quality_of_life_data)
population_df = preprocess_indicator('population', population_data)
event_df = preprocess_event(event_data)
print(event_df)

fact_df = preprocess_fact(country_df, year_df, education_df, health_df, quality_of_life_df, population_df,
                          event_df, quality_of_life_index_data, development_index_data, human_development_index_data)

country_df.to_csv(PATH['out']['dimension'] + 'country.csv', index=False)
year_df.to_csv(PATH['out']['dimension'] + 'year.csv', index=False)
education_df.to_csv(PATH['out']['dimension'] + 'education.csv', columns=[
                    'education_key'] + list(INDICATORS['education'].keys()), index=False)
health_df.to_csv(PATH['out']['dimension'] + 'health.csv',
                 columns=['health_key'] + list(INDICATORS['health'].keys()), index=False)
quality_of_life_df.to_csv(
    PATH['out']['dimension'] + 'quality_of_life.csv', columns=['quality_of_life_key'] + list(INDICATORS['quality_of_life'].keys()), index=False)
population_df.to_csv(PATH['out']['dimension'] + 'population.csv', columns=[
                     'population_key'] + list(INDICATORS['population'].keys()), index=False)
event_df.to_csv(PATH['out']['dimension'] + 'event.csv', columns=['event_key', 'type', 'description', 'start_year',
                                                                 'start_month', 'start_day', 'end_year', 'end_month', 'end_day', 'outcome', 'source'], index=False)

fact_df.to_csv('data/processed/fact.csv', index=False)


DB_HOST = 'localhost'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'postgres'

conn = psycopg2.connect(host=DB_HOST,
                        dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD)

cur = conn.cursor()

for dimension_table in TABLES['dimensions']:
    cur.execute(get_drop_table_str(dimension_table))
    
    a = get_create_table_str(dimension_table)

    cur.execute(get_create_table_str(dimension_table))

    file = open(PATH['out']['dimension'] + dimension_table + '.csv')
    cur.copy_expert(sql=get_copy_table_str(dimension_table), file=file)


cur.execute(get_drop_table_str(TABLES['fact']))

cur.execute(get_create_table_str(TABLES['fact']))

file = open(PATH['out']['fact'])
cur.copy_expert(sql=get_copy_table_str(TABLES['fact']), file=file)

conn.commit()

cur.close()

conn.close()
