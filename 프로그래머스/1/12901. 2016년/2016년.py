def solution(a, b):
    
    dayForMonth={1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    yoyeil={0:"FRI",1:"SAT",2:"SUN",3:"MON",4:"TUE",5:"WED",6:"THU"}
    daysTotal=sum([dayForMonth[i] for i in list(dayForMonth.keys())[:a-1]])+(b-1)
    
    return yoyeil[daysTotal%7]