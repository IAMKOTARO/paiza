# n = int(input())
# queries = []
# pages = []
# for i in range(n):
#     query = input()
#     queries.append(query)
# for query in queries:
#     if query.startswith('go to'):
#         page_type = query.replace('go to ', '')
#         pages.append(page_type)
#         print(page_type)
#     elif query == 'use the back button':
#         print(pages.pop(-2))
#     else:
#         print('Invalid query')
#         exit(0)
n = int(input())

goto, back = 'go to ', 'use the back button'
history = []
current_pos = 0
for i in range(n):
    command = input()
    if goto in command:
        page = command[len(goto):]
        current_pos = 0
    elif back in command:
        current_pos -= 2
        page = history[current_pos]
    history.append(page)

for page in history:
    print(page)