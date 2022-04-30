from statsmodels.sandbox.stats.runs import runstest_1samp 
from scipy.stats import chisquare


#LCG
print("Enter the count of random numbers required: ")
amount = int(input())

mod_lcg = 12356
lcg_seed = 46
multiplier = 25
incremental_val = 563
num=lcg_seed
lcg_list = []
for j in range(amount):
  new_num  = (multiplier*num + incremental_val)%mod_lcg
  lcg_list.append(new_num)
  num = new_num

print("-------------Linear Congruential Generator (LCG)-------------")
print("Output : ")
for item in lcg_list:
  print(item,end=', ')
print("\n-----------------------------------------------")
#end

#runs - test
print("Runs test : p value : ", runstest_1samp(lcg_list)[1])

#chisqaure - test
freq_lcg = {}
for i in range(mod_lcg):
  freq_lcg[i]=0

lcgF_list = []
for i in lcg_list:
  freq_lcg[i]=freq_lcg[i]+1

for key,value in freq_lcg.items():
  lcgF_list.append(value)
print("Chisquare test : p value : ",chisquare(lcgF_list)[1])


#LFG
l1 = 4
l2 = 8
lfg = [4,71,79,29,521,243,59,427,46,522,19,401]
lfg_list=[]
mod_lfg = 2536
for num in range(amount):
  new_num = (lfg[l1-1] + lfg[l2-1]) % mod_lfg
  lfg_list.append(new_num)
  for j in range(len(lfg)-1):
    lfg[j]=lfg[j+1]
  lfg[len(lfg)-1]=new_num
print("\n")
print("----------Lagged Fibonacci Generator (LFG) -----------")
print("Output: ")
for item in lfg_list:
  print(item,end=' , ')
print("\n-----------------------------------------------")
#end

#runs - test
print("Runs test : p value : ", runstest_1samp(lfg_list)[1])

#chisqaure - test
freq_lfg = {}
for i in range(mod_lfg):
  freq_lfg[i]=0

lfgF_list = []
for i in lfg_list:
  freq_lfg[i]=freq_lfg[i]+1

for key,value in freq_lfg.items():
  lfgF_list.append(value)

print("Chisquare test : p value : ",chisquare(lfgF_list)[1])
print("\n-----------------------------------------------")

