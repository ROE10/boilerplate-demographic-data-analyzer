import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv', header=None, names=[
    'age', 'workclass', 'fnlwgt', 'education', 'education-num',
    'marital-status', 'occupation', 'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary'
])

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df ['race'].value_counts()
    print(race_count)

    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    print(f"Average age of men: {average_age_men:.2f}")

    # What is the percentage of people who have a Bachelor's degree?
    total_count = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = (bachelors_count / total_count) * 100
    print(f"Percentage with Bachelors degrees: {percentage_bachelors:.2f}%")

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']
    advanced_edu_df = df[df['education'].isin(advanced_education)]
    percentage_advanced_edu_high_income = (len(advanced_edu_df[advanced_edu_df['salary'] == '>50K']) / len(advanced_edu_df)) * 100
    print(f"Percentage with advanced education earning >50K: {percentage_advanced_edu_high_income:.2f}%")
    # What percentage of people without advanced education make more than 50K?
    non_advanced_edu_df = df[~df['education'].isin(advanced_education)]
    percentage_non_advanced_edu_high_income = (len(non_advanced_edu_df[non_advanced_edu_df['salary'] == '>50K']) / len(non_advanced_edu_df)) * 100
    print(f"Percentage without advanced education earning >50K: {percentage_non_advanced_edu_high_income:.2f}%")

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = ['Bachelors', 'Masters', 'Doctorate']
    lower_education =  df[~df['education'].isin(advanced_education)]

    # percentage with salary >50K
    higher_education_rich = df[df['education'].isin(advanced_education)]
    percentage_advanced_edu_high_income = (len(advanced_edu_df[advanced_edu_df['salary'] == '>50K']) / len(advanced_edu_df)) * 100
    print(f"Percentage with advanced education earning >50K: {percentage_advanced_edu_high_income:.2f}%")
    lower_education_rich = df[~df['education'].isin(advanced_education)]
    percentage_non_advanced_edu_high_income = (len(non_advanced_edu_df[non_advanced_edu_df['salary'] == '>50K']) / len(non_advanced_edu_df)) * 100
    print(f"Percentage without advanced education earning >50K: {percentage_non_advanced_edu_high_income:.2f}%")

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    print(f"Minimum work hours per week: {min_work_hours}")

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = (len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100
    print(f"Percentage of people working minimum hours earning >50K: {percentage_min_workers_high_income:.2f}%")

    # What country has the highest percentage of people that earn >50K?
    country_salary_df = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary_df['>50K'] = country_salary_df['>50K'].fillna(0)
    highest_earning_country = country_salary_df['>50K'].idxmax()
    highest_earning_country_percentage = country_salary_df['>50K'].max() * 100

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = india_high_income = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_occupation_india = india_high_income['occupation'].value_counts().idxmax()
    print(f"Most popular occupation in India for those earning >50K: {top_occupation_india}")

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
