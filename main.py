import pandas as pd
import numpy as np


def identify_customers(data: pd.DataFrame) -> np.ndarray:
    """
    Function that accepts a dataset and returns a binary array showing which customers to contact.
    This function will be called to evaluate your program - DO NOT CHANGE ITS SIGNATURE
    :param data: DataFrame with the same format as 3625_assign2_data_train, BUT without the target column (the "sucess" column")
    :return: a binary array of length "n", where n is the number of instances in data. Indices set to 1 indicate the customers 
            from data that should be contacted
    """
    # your code here



if __name__ == '__main__':

    # example of how to load the training data, splitting into x and y
    dataset = pd.read_csv('./data/3625_assign2_data_train.csv', index_col=None)

    x = dataset.drop('success', axis=1)
    y = dataset['success']

    print(f'number of instances: {x.shape[0]}, number of attributes: {x.shape[1]}')
