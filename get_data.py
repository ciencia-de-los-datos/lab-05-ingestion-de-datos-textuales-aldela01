'''This script is used to get the data from the txt files contained in the test and train folders.
The data comes from a sentiment analysis dataset, which contains phrases and their respective sentiment, 
which can be positive, negative or neutral.

The train and test folders contain the folders positive, negative and neutral, which contain the txt files with the phrases.

So, this script reads the txt files and creates a csv file with the phrases and their respective sentiment.

In order to do that, the script uses the os and pandas libraries.

'''

import os
import pandas as pd

def get_data(folder):
    """Get data from the txt files in the given folder."""
    phrases = []
    sentiments = []
    for sentiment in os.listdir(folder):
        sentiment_folder = os.path.join(folder, sentiment)
        #Ignore files that are not directories
        if not os.path.isdir(sentiment_folder):
            continue
        for file in os.listdir(sentiment_folder):
            '''Ignore files that are not txt files'''
            if not file.endswith(".txt"):
                continue
            with open(os.path.join(sentiment_folder, file), "r") as f:
                phrases.append(f.read())
                sentiments.append(sentiment)
    df = pd.DataFrame({"phrase": phrases, "sentiment": sentiments})          
    return df

def drop_nulls(df):
    """Drop rows with null values."""
    #Transform NaN values to None
    df = df.where(pd.notnull(df), None)
    return df.dropna()

def save_data(df, filename):
    """Save the data to a csv file."""
    #If the file already exists, it will be overwritten
    df.to_csv(filename, index=False)

def main():
    #Get the data from the train folder
    train = get_data("train")
    #Drop rows with null values
    train = drop_nulls(train)
    #Save the data to a csv file
    save_data(train, "train_dataset.csv")

    #Get the data from the test folder
    test = get_data("test")
    #Drop rows with null values
    #test = drop_nulls(test)
    #Save the data to a csv file
    save_data(test, "test_dataset.csv")

if __name__ == "__main__":
    main()

# train = get_data("train")
# #print(train.sentiment.value_counts())
# print(train[train['sentiment']=="positive"])
# test = get_data("test")
# #print(test[test['sentiment']=="positive"])
# print(test.sentiment.value_counts())