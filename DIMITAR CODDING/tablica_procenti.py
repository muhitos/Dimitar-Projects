import matplotlib.pylab as p

percent = [35, 45, 28, 10, 10]
languges = ['Python', 'Java', 'C++', 'Go', 'JavaScript']
p.pie(percent, labels=languges)
p.show()