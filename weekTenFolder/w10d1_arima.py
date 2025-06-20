


# import pandas as pd
# import matplotlib.pyplot as plt
# from statsmodels.tsa.arima.model import ARIMA

# # Load and prepare data
# df = pd.read_csv('../weekFourFolder/selmerWeather.csv')
# df['DATE'] = pd.to_datetime(df['DATE'])
# df.set_index('DATE', inplace=True)

# # Set daily frequency and fill missing days
# df = df.asfreq('D')
# df['TMAX'] = pd.to_numeric(df['TMAX'], errors='coerce')
# df['TMAX'] = df['TMAX'].interpolate()  # fills missing data smoothly

# # Fit ARIMA model
# model = ARIMA(df['TMAX'], order=(1,1,1))
# model_fit = model.fit()

# print(model_fit.summary())

# # Forecast next 5 days
# forecast = model_fit.forecast(steps=5)

# # Plot
# plt.figure(figsize=(10,5))
# plt.plot(df['TMAX'], label='Historical TMAX')
# plt.plot(forecast.index, forecast, label='Forecast (next 5 days)', marker='o', linestyle='--')
# plt.title('Selmer, TN Daily Max Temperature Forecast')
# plt.xlabel('Date')
# plt.ylabel('Temperature (°F)')
# plt.legend()
# plt.grid(True)
# plt.show()


# plt.plot(df['TMAX'], label='Historical TMAX')
# plt.plot(forecast.index, forecast, label='Forecast')
# plt.xlim(df.index.min(), forecast.index.max())
# plt.title('Daily Max Temperature Forecast')
# plt.xlabel('Date')
# plt.ylabel('Temperature (°F)')
# plt.legend()
# plt.show()


import pandas as pd

# Simulated last 10 days of max temps
temps = [88, 85, 78, 86, 82, 80, 91, 85, 89, 83]

# Your “simple ARIMA-like” guess: average of last 3 days
def simple_forecast(data):
    return sum(data[-3:]) / 3

# Guess tomorrow's temp
guess = simple_forecast(temps)
print(f"My guess for tomorrow's temp: {guess:.2f} °F")

# Let's say tomorrow’s actual temp was 95 (just for example)
actual = 95
print(f"Actual temp tomorrow: {actual} °F")

# How close was the guess?
error = abs(guess - actual)
print(f"Prediction error: {error:.2f} °F")



# from statsmodels.tsa.arima.model import ARIMA
# import pandas as pd

# def arima_guess_game():
#     print("🎮 Welcome to 'Guess My Pattern'!")
#     print("Enter a series of numbers (between 1 and 10).")
#     print("Example: 2 3 4 5")

#     # Step 1: Get user input
#     user_input = input("Type at least 5 numbers, separated by spaces: ")
#     numbers = list(map(int, user_input.strip().split()))

#     # Step 2: Fit ARIMA
#     data = pd.Series(numbers)
#     model = ARIMA(data, order=(1,1,1))
#     model_fit = model.fit()

#     # Step 3: ARIMA makes a guess
#     forecast = model_fit.forecast()
#     guess = model_fit.forecast().iloc[0]

#     print(f"\n🤖 ARIMA guesses the next number is: {round(guess)}")

#     # Step 4: Ask if it was right
#     real = int(input("What was the real next number? "))
#     if round(guess) == real:
#         print("🎉 ARIMA got it right!")
#     else:
#         print("❌ Not quite. But nice try, ARIMA!")

# arima_guess_game()
