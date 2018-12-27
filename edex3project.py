
days = [0,'MONDAY', 'TUESDAY','WEDNESDAY', 'THURSDAY' ,'FRIDAY' ,'SATURDAY', 'SUNDAY']

index=int(input("enter number 1 of 7: "))
if (index <= 0): {
        print("invalid number")
        }
if(index > 7):{
        print("invalid number")
}
else:{
        print(days[index])
}


