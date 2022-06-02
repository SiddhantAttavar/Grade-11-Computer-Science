# Print the following patterns:
# i.
# # # # #
# # # # 
# # # 
# # 
# 
# ii.
# 8
# 8 6
# 8 6 4
# 8 6 4 2

# Pattern 1
for i in range(4, 0, -1):
    print('# ' * i)

# Pattern 2
for i in range(4):
    print(*range(8, 8 - 2 * i - 1, -2))
