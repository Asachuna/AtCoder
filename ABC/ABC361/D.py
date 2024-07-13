import sys
sys.setrecursionlimit(100000)
import queue

N = int(input())
S = input()
T = input()

S += ".."
T += ".."

dp = {}

global found
found = False

q= queue.Queue()

def getSteps(state, steps):
    if state in dp:
      return dp[state]
    
    else:
      dp[state] = steps

    dot1Index = state.index(".")
    dot2Index = dot1Index + 1
    
    for i in range(len(S)-1):
      s1 = state[i]
      s2 = state[i+1]
      if (s1 != "." and s2 != "."):
        newState = list(state)
        newState[dot1Index] = s1
        newState[dot2Index] = s2
        newState[i] = "."
        newState[i+1] = "."
        newState = "".join(newState)
        
        q.put([newState, steps+1])
        
q.put([T, 0])

while not q.empty():
  newState, steps = q.get(False)
  getSteps(newState, steps)
  

result = getSteps(S, float("inf"))
if result == None:
  print(-1)
else:
  print(result)