content = {'1': {'content': {'title': 'here we go'}},
           '2': {'content': {'title': 'sr software'}},
           '3': {'content': {'title': 'engineer here'}},
           '4': None, }


title = set()

for k1, v1 in content.iteritems():
    try:
        for word in v1['content']['title'].split():
            title.add(word)
    except Exception as e:
        print e, k1
        pass

for i in title:
    print i
