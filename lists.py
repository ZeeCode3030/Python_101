# LIST
# students = ['Hermoine', 'Harry', 'Rob']

#DICTIONARY 
'''students = {
    #Key : value, Hermoine is the index
    "Hermoine" : "Gryffindor", 
    "Harry" : 'Gryffindor',
    "Ron" : 'Gryffindor',
    "Draco" : 'Slytherin'
}

for student in students: # you can also do
# for i in range(len(students)):
    # if students[i].find("h"|"H") == True:    
    #     print(i + 1, students[i])
    if student.find("H") > -1 : #returns -1 on failure 
        print (student)
   
# to print the key and the value of the key/name 
    print (student,"is in house", students[student])

'''
# 3 DIMENSIONAL
students = [
    {'name':'Hermoine', 'house':'Gryffindor', 'patronus':'Otter'}, 
    {'name':'Harry', 'house':'Gryffindor', 'patronus':'Stag'}, 
    {'name':'Rob', 'house':'Gryffindor', 'patronus':'Jack'}, 
    {'name':'Draco', 'house':'Slytherin', 'patronus':None} 
]

for student in students:
    print (student[name], student[house], student[patronus] )


