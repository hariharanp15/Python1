votes = {
    "hari": 0,
    "siva": 0,
    "raja": 0
}

while True:
    print("Vote for hari / siva / raja (or type 'exit')")
    choice = input("Enter vote: ")

    if choice == "exit":
        break

    if choice in votes:
        votes[choice] += 1
    else:
        print("Invalid candidate")

winner = max(votes, key=votes.get)
print("Winner:", winner)