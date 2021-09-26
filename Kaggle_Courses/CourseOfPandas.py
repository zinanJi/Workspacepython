import pandas as pd
""" DataFrame
            Bob	            Sue
Product A	I liked it.	    Pretty good.
Product B	It was awful.   Bland.
"""
pd.DataFrame(
    {
        'Bob': ['I liked it.', 'It was awful.'],
        'Sue': ['Pretty good.', 'Bland.']
    },
    index=['Product A', 'Product B'])
""" Series
2015 Sales    30
2016 Sales    35
2017 Sales    40
Name: Product A, dtype: int64
"""
pd.Series([30, 35, 40],
          index=['2015 Sales', '2016 Sales', '2017 Sales'],
          name='Product A')

wine_reviews = pd.read_csv(
    "Kaggle_Courses/wine-reviews/winemag-data-130k-v2.csv")
# in this dataset that the CSV file has a built-in index,
# which pandas did not pick up on automatically
# we can specify an index_col to make pandas use a column for the index
# (instead of creating a new one from scratch),
wine_reviews = pd.read_csv(
    "Kaggle_Courses/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

# use the shape attribute to check how large the resulting DataFrame is:
wine_reviews.shape
# using the head() command, which grabs the first five rows of the DataFrame:
wine_reviews.head()

pd.set_option('max_rows', 5)

print(wine_reviews)


# access the country property of wine_reviews
print(wine_reviews.country)
# If we have a Python dictionary,
# we can access its values using the indexing ([]) operator.
# the indexing operator [] does have the advantage
# that it can handle column names with reserved characters in them
print(wine_reviews['country'])
# drill down to a single specific value
print(wine_reviews['country'][0])

# first paradigm:index-based selection——iloc
# select the first row of data in a DataFrame
print(wine_reviews.iloc[0])
# to get a column with iloc
print(wine_reviews.iloc[:, 0])
# to select the first column from just the second, and third row
print(wine_reviews.iloc[1:3, 0])
print(wine_reviews.iloc[[1, 2], 0])
# negative numbers can be used in selection
print(wine_reviews.iloc[-5:])

# second paradigm:label-based selection——loc
# the data index value matters
print(wine_reviews.loc[0, 'country'])
print(wine_reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']])

# manipulating the index
# wine_reviews.set_index("title")

# Conditional selection
print(wine_reviews.loc[(wine_reviews.country == 'Italy')
                       & (wine_reviews.points >= 90)])
# isin is lets you select data whose value "is in" a list of values
print(wine_reviews.loc[wine_reviews.country.isin(['Italy', 'France'])])
# isnull (and its companion notnull)
# let you highlight values which are (or are not) empty (NaN).
print(wine_reviews.loc[wine_reviews.price.notnull()])

# assigning data
# wine_reviews['critic'] = 'everyone'
# wine_reviews['index_backwards'] = range(len(reviews), 0, -1)


# Summary Functions and Maps
