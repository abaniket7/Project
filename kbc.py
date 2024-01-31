questions = [ ["Who was the first man to walk on the moon?", "Neil Armstrong", "Buzz Aldrin", "Yuri Gagarin", "Alan Shepard", 1],
              ["Which scientist is famous for the theory of relativity?", " Isaac Newton", "Albert Einstein", "Galileo Galilei", "Marie Curie", 2],
              ["What is the world's largest ocean?", "Atlantic Ocean", " Indian Ocean", "Arctic Ocean", "Pacific Ocean", 4],
              ["Who wrote the play ""Romeo and Juliet""?", "William Shakespeare", "Arthur Miller", "Tennessee Williams", " Oscar Wilde", 1],
              ["Which country won the FIFA World Cup 2018?", "Germany", "France", "Brazil", "Italy", 2],
              ["Who is the current CEO of Apple Inc.?", "Tim Cook", "Jeff Bezos", "Elon Musk", "Mark Zuckerberg", 1],
              ["What is the chemical formula for water?", "CO2", "H2O", "O2", "NaCl", 2],
              ["Who painted the famous artwork ""Mona Lisa""?", "Michelangelo", "Leonardo da Vinci", " Salvador Dalí", "Vincent van", 2],
              ["In which country is the Taj Mahal located?", "India", "China", "Egypt", "Turkey", 1],
              ["What is the capital city of Brazil?", "Rio de Janeiro", "Brasília", "São Paulo", "Buenos Aires", 2],
              ["Which planet is known as the ""Red Planet"" ?", "Venus", "Mars", "Jupiter", "Saturn", 2],
              ["Who is the author of the famous novel ""To Kill a Mockingbird"" ?", " F. Scott Fitzgerald", "Harper Lee", "J.D. Salinger", "Mark Twain", 2],
              ["What is the chemical symbol for the element gold?", "Au", "Ag", "Fe", "Hg", 1],
              ["Which city is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 3],
              ["Who painted the famous artwork ""The Starry Night""?", " Claude Monet", "Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci", 3],
              ["Who is credited with inventing the telephone?", "Thomas Edison", "Nikola Tesla", "Guglielmo Marconi", "Alexander Graham Bell", 4] ]
levels = [ 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 7500000, "1 Crore", "7.5 Crore"]
i=0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]} :")
    print(question[0])
    print(f"1. {question[1]}                2. {question[2]}")
    print(f"3. {question[3]}                4. {question[4]}")
    reply = int(input("Enter the choice & for Quit press 0: "))
    if(reply == 0):
        money = levels[i-1]
        break
    elif(reply == question[-1]):
        print(f"Correct Answer, You have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif (i == 14):
            money = 7500000
        else :
            money = "7.5 Crore"
    else:
        print(f"Wrong Answer")
        break
print(f"Your final winning amount iss {money}")