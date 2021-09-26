import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

melbourne_file_path = 'Kaggle_Courses/melbourne-housing-snapshot/melb_data.csv'

melbourne_data = pd.read_csv(melbourne_file_path)

# print(melbourne_data.describe())
print(melbourne_data.columns)

# dropna drops missing values (think of na as "not available")
melbourne_data = melbourne_data.dropna(axis=0)

y = melbourne_data.Price

# select features from melbourne_data.columns
melbourne_features = [
    'Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude'
]
X = melbourne_data[melbourne_features]

print(X.describe())
print(X.head())

# Define model. Specify a number for random_state(seed) to ensure same results each run
melbourne_model = DecisionTreeRegressor(random_state=1)

# Fit model
melbourne_model.fit(X, y)

print("Making predictions for the following 5 houses:")
print(X.head())
print("The predictions are")
print(melbourne_model.predict(X.head()))

# Validation
# calculate the mean absolute error
predicted_home_prices = melbourne_model.predict(X)
print(mean_absolute_error(y, predicted_home_prices))

# split data into training and validation data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=0)
# Define model
melbourne_model = DecisionTreeRegressor(random_state=0)
# Fit model
melbourne_model.fit(train_X, train_y)
# get predicted prices on validation data
val_predictions = melbourne_model.predict(val_X)
print(mean_absolute_error(val_y, val_predictions))


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes,
                                  random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return (mae)


# compare MAE with differing values of max_leaf_nodes
for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: %d  \t\t Mean Absolute Error:  %d" %
          (max_leaf_nodes, my_mae))

# Random Forest
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X, train_y)
melb_preds = forest_model.predict(val_X)
print(mean_absolute_error(val_y, melb_preds))

# Train a model for the competition¶
# To improve accuracy, create a new Random Forest model
#  which you will train on all training data
forest_model_on_full_data = RandomForestRegressor(random_state=1)
# fit forest_model_on_full_data on all data from the training data
forest_model_on_full_data.fit(X, y)
# path to file you will use for predictions
test_data_path = 'Kaggle_Courses/melbourne-housing-snapshot/melb_data.csv'
# read test data file using pandas
test_data = pd.read_csv(test_data_path)
# create test_X which comes from test_data,
# but includes only the columns you used for prediction.
test_X = test_data[melbourne_features]
# make predictions which we will submit.
test_preds = forest_model_on_full_data.predict(test_X)

output = pd.DataFrame({'Id': test_data.Id, 'SalePrice': test_preds})
output.to_csv('submission.csv', index=False)
