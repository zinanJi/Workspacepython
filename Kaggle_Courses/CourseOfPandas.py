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
# describe() is type-aware
print(wine_reviews.points.describe())
print(wine_reviews.taster_name.describe())

# use the mean() functionto see the mean of the points allotted
print(wine_reviews.points.mean())
# use the unique() function see a list of unique values
print(wine_reviews.taster_name.unique())
# use the value_counts() method to see a list of unique values
# and how often they occur in the dataset
print(wine_reviews.taster_name.value_counts())

# Map
review_points_mean = wine_reviews.points.mean()
# this 'centering' transformation is a common preprocessing step 
# before applying various machine learning algorithms.
print(wine_reviews.points.map(lambda p: p - review_points_mean))


# apply() is the equivalent method to transform a whole DataFrame
# by calling a custom method on each row
def remean_points(row):
    row.points = row.points - review_points_mean
    return row


# axis='columns' is to transform each row,
# axis='index', is to transform each column.
wine_reviews.apply(remean_points, axis='columns')

# map() and apply() return new, transformed Series and DataFrames
# But they don't modify the original data they're called on.
print(wine_reviews.head(1).points)

# Pandas provides many common mapping operations as built-ins.
review_points_mean = wine_reviews.points.mean()
print(wine_reviews.points - review_points_mean)
print(wine_reviews.country + " - " + wine_reviews.region_1)

# Groupwise analysis
# eplicate what value_counts() does by doing
print(wine_reviews.groupby('points').points.count())
# to get the cheapest wine in each point value category
print(wine_reviews.groupby('points').price.min())
# This DataFrame is accessible to us directly using the apply() method
# eg. selecting the name of the first wine reviewed from each winery
print(wine_reviews.groupby('winery').apply(lambda df: df.title.iloc[0]))
# group by more than one column for even more fine-grained control
# eg. pick out the best wine by country and province
print(
    wine_reviews.groupby(['country', 'province'
                          ]).apply(lambda df: df.loc[df.points.idxmax()]))

# agg()
# run a bunch of different functions on your DataFrame simultaneously.
print(wine_reviews.groupby('country').price.agg([len, min, max]))

# groupby() will sometimes result in what is called a multi-index.
# A multi-index differs from a regular index in that it has multiple levels.
countries_reviewed = wine_reviews.groupby(['country',
                                           'province']).description.agg([len])
print(countries_reviewed)
mi = countries_reviewed.index
print(type(mi))

# the reset_index() is the one for converting back to a regular index
countries_reviewed.reset_index()

# Sorting
# sort_values() is to get data in the data order not  in index order
countries_reviewed.reset_index()
print(countries_reviewed.sort_values(by='len'))

# sort_values() defaults to an ascending sort,we can set scending=False
print(countries_reviewed.sort_values(by='len', ascending=False))

# use the companion method sort_index() to sort by index values
print(countries_reviewed.sort_index())

# sort by more than one column at a time
print(countries_reviewed.sort_values(by=['country', 'len']))

# Data Types and Missing Values
# The data type for a column in a DataFrame or a Series is known as the dtype.
print(wine_reviews.price.dtype)
print(wine_reviews.dtypes)

# use the astype() function to convert a column of one type into another.
print(wine_reviews.points.astype('float64'))

# A DataFrame or Series index has its own dtype, too
print(wine_reviews.index.dtype)

# Missing data
# Entries missing values are given the value NaN,
# these NaN values are always of the float64 dtype.
# Pandas provides some methods specific to missing data. 
# use pd.isnull() to select NaN entries
print(wine_reviews[pd.isnull(wine_reviews.country)])

# Replacing missing values is a common operation.
# fillna() provides a few different strategies for mitigating such data.
# simply replace each NaN with an "Unknown":
print(wine_reviews.region_2.fillna("Unknown"))

# use replace() to replace a non-null value
# it's handy for replacing missing data which is given some kind of sentinel value in the dataset: 
# things like "Unknown", "Undisclosed", "Invalid", and so on.
print(wine_reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))


# use rename() to   change index names and/or column names
print(wine_reviews.rename(columns={'points': 'score'}))
# specify a index or column keyword parameter, respectively to rename index or column values
print(wine_reviews.rename(index={0: 'firstEntry', 1: 'secondEntry'}))
# rename_axis() method may be used to change the row index and the column index names
print(wine_reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))

# Combining
# concat() is use to smush the data in different DataFrame or Series objects but having the same fields (columns)
canadian_youtube = pd.read_csv("youtube-new/CAvideos.csv")
british_youtube = pd.read_csv("youtube-new/GBvideos.csv")
pd.concat([canadian_youtube, british_youtube])

# merge():Most of what merge() can do can also be done more simply with join()
# join() combine different DataFrame objects which have an index in common
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])

left.join(right, lsuffix='_CAN', rsuffix='_UK')

