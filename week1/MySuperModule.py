class ListKeeper:
    
    
    def show():
        #Key of dictionary entry acts as the name, value holds the items of the respective list
        return(dict0.keys())

    def add(name, list):
        #new dict entry of key and value gets created
        dict0[name] = list

    def delete(name):
        #removes entry with given name
        dict0.pop(name)

    def sort(name):
        #sorts list items ascending by value
        dict0[name].sort()
        return(dict0[name])

    def append(name,list):
        #appends new items to an existing list
        dict0[name].extend(list)




dict0 = {}

dict0["example"] = [1,2,3,4,5]