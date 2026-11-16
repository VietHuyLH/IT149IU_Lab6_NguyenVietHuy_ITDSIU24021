# Student: Nguyễn Viết Huy
# Student ID: ITDSIU24021
# Class/Group: IT149IU – Group 01
# Course: IT149IU - Fundamentals of Programming (Python)
# Lab 6 - Dictionaries and Sets
# AI assistance: ChatGPT was used to help draft/check solutions; review and understand before submission.

chess = {'Nam', 'Phuc', 'Hoa', 'Em', 'Oanh', 'Chi', 'Giang'}
robotics = {'Nam', 'Phuc', 'Quyen', 'Minh', 'Em', 'Lan', 'Chi'}
music = {'Nam', 'Khang', 'Phuc', 'Quyen', 'Hoa', 'Binh', 'Lan'}

# Task 1: set operations on club membership
in_all = chess & robotics & music
only_chess = chess - robotics - music
in_exactly_two = ((chess & robotics) | (chess & music) | (robotics & music)) - in_all
in_at_least_one = chess | robotics | music
robotics_xor_music = robotics ^ music

print("Chess members:", sorted(chess))
print("Robotics members:", sorted(robotics))
print("Music members:", sorted(music))
print("In all three clubs:", sorted(in_all))
print("Only chess:", sorted(only_chess))
print("In exactly two clubs:", sorted(in_exactly_two))
print("In at least one club:", sorted(in_at_least_one))
print("Robotics XOR music:", sorted(robotics_xor_music))

# Basic consistency checks
assert in_all <= chess and in_all <= robotics and in_all <= music
assert only_chess.isdisjoint(robotics | music)
assert in_exactly_two.isdisjoint(in_all)
assert in_at_least_one == chess | robotics | music
assert robotics_xor_music == (robotics | music) - (robotics & music)
print("Task 1 checks: PASS")
