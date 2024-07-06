from datetime import datetime , timedelta

def display_current_datetime():   
    current_date = datetime.now()
    print(f"Current date and time: {current_date}, %Y-%m-%d %H:%M:%S")

display_current_datetime()


def calculate_future_date(YYYY, MM, DD):
       current_date = datetime.now()
       Delt  = timedelta(days= number_of_days)
       future_date = current_date + Delt
       formatted_future_date = future_date.strftime("%Y-%m-%d")
       print(f"Future date after days: {formatted_future_date}")
       
number_of_days = int(input("Enter the number of days to add to the current date:"))


# Display the current date and time
display_current_datetime()

# Calculate and display the future date
calculate_future_date(2024, 6, 12)

result = calculate_future_date
print(result)

