
# Simple EVM Voting Machine in Python

candidates = {
    "1": {"name": "Candidate A", "votes": 0},
    "2": {"name": "Candidate B", "votes": 0},
    "3": {"name": "Candidate C", "votes": 0}
}

total_voters = int(input("Enter total number of voters: "))

for voter in range(total_voters):
    print("\n===== EVM VOTING MACHINE =====")

    for key, candidate in candidates.items():
        print(f"{key}. {candidate['name']}")

    vote = input("Enter your vote (1/2/3): ")

    if vote in candidates:
        candidates[vote]["votes"] += 1
        print("Your vote has been recorded!")
    else:
        print("Invalid vote! Your vote was not recorded.")

print("\n===== ELECTION RESULTS =====")

for candidate in candidates.values():
    print(f"{candidate['name']}: {candidate['votes']} votes")

max_votes = max(c["votes"] for c in candidates.values())

winners = [
    c["name"] for c in candidates.values()
    if c["votes"] == max_votes
]

if len(winners) == 1:
    print("\nWinner:", winners[0])
else:
    print("\nElection tied between:", ", ".join(winners))
