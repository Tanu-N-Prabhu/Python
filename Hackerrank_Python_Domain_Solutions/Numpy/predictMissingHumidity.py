# necessary import libraries
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression

# Function: predictMissingHumidity
# Description: Predict missing humidity values using linear regression.
# Parameters:
#   - startDate: Start date of the data.
#   - endDate: End date of the data.
#   - knownTimestamps: List of timestamps with known humidity values.
#   - humidity: List of known humidity values corresponding to the knownTimestamps.
#   - timestamps: List of timestamps for which humidity needs to be predicted.
# Returns:
#   - numpy array: Predicted humidity values for the given timestamps.
def predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps):
    # Convert knownTimestamps to seconds since the epoch
    x = [int(abs((datetime.datetime.utcfromtimestamp(0) - 
                  datetime.datetime.strptime(item, "%Y-%m-%d %H:%M")).total_seconds())) 
         for item in knownTimestamps]
    
    # Known humidity values
    y = humidity

    # Create a linear regression model
    lm = LinearRegression()
    lm.fit(np.array(x).reshape(-1, 1), y)

    # Convert timestamps to seconds since the epoch for prediction
    z = [int(abs((datetime.datetime.utcfromtimestamp(0) - 
                  datetime.datetime.strptime(item, "%Y-%m-%d %H:%M")).total_seconds())) 
         for item in timestamps]
    
    # Predict humidity values for the given timestamps
    return lm.predict(np.array(z).reshape(-1, 1))



if __name__=="__main__":
    # dummy inputs
    startDate = '2013-01-01'
    endDate = '2013-01-01'
    knownTimestamps = ['2013-01-01 07:00', '2013-01-01 08:00', '2013-01-01 09:00', '2013-01-01 10:00',
                        '2013-01-01 11:00', '2013-01-01 12:00']
    humidity = [10.0, 11.1, 13.2, 14.8, 15.6, 16.7]
    timestamps= ['2013-01-01 13:00', '2013-01-01 14:00']

    # call the utility function
    answer = predictMissingHumidity(startDate, endDate, knownTimestamps, humidity, timestamps)
    print(answer)