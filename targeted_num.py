def target_number(numbers, target):
   seen={}
   for i,num_1 in enumerate(numbers):
      num_2=target-num_1
      if num_2 in seen:
            return (seen[num_2],i)
      seen[num_1]=i
   return None
print(target_number([10,15,3,7],17))