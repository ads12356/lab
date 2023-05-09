def smith_waterman(seq1, seq2, gap_penalty=-2, match_score=1, mismatch_penalty=-1):
    m = len(seq1)
    n = len(seq2)

    matrix = [[0] * (n+1) for i in range(m+1)]
    max_score = 0
    max_pos = None
   
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if seq1[i - 1] == seq2[j - 1]:
                match = match_score
            else:
                match = mismatch_penalty
            diag_score = matrix[i - 1][j - 1] + match
            up_score = matrix[i - 1][j] + gap_penalty
            left_score = matrix[i][j - 1] + gap_penalty
            score = max(0, diag_score, up_score, left_score)
            matrix[i][j] = score
            if score > max_score:
                max_score = score
                max_pos = (i, j)
   
    align1 = ""
    align2 = ""
    i, j = max_pos
    while i > 0 and j > 0 and matrix[i][j] > 0:
        score = matrix[i][j]
        diag_score = matrix[i - 1][j - 1]
        up_score = matrix[i - 1][j]
        left_score = matrix[i][j - 1]
        if score == diag_score + match_score or seq1[i - 1] == seq2[j - 1]:
            align1 = seq1[i - 1] + align1
            align2 = seq2[j - 1] + align2
            i -= 1
            j -= 1
        elif score == up_score + gap_penalty:
            align1 = seq1[i - 1] + align1
            align2 = "-" + align2
            i -= 1
        else:
            align1 = "-" + align1
            align2 = seq2[j - 1] + align2
            j -= 1
    return max_score, align1, align2


seq1 = "ATGCA"
seq2 = "AGCA"
score, align1, align2 = smith_waterman(seq1, seq2)
print("Alignment score:", score)
print(align1)
print(align2)