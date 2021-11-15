# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('B2.json') as f:



        data = json.load(f)
        with open('grades.json') as f:

         data2 = json.load(f)
         question = data2["results"]
         my_question = data["B22"]
       #  for my_question_data in my_question:
        #     print(my_question_data)
        # print("my code ="+str(type(my_question_data)))
         #printing all elevator content
        # print(my_question_data["_elevators"])
        # elvator_data = my_question["_elevators"] //this is not valid
         #print(type(my_question))
         #all the values of my_question are keys
         for key in my_question :
           #  print(key)
       # print(type(key))
        #print("iam not in for loop")
          elevaor_field = key["_elevators"]
       # print(type(elevaor_field))

        # for elem_data in elvator_data :
           #  print(elem_data)
         #now its list
        # print(data2["results"])
        # print("data2 type = "+str(type(data2["results"])))
        # print(data2['results'][2])
         #i cant do that do that becouse i only have 1 object and its building

         #print("Data1 type = "+str(type(data['B22'])))
        # print(data2['B'])
        # for question_data in question:
       #      print(question_data)
      #  print(type(question_data))
        #now i can use data as normal dict

        #for B in data['B22']:
       # for json_dict in data['B22']:
       #  for key, value in json_dict.iteritems():
          #  print("key: {0} | value: {1}".format(key, value))
       # for (k, v) in data.items():
        # print("Key: " + k)
         #print("Value: " + str(v))
        #str1
        #tr2
        #now we iterating as list
        #print(data.keys())
        #print(data.values())
       # print('before loop')
        #python doesnt have array
        elevaor_field = []
        #for key in data['B22']['_elevators']:
            #elevaor_field.append(key)
        #print(str(type(data['B22']['_elevators'])))
        #iterating over list data['b22'] with keys that are dictionary
        k = 0
        ans = ""
        #data['B22'] is list
        #the elements in the list are dicts
      #  "_minFloor": -2,
       # "_maxFloor": 10,
        #"_elevators": [
        #print(data['B22'][0][0])
        #print(dir(data['B22']))
      #  print(data['B22']["_minFloor"])
        dima = data['B22']
        print(dima[0]["_minFloor"])
       # print(dima[0]["_elevators"])
        ele = dima[0]["_elevators"]
        print(type(ele))
        #iterating over object that has dicts
        #first it is {first elevator} and second {second elevator}
        #iterating of objects
        #kaasher it magia le object eshlo dict
        elem_in_ele = []
        #nitan laruz al maftehot
        for it in ele:
         for key in it.keys():
            print(key)

        print(type(it))

        for key in data['B22']:
            #print("first elements"+str(data['B22']))
            _minFloor = key["_minFloor"]
            _maxFloor = key["_maxFloor"]
           # print((type(data['B22'])))
        #    print(type(key))
            #print(_minFloor)
           # print(_maxFloor)
            elevaor_field = key["_elevators"]
          #  print(elevaor_field)
           # print(elevaor_field)

            #print(type(key.keys()))
           # if key  == "_elvators":
          #      ans = key

       # print(ans)
            #for second_key in key.keys():
             #   print(second_key)
              #  if second_key == "_elevators"


        #print('elevator fiels are'+str(elevaor_field))
        for key in data['B22']:
       #    print(type(data['B22']))
         #  print(type(key))

           my_iter = iter(data['B22'])
           #print('the key type is '+str(type(key)))
          # print('my iterator type is ='+str(my_iter))
           #print("key type is is = "+str(type(data['B22'])))
          # print("all methods are ="+str(dir(key)))
          # if data['B22'][key] ==("_minFloor"):
              # print('iam at first if' )
           #print("*"+str(next(my_iter)))
           if my_iter == "_minFloor":
            str1 = key
          #  print(str1)
           # print('iam at if statement')
          #  print('key type is ='+str(type(key)))
          #  print(type(my_iter))
            #now i have iterator
            #lets see all the methods
            #print(dir(data['B22']))
            # iterate through it using next()

            # Output: 4
            #if my_iter.__eq__('_minFloor') :
            #     print('iam inside if')

           # print("-->"+str(next(my_iter)))

            #we can put if statemnts and take the data
            #we iterating on list now
            #b22 key other are value
            #k = 0
            #print(key[0:])
            #print(data['B22'])
           # print(key["_minFloor"])
            #print(type(key["_minFloor"]))
           # k = k+1
           # print(type(key))

        #for key in data['B22']:
            #print(key)

         #   print(B)
          #  print(B['_minFloor'])


    #print_hi('PyCharm')

   # x = 5
    #print(x)
    #my_list= [1 ,"apples",'2',1.2333]
    #print(my_list)
    #x = 5**3
    #print(x)
    #for i in range(1,len(my_list)):
    #    print(my_list[i])



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
