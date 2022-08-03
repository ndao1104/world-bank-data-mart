PATH = {
    'in': {
        'dimension': 'data/raw/dimensions/',
        'fact': 'data/raw/measures/'
    },
    'out': {
        'dimension': 'data/processed/dimensions/',
        'fact': 'data/processed/fact.csv'
    }
}

TABLES = {
    'dimensions': [
        'country',
        'year',
        'education',
        'health',
        'quality_of_life',
        'population',
        'event',

    ],
    'fact': 'fact'
}

COUNTRIES = [
    'ARG',
    'BGD',
    'BRA',
    'CAN',
    'COL',
    'IND',
    'MEX',
    'PAK',
    'USA'
]

YEAR = {
    'start': 2005,
    'end': 2020
}

INDICATORS = {
    'education': {
        'literacy_rate_total': 'Literacy rate, adult total (% of people ages 15 and above)',
        'literacy_rate_male': 'Literacy rate, adult male (% of males ages 15 and above)',
        'literacy_rate_female': 'Literacy rate, adult female (% of females ages 15 and above)',
        'enrollment_rate_primary_total': 'School enrollment, primary (% gross)',
        'enrollment_rate_primary_male': 'School enrollment, primary, male (% gross)',
        'enrollment_rate_primary_female': 'School enrollment, primary, female (% gross)',
        'enrollment_rate_secondary_total': 'School enrollment, secondary (% gross)',
        'enrollment_rate_secondary_male': 'School enrollment, secondary, male (% gross)',
        'enrollment_rate_secondary_female': 'School enrollment, secondary, female (% gross)',
        'enrollment_rate_tertiary_total': 'School enrollment, tertiary (% gross)',
        'enrollment_rate_tertiary_male': 'School enrollment, tertiary, male (% gross)',
        'enrollment_rate_tertiary_female': 'School enrollment, tertiary, female (% gross)',
        'public_education_spending': 'Public spending on education, total (% of GDP)'
    },
    'health': {
        'prevalence_stunting': 'Prevalence of stunting, height for age (% of children under 5)',
        'prevalence_overweight': 'Prevalence of overweight (% of adults)',
        'prevalence_diabetes': 'Diabetes prevalence (% of population ages 20 to 79)',
        'prevalence_hiv': 'Prevalence of HIV, total (% of population ages 15-49)',
        'immunization_bcg': 'Immunization, BCG (% of one-year-old children)',
        'immunization_dpt': 'Immunization, DPT (% of children ages 12-23 months)',
        'immunization_hep': 'Immunization, HepB3 (% of one-year-old children)',
        'immunization_pol': 'Immunization, Pol3 (% of one-year-old children)',
        'immunization_measles_1': 'Immunization, measles (% of children ages 12-23 months)',
        'immunization_measles_2': 'Immunization, measles second dose (% of children by the nationally recommended age)',
        'death_rate_stillbirth': 'Number of stillbirths',
        'death_rate_infant': 'Number of infant deaths',
        'num_surgical_procedure': 'Number of surgical procedures (per 100,000 population)',
        'num_hospital_beds': 'Hospital beds (per 1,000 people)',
        'num_nurse_midwife': 'Nurses and midwives (per 1,000 people)',
        'num_physician': 'Physicians (per 1,000 people)',
        'domestic_health_expenditure': 'Domestic general government health expenditure (% of GDP)'
    },
    'quality_of_life': {
        'gni': 'GNI per capita, Atlas method (current US$)',
        'hci_total': 'Human capital index (HCI) (scale 0-1)',
        'hci_male': 'Human capital index (HCI), male (scale 0-1)',
        'hci_female': 'Human capital index (HCI), female (scale 0-1)',
        'poverty_headcount_ratio': 'Poverty headcount ratio at national poverty line (% of population)',
        'labor_force_total': 'Labor force, total',
        'unemployment_rate_total': 'Unemployment, total (% of total labor force)',
        'unemployment_rate_male': 'Unemployment, male (% of male labor force)',
        'unemployment_rate_female': 'Unemployment, female (% of female labor force)',
        'access_to_drinking_water': 'People using at least basic drinking water services (% of population)',
        'access_to_sanitation': 'People using at least basic sanitation services (% of population)',
        'access_to_handwashing_facilities': 'People with basic handwashing facilities including soap and water (% of population)'
    },
    'population': {
        'population_total': 'Population, total',
        'population_male': 'Population, male',
        'population_female': 'Population, female',
        'population_urban': 'Urban population',
        'population_urban_percentage': 'Urban population (% of total population)',
        'population_urban_growth': 'Urban population growth (annual %)',
        'population_rural': 'Rural population',
        'population_rural_percentage': 'Rural population (% of total population)',
        'population_rural_growth': 'Rural population growth (annual %)',
        'life_expectancy_total': 'Life expectancy at birth, total (years)',
        'life_expectancy_male': 'Life expectancy at birth, male (years)',
        'life_expectancy_female': 'Life expectancy at birth, female (years)',
        'net_migration': 'Net migration'
    }
}
