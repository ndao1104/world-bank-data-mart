def get_drop_table_str(table_name):
    drop_table_str = 'DROP TABLE IF EXISTS {table_name}'.format(
        table_name=table_name)

    return drop_table_str


def get_create_table_str(table_name):
    if table_name == 'country':
        create_table_str = '''
            CREATE TABLE country (
                country_key INTEGER PRIMARY KEY NOT NULL,
                name VARCHAR,
                code VARCHAR,
                capital VARCHAR,
                continent VARCHAR,
                region VARCHAR,
                currency VARCHAR,
                income_group VARCHAR,
                gdp FLOAT,
                area INTEGER,
                population INTEGER,
                birth_rate FLOAT,
                death_rate FLOAT
            )
        '''
    elif table_name == 'year':
        create_table_str = '''
            CREATE TABLE year (
                year_key INTEGER PRIMARY KEY NOT NULL,
                year INTEGER,
                decade INTEGER
            )
        '''
    elif table_name == 'education':
        create_table_str = '''
            CREATE TABLE education (
                education_key INTEGER PRIMARY KEY NOT NULL,
                literacy_rate_total FLOAT,
                literacy_rate_male FLOAT,
                literacy_rate_female FLOAT,
                enrollment_rate_primary_total FLOAT,
                enrollment_rate_primary_male FLOAT,
                enrollment_rate_primary_female FLOAT,
                enrollment_rate_secondary_total FLOAT,
                enrollment_rate_secondary_male FLOAT,
                enrollment_rate_secondary_female FLOAT,
                enrollment_rate_tertiary_total FLOAT,
                enrollment_rate_tertiary_male FLOAT,
                enrollment_rate_tertiary_female FLOAT,
                public_education_spending FLOAT
            )
        '''
    elif table_name == 'health':
        create_table_str = '''
            CREATE TABLE health (
                health_key INTEGER PRIMARY KEY NOT NULL,
                prevalence_stunting FLOAT,
                prevalence_overweight FLOAT,
                prevalence_diabetes FLOAT,
                prevalence_hiv FLOAT,
                immunization_bcg INTEGER,
                immunization_dpt INTEGER,
                immunization_hep INTEGER,
                immunization_pol INTEGER,
                immunization_measles_1 INTEGER,
                immunization_measles_2 INTEGER,
                death_rate_stillbirth INTEGER,
                death_rate_infant INTEGER,
                num_surgical_procedure INTEGER,
                num_hospital_beds FLOAT,
                num_nurse_midwife FLOAT,
                num_physician FLOAT,
                domestic_health_expenditure FLOAT
            )
        '''
    elif table_name == 'quality_of_life':
        create_table_str = '''
            CREATE TABLE quality_of_life (
                quality_of_life_key INTEGER PRIMARY KEY NOT NULL,
                gni FLOAT,
                hci_total FLOAT,
                hci_male FLOAT,
                hci_female FLOAT,
                poverty_headcount_ratio FLOAT,
                labor_force_total FLOAT,
                unemployment_rate_total FLOAT,
                unemployment_rate_male FLOAT,
                unemployment_rate_female FLOAT,
                access_to_drinking_water FLOAT,
                access_to_sanitation FLOAT,
                access_to_handwashing_facilities FLOAT
            )
        '''
    elif table_name == 'population':
        create_table_str = '''
            CREATE TABLE population (
                population_key INTEGER PRIMARY KEY NOT NULL,
                population_total FLOAT,
                population_male FLOAT,
                population_female FLOAT,
                population_urban FLOAT,
                population_urban_percentage FLOAT,
                population_urban_growth FLOAT,
                population_rural FLOAT,
                population_rural_percentage FLOAT,
                population_rural_growth FLOAT,
                life_expectancy_total FLOAT,
                life_expectancy_male FLOAT,
                life_expectancy_female FLOAT,
                net_migration FLOAT
            )
        '''
    elif table_name == 'event':
        create_table_str = '''
            CREATE TABLE event (
                event_key INTEGER PRIMARY KEY NOT NULL,
                type INTEGER,
                description VARCHAR,
                start_year INTEGER,
                start_month INTEGER,
                start_day INTEGER,
                end_year INTEGER,
                end_month INTEGER,
                end_day INTEGER,
                outcome VARCHAR,
                source VARCHAR
            )
        '''
    elif table_name == 'fact':
        # create_table_str = '''
        #     CREATE TABLE fact (
        #         country INTEGER,
        #         year INTEGER,
        #         education INTEGER,
        #         health INTEGER,
        #         quality_of_life INTEGER,
        #         population INTEGER,
        #         event INTEGER,
        #         quality_of_life_index INTEGER,
        #         development_index INTEGER,
        #         human_development_index INTEGER
        #     )
        # '''
        create_table_str = '''
            CREATE TABLE fact (
                country INTEGER,
                year INTEGER,
                education INTEGER,
                health INTEGER,
                quality_of_life INTEGER,
                population INTEGER,
                quality_of_life_index INTEGER,
                development_index INTEGER,
                human_development_index INTEGER
            )
        '''
    else:
        create_table_str = None

    return create_table_str


def get_copy_table_str(table_name):
    copy_table_str = 'COPY {table_name} FROM stdin WITH CSV HEADER DELIMITER AS \',\''.format(
        table_name=table_name)

    return copy_table_str