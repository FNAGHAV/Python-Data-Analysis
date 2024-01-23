# Input file path and output file path 
file_path = "../Python-Challenge/PyPoll/Resources/election_data.csv"
text_path = "../Python-Challenge/PyPoll/Analysis/Analysis.txt"


# importing library
import csv


# Csv file reading and writing 
with open(file_path, 'r') as file:
    reader_file = csv.reader(file)
    Header = next(reader_file)
    with open(text_path, 'w') as Analysis:
        writer_file = csv.writer(Analysis)
        count = 0
        list_candidate = {}
        
        
        # for loop through the lines of the csv file
        for line in reader_file:
            ID = line[0]
            county = line[1]
            candidate = line[2]
            count += 1
            if candidate in list_candidate:
                list_candidate[candidate] += 1
            else:
                list_candidate[candidate] = 1
                
        
        # maximum vote counter
        max_vote = max(list_candidate.values())
        
        
        # winner identifier
        winner = [candidate for candidate, vote in list_candidate.items() if vote == max_vote]

        percentages = [(candidate, (vote / count) * 100, vote) for candidate, vote in list_candidate.items()]

        
        # Writing on the csv file for election results, total votes, candidates and their votes and percentage, and finally the winner.
        writer_file.writerows([
            ['Election result'],
            [],
            ["------------------"],
            [],
            [f"Total Votes: {count}"],
            [],
            ["------------------"],
            []
        ])
        for candidate, percentage, vote in percentages:
            writer_file.writerows([
                [f"{candidate}: {percentage:.3f}% ({vote})"],
                []
            ])
        writer_file.writerows([
            ["------------------"],
            []
        ])
        writer_file.writerows([
            [f"winner: {winner[0]}"],
            [],
            ["------------------"]
        ])

    # printing the output in terminal
    print(f"Election Results"
          f"\n\n---------------------"
          f"\n\nTotal Votes: {count}"
          f"\n\n---------------------")
    for candidate, percentage, vote in percentages:
        print(f"\n{candidate}: {percentage:.3f}% ({vote})")
    print()
    print(f"---------------------"
          f"\n\nWinner: {winner[0]}"
          f"\n\n---------------------")
