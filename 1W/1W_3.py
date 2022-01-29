score = [(100, 100), (95, 90), (55, 60), (75, 80), (70, 70)]

def get_avg(score):
    for i in range(len(score)):
        print(f"{i+1} 번, 평균 : {sum(score[i])/2}")

get_avg(score)
