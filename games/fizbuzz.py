#Game
#start form 1
#for multiples of 3 - fizz
#for multiples of 5 - buzz
#for multiples of 3 & 5 - fizzbuzz
num=1 # to track the numbers
player_count=int(input("Enter the number of players: ")) #total no of players
player_tag=list(range(1,player_count+1)) #names of the players
n=0 # to keep check of the player tag in the game
print("Start entering the answers :")
while(player_count>1):
    print("Player",player_tag[n]," :",end=" ")
    ans=input()
    expected=str(num)
    if(num%3==0 and num%5 ==0):
            # print('FizzBuzz')
             expected='fizzbuzz'
    elif(num%3==0):
            # print("Fizz")
             expected='fizz'
    elif(num%5==0):
            # print("Buzz")
             expected='buzz'
    if(ans!=expected):
                     player_count-=1
                     print("\t\twrong!, player",player_tag[n],"is out")
                     player_tag.remove(player_tag[n])
                     
    else:
            n = (n + 1) % player_count
    num+=1
   
print("\nWinner is player",player_tag[0])
