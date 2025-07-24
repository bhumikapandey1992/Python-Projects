# Python Project – Simple Quiz Game

def run_quiz():
    score = 0
    print("1. What is the capital of France?")
    answer = input("a) Paris b)Rome c) Madrid\n")
    if answer.lower() == "a":
        score  +=1
    print("\n2. What does CPU stand for?")
    answer = input("a) Central Programming Unit b) Central processing unit\n")
    if answer.lower() == "b":
     score += 1
    print("\n3. What is the output of print(2+3)?")
    answer = input("a) 5 b) '2 + 3' c)23 \n")
    if answer.lower() == "a":
       score += 1
    print(f"\n✅ You got {score} out of 3 correct!")

def mainfunc():
   play_again = "yes"
   while play_again == "yes":
      run_quiz()
      play_again = input("Do you want to try again? (yes/no):").lower()

mainfunc()