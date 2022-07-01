"""
Problem Statement:-
You are given few sentences as a list (Python list of sentences). Take a query string as an input from the user. You have to pull out the sentences matching this query inputted by the user in decreasing order of relevance after converting every word in the query and the sentence to lowercase. Most relevant sentence is the one with the maximum number of matching words with the query.

Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

Input:
Please input your query string

“Python is”

Output:
2 results found:

1) python is not snake
2) python is good

"""
#  FOR UNDERSTANDING THERE ISS A ADDITION OF SCORES WITH SENTENCES

def mathchingWords(sentence1,sentences2):
    words1 = sentence1.strip().split(" ")
    words2 = sentences2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            #print(f" {word1} ---> {word2}")
            if word1.lower() == word2.lower() :
                score += 1
    return score



if __name__ == "__main__":
    #mathchingWords("python is good","this is snake")
    sentences = ["python is good","python is not snake"]

    print("You can search for this sentence according by their words occuring in priority order\n")
    print("SENTENCES ARE:",sentences,"\n")
    query = input("Please Input Query String\n")
    scores = [mathchingWords(query,sentence) for sentence in sentences]
    #print(scores)

    sortedSentScore = [sentScore for sentScore in sorted(
        zip(scores, sentences),reverse=True ) if sentScore[0] != 0]
    #print(sortedSentScore)

    print(f"{len(sortedSentScore)} result found:-\n")
    for score,item in sortedSentScore:
        print(f"{item}")
