#Class List Manager Group8
#MIS 211 bouns assignment

names=["Sara","Noura","Lama","Reem","Amal","Lama"]

#=====Each student adds her function BELOW this line======

#writen by: Jude Almasoud (task 1)
def count_names(names):
   return len(names)

#written by: Reema Albiaybe (task 6)
def to_upper(names):
   upper_names = []
   for name in names:
      upper_names.append(name.upper())
   return upper_names
   









#===== Each student adds her function ABOVE this line=====

def main():
  print("Welcome to the Class List Manager!")
  print("Class List:", names)

  print("Number of names:",count_names(names))
  print("Uppercase names:",to_upper(names))








main()
