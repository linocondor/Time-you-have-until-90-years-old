print("How many time I have left If I live until 90 years old?")
age = input("What is your current age?  ")

age = int(age)

years_until_90 = 90
months_until_90 = years_until_90 * 12
weeks_until_90 = years_until_90 * 52
days_until_90 = years_until_90 * 365

current_age = age
current_month = age * 12
current_weeks_lived = age * 52
current_days_lived = age * 365

#Days, weeks, years reminder

year_remind = years_until_90 - current_age
month_remind = months_until_90 - current_month
weeks_remind = weeks_until_90 - current_weeks_lived
days_remind = days_until_90 - current_days_lived
print("------------------------------------------")
print(f"You have {days_remind} days, {weeks_remind} weeks, {month_remind} months, and {year_remind} years left.")



