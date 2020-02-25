for i in range (101):
    if i%2 == 0:
        print(i, end=' , ')



#slavar = {"Ua" : "Kiev", 'De' : "Berlin", "Ru" : "Moskva"}
#strani = ["Ua", "Polska", "Ru"]
#for i in strani:
#    if i in slavar:
#        print(slavar[i])


Capitals = dict()
Capitals['Russia'] = 'Moscow'
Capitals['Ukraine'] = 'Kiev'
Capitals['USA'] = 'Washington'
Countries = ['Russia', 'France', 'USA', 'Russia']
for country in Countries:
    if country in Capitals:
        print('The capital of ' + country + ' is ' + Capitals[country])



if 