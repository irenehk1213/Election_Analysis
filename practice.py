counties_dict={"Arapahoe": "422829", "Denver:"463353", "Jefferson": "434343" }
message_to_candidate=(
    f"You received {candidate_votes:,} number of votes."
    f"The total number of votes in the election was {total_votes:,}"
    f"You received {candidate_votes/total_votes*100: .2f}% of the total votes"
)