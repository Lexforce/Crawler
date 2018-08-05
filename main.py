import urllib.request
import re



start_url = 'http://tedgreene.com'
visited = []
to_visit = []
to_visit.append(start_url)


while(len(to_visit) > 0):
    current_url = to_visit.pop()
    print("current_url = {}\n".format(current_url))
    with urllib.request.urlopen(current_url) as response:
        visited.append(current_url)
        content = response.read().decode('utf-8', 'ignore')

        #page = content.decode('UTF-8')
        #print(content.type)
        lines = content.split('\n')
        #print(len(lines))

        for line in lines:
            m = re.search('<a href="([^"]*)">', line)
            m2 = re.search('href="(\w*/\w*.pdf)"', line)
            if m:
                #print(m.group(1))
                #last_slash = current_url.rfind('/')
                print("matched group: " + m.group(1))
                new_url = current_url + '/' + m.group(1)
                if new_url not in visited:
                    print("new url: {}".format(new_url))
                    to_visit.append(new_url)
            if m2:
                print(start_url + '/' + m2.group(1))

print("\n\n***to_visit empty***\n")
