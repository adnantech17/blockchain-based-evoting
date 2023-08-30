from phe import paillier
from votingSystem import VotingSystem

votes = []


def main_menu():
    print("Voting System Menu")
    print("1. Vote for Candidate 1")
    print("2. Vote for Candidate 2")
    print("3. Vote for Candidate 3")
    print("4. Vote for Candidate 4")
    print("5. Vote for Candidate 5")
    print("6. End Voting")
    choice = input("Enter your choice: ")
    return choice


def main():
    votingSystem = VotingSystem()
    votingSystem.loadAndSavePublicKey()

    while True:
        choice = main_menu()

        if choice == "1":
            vote = [1, 0, 0, 0, 0]
            encrypted_vote = votingSystem.encryptVote(vote)
            print("Vote for Candidate 1 recorded.")
        elif choice == "2":
            vote = [0, 1, 0, 0, 0]
            encrypted_vote = votingSystem.encryptVote(vote)
            print("Vote for Candidate 2 recorded.")
        elif choice == "3":
            vote = [0, 0, 1, 0, 0]
            encrypted_vote = votingSystem.encryptVote(vote)
            print("Vote for Candidate 3 recorded.")
        elif choice == "4":
            vote = [0, 0, 0, 1, 0]
            encrypted_vote = votingSystem.encryptVote(vote)
            print("Vote for Candidate 4 recorded.")
        elif choice == "5":
            vote = [0, 0, 0, 0, 1]
            encrypted_vote = votingSystem.encryptVote(vote)
            print("Vote for Candidate 5 recorded.")
        elif choice == "6":
            print("Voting has ended.\n\n")
            print(".........Vote Count Phase begun.........\n\n\n")
            countedVotes = votingSystem.voteCount(votes)
            print(".........Vote Count Phase ended.........\n\n\n")
            print("Need keys from at least two share holders to view the result..")

            key1 = input('Input First key: ')
            key2 = input('Input Second key: ')
            votingSystem.combineKey([key1, key2])

            print(votingSystem.decryptVote(countedVotes))
            break
        else:
            print("Invalid choice. Please select a valid option.")

        votes.append(encrypted_vote)


if __name__ == "__main__":
    main()
