"""
sample `questions.txt` file:
1+1=2
2+2=4
8-4=4
task description:
- read from `questions.txt`
- for each question, print out the question and and wait for the user's answer
    for example, for the first question, print out: `1+1=`
- after the user answers all the questions, calculate 
her score and write it to the `result.txt` file
    the result should be in such format: `Your final score is n/m.`
    where n and m are the number of correct answers and the maximum score respectively
"""
# your code starts here:

questions = open('questions.txt', 'r')
each_questions = [line.strip() for line in questions.readlines()]

score = 0
total = len(each_questions)

for line in each_questions:
    q, a = line.split("=")

    ans = input(f"{q}=")

    if a == ans:
        score += 1
    
result = open("result.txt", "w")  # open result.txt
# write final score to result.txt
result.write(f"Your final score is {score}/{total}.")
result.close()


