
# finished!!

print("second half action")
print("==================")

print()

half_time_score_away_team = int(input("Enter the away teams half-time score: "))
half_time_score_home_team = int(input("Enter the home teams half-time score: "))

print()

full_time_score_away_team = int(input("Enter the away teams full-time score: "))
full_time_score_home_team = int(input("Enter the home teams full-time score: "))

print()

total_goals = int((full_time_score_home_team + full_time_score_away_team) - (half_time_score_home_team + half_time_score_away_team))


print("The total number of goals scored after half-time is: ", total_goals )