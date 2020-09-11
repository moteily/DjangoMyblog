import numpy as np
import pandas as pd


if __name__ == '__main__':
    data = [["2017-10-18", 11.53, 11.69, 11.70, 11.51, 871365.0, 1],

            ["2017-10-19", 11.64, 11.63, 11.72, 11.57, 722764.0, 2],

            ["2017-10-20", 11.59, 11.48, 11.59, 11.41, 461808.0, 3],

            ["2017-10-23", 11.39, 11.19, 11.40, 11.15, 1074465.0, 4]]

    data2 = [[11.53, 11.69, 11.70, 11.51, 871365.0, 2],

             [11.64, 11.63, 11.72, 11.57, 722764.0, 3],

             [11.59, 11.48, 11.59, 11.41, 461808.0, 44],

             [11.39, 11.19, 11.40, 11.15, 1074465.0, 4]]

    series = pd.Series(data, index=['a', 'b', 'c', 'd'])
    dataframe = pd.DataFrame(data2, index=["2017-10-18", "2017-10-19", "2017-10-20", "2017-10-23"],
                             columns=["open", "close", "high", "low", "volume", "code"])
    dataframe2 = pd.Series(data)
    arr1 = series.as_matrix()
    arr2 = dataframe.as_matrix()
    arr3 = np.array(dataframe)
    arr4 = np.array(dataframe2)
    print(series)
    print(dataframe)
    print(dataframe.iat[1, 1])
    print(arr1)
    print(arr2)

    print(arr4)
    print(dataframe.iloc[0:2,[1,3,5,4]])
    print(dataframe.iloc[1,:])
    print(arr3)
    print(list(dataframe))
    print(list(arr3))
    print(len(list(arr3)))
    print(len(arr3))
    print(np.array(list(arr3)))
