# allow pandas to be used in this program as pd
import pandas as pd

# value set for the while loop
run = True

# use pandas to read the file
# usecols selects what colums are to be accesed, any others will be ignored
df = pd.read_csv("tinder_google_play_reviews.csv", usecols= ["userName", "score", "at","content"])

# Allow all of the information to display even if it is long
# None can be replaced with a numeric value
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Set varibales to hold number of 1,2,3,4, and 5 star results
score1 = df[(df['score'] == 1)]
score2 = df[(df['score'] == 2)]
score3 = df[(df['score'] == 3)]
score4 = df[(df['score'] == 4)]
score5 = df[(df['score'] == 5)]

# Start a while loop for the user to select a display range for sample results
while run == True:

    num_results = input("How many sample results would you like to see (0-549,312): ")

    if int(num_results) > 549312:
        print("Pick a smaller number\n")
        run = True

    elif int(num_results) < 0:
        print("Pick a larger number\n")
        run = True

    else:
        run = False

# display results according to the perameters set in num_results
#   if too high of a range is selected it will only display the first 5 and the 5 before the picked number
print(f'\n{df.head(int(num_results))}\n')

# remove the null values to avoid errors later in the code
df.dropna(inplace = True)

# diplay the number of occurrence of each catagory
print(f'1 star: {len(score1)}')
print(f'2 star: {len(score2)*2}')
print(f'3 star: {len(score3)*3}')
print(f'4 star: {len(score4)*4}')
print(f'5 star: {len(score5)*5}')

# add up the total value of all the stars
avg = (len(score1)) + (len(score2)*2) + (len(score3)*3) + (len(score4)*4) + (len(score5)*5)

# create a variable to hold the total number of rows in the data
total = len(df)

# find and display the average number of stars
print(f'\nAvg rating: {round(avg / total)}\n')

review_view = input("\nWould you like to view the reviews for a specific star rating (Y/N): ")

while review_view.lower() == "y":
    review = input("\nWhich reviews would you like to see (1,2,3,4,5): ")

    if review == '1':
        print(score1.head(10))
    
    elif review == '2':
        print(score2.head(10))

    elif review == '3':
        print(score3.head(10))

    elif review == '4':
        print(score4.head(10))

    elif review == '5':
        print(score5.head(10))

    else:
        print("\ninvalid input")
    
    review_view = input("\nWould you like to view the reviews for another specific star rating (Y/N): ")

search = input("\nWould you like to check the users for a specific name (Y/N): ")

# start a while loop to have the user search through the usernames for certain occurrence of names/words
while search.lower() == 'y':
    find_name = input("What name would you like to look for: ")

    # check for occurrence of name/word picked by user
    name = df[(df['userName'].str.contains(find_name))]

    print(f'The number of occurrence of that name is: {len(name)}\n')

    display = input("Would you like to see the occurrence (Y/N): ")

    if display.lower() == "y":

        # diplay all of the rows that have the specificed name/word
        print(name)

    search = input("Would you like to check for another specific name (Y/N): ")

# This does not actually do anything, it just looks better
print("\nCLOSING PROGRAM...")