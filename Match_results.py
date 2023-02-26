#Inpit:list of football team games with match result.
#A team is awarded 3 points for a win, 0 for a loss, and 1 for a draw.
#Output:summary table of results of all matches
#Rules for input:
#1.The first line contains an integer — the number of completed games.
#2.This is followed by n lines containing the results of the game in the following format:
#First Team;Scored by_first team;Second Team;Scored by_second team
#Rules for output:
#1.The order in which commands are output is arbitrary.
#2.Format of output: Team:Total_games Wins Draws Losses Total_points
print('Enter the match result following the instructions:')
n=int(input())
g={}
g2=[]
for i in range(n):
  s=input().split(';')
  g2+=[s]
for x in g2:
  g.setdefault(x[0], [0]*5)
  g.setdefault(x[2], [0]*5)
for t in g2:
  if int(t[1])>int(t[3]):
    gFirstList=g.get(t[0])
    gFirstList[1]+=1
    gFirstList[4]+=3
    gSecondList=g.get(t[2])
    gSecondList[3]+=1
    gFirstList[0]+=1
    gSecondList[0]+=1
  if int(t[1])<int(t[3]):
    gFirstList=g.get(t[0])
    gFirstList[3]+=1
    gSecondList=g.get(t[2])
    gSecondList[1]+=1
    gSecondList[4]+=3
    gFirstList[0]+=1
    gSecondList[0]+=1
  if int(t[1])==int(t[3]):
    gFirstList=g.get(t[0])
    gFirstList[2]+=1
    gSecondList=g.get(t[2])
    gSecondList[2]+=1
    gFirstList[0]+=1
    gSecondList[0]+=1
    gFirstList[4]+=1
    gSecondList[4]+=1
for k, v in g.items():
  print(k+':',sep='',end='')
  print(*v)