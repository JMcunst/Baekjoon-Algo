def find_all_hobbyists(hobby, hobbies):
    list_hobbyists = []
    print(len(hobbies))

    for dict in hobbies.items():
        if hobby in dict[1]:
            list_hobbyists.append(dict[0])

    print(list_hobbyists)
    
    
    return [] 

hobbies = { 
    "Steve": ['Fashion', 'Piano', 'Reading'],
    "Patty": ['Drama', 'Magic', 'Pets'],
    "Chad": ['Puzzles', 'Pets', 'Yoga']
}
    

find_all_hobbyists('Yoga', hobbies)

