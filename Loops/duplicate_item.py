items=["apple","banana","mango","apple"]

unique_ele=set()

for item in items:
  if item in unique_ele:
    print("Duplicate exited:")
    break
  else:
    unique_ele.add(item)