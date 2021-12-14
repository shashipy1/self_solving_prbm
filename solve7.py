def matchingWords(sentance1, sentance2):
    words1 = sentance1.split(" ")
    words2 = sentance2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1
    return score
if __name__ == '__main__':
    print(matchingWords("This is good", "Python is good"))
    sentences = ["python is good", "this is snake", "harry is good coder",
                 "Subscribe my youtube channel indain jharokha"]
    query = input("please enter the query string\n")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    # print(scores)
    sortedSentScore = [sentScore for sentScore in sorted(zip(scores, sentences), reverse= True) if sentScore[0] != 0]
    # print(sortedSentScore)

    print(f"{len(sortedSentScore)} RESULT FOUND!")
    for score, item in sortedSentScore:
        print(f"\"{item}\": with a score of {score}\n")