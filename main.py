from sets import Set

persian = "\n".join(list(Set(open('persian').read().split('\n'))))
p_file = open('persian', 'w')
p_file.write(persian)