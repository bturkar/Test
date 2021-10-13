"""1.Find grade of a student based on below requirement."""
marks=int(input('Enter Your Score : '))
if marks>0:
    if marks >= 35:
        if marks >= 80:
            print('Congratulation you Passed with grade : A+')
        elif 79 >= marks > 60:
            print('Your Grade is : A')
        elif 60 >= marks > 50:
            print('Your Grade is : B')
        elif 50 >= marks > 40:
            print('Your grade is : C')
        else:
            print('Your grade is : D')
    else:
        print('Failed, Better luck next time')
else:
    print('Invalid Input ')