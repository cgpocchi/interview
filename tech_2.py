from functools import reduce

def intersect(list1, list2):
  res = set([])
  s1 = set(list1)
  for elt in list2:
    if elt in s1:
      res.add(elt)
  return res

# print(intersect([1,2,2,3,5], [2,5,0])) # [2,5]
# print(intersect([], [1,2,3])) # return []
# print(intersect([1,2,4], [])) # return []
# print(intersect([-1,-1,-2,-3], [1,1,2,3])) # return []

def intersect3(list1, list2, list3):
  return intersect(list3, intersect(list1, list2))

# print(intersect3([1,2], [3,4,5], [6,7])) # ret []
# print(intersect3([1,2,2,3,5], [6,3,5], [6,7])) # return []
# print(intersect3([1,4,4], [1,4,5], [1,4,6])) #return [1,4]

#time - O(sum (1->m-1) n_i + n_(i+1))
#space -O(sum (1->m-1) n_i + min(n_i, n_i+1))
def intersectn(lists):
  return reduce(intersect, lists)

# print(intersectn([[1,4,4], [1,4,5], [1,4,6], [1,5,7]]))
# print(intersectn([[], [1,2,3]]))
# print(intersectn([[1,2,3]]))

def intersect_2_files(file1, file2):
  res = set([])
  with open(file1, 'r') as name1:
    init_set = set(name1.readlines())
  
  with open(file2, 'r') as name2:
    for line in name2:
      if line in init_set:
        res.add(line)
  
  return res

def intersect_n_files(files):
  return reduce(intersect_2_files, files)

print(intersect_n_files(['tets1.txt', 'test2.txt']))

# def intersect_files(files):
#   init_name = files[0]
#   init_set = set([])
#   with open(init_name, 'r') as iname:
#     for line in iname:
#       init_set.add(line)
  
#   for name in files[1:]:
#     with open(name, 'r') as fname:

