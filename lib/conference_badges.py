def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    return [f'Hello, my name is {name}.' for name in names]

def assign_rooms(names):
    rooms = range(1, 9)
    
    assignments = []
    for room in rooms:
        assignments.append(f'Hello, {names[room - 1]}! You\'ll be assigned to room {room}!')
    
    return assignments

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)


# def badge_maker(name):
#     return f'Hello, my name is {name}.'
# badge_maker("Guido van Rossum")

# def batch_badge_creator(names):
#     greet = []

#     for eachName in names:
#         greet.append(f"Hello, my name is {eachName}.")
#     return greet
# batch_badge_creator(['Guido', 'Edsger', 'Ada', "Grace"])

# def assign_rooms(names):
#     room_num = 1
#     assign_rooms = []

#     while room_num < len(names):
#         for eachName in names:
#             assign_rooms.append(f"Hello, {eachName}! You'll be assigned to room {room_num}!")
#             room_num += 1
#     return assign_rooms
# assign_rooms(['Guido', 'Edsger', 'Ada', 'Grace'])

# def printer(names):
#     return batch_badge_creator(names)
#     return assign_rooms(names)
# printer(["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"])


