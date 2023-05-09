#sequence Alignment
S1 = 'ATGCA'
S2 = 'AGCA'
match_score = 1
mismatch_score = -1
gap_score = -2
# Initialize the number of matches, mismatches, and gaps to 0
matches = 0
mismatches = 0
gaps = 0
for i in range(0,len(S1)):
    if S1[i] != S2[i]:
        S2 = S2[:i] + '-' +S2[i:]
for i in range(len(S1)):
    if S1[i] == S2[i]:
        matches += 1
    elif S1[i] == '-' or S2[i] == '-':
        gaps += 1
    else:
        mismatches += 1
final_score   = matches*match_score + mismatches*mismatch_score + gaps*gap_score
print("Matches:", matches)
print("Mismatches:", mismatches)
print("Gaps:", gaps)
print("Final Score:",final_score)