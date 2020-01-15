sample_set = {'status': 1, 'data':
    {'users': [
        {'fstname': 'a', 'lstname': 'b', 'phone': '1234', 'dob': '12-02-1997'},
        {'fstname': 'q', 'lstname': 'z', 'phone': '5677', 'dob': '78900'},
        {'fstname': '', 'lstname': '', 'phone': '', 'dob': ''}
    ]
    }
              }
find = 'a'
data = 'not working'
# for s in sample_set['data']['users']:
#     if find in s['fstname'].keys():
#         data = s
for s in sample_set['data']['users']:
    if find is s['fstname']:
        print(s)
