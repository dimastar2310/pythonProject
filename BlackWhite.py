
#def blackOrWhite(l,indexI,indexJ):
def check_black(indexI, indexJ,l1):
    for k in l1:
        for key, value in k.items():
            for key2 in value.keys():
                if key == indexI and key2 == indexJ:
                    if value[indexJ]==1:
                      print("white cell")
                    else:
                        print("black cell")



def main():


    l1 = [{8: {'a': 1}}, {8: {'b': 0}}, {8: {'c': 1}}, {8: {'d': 0}}, {8: {'e': 1}}, {8: {'f': 0}}, {8: {'g': 1}},
          {8: {'h': 0}},
          {7: {'a': 1}}, {7: {'b': 0}}, {7: {'c': 1}}, {7: {'d': 0}}, {7: {'e': 1}}, {7: {'f': 0}}, {7: {'g': 1}},
          {7: {'h': 0}},
          {6: {'a': 1}}, {6: {'b': 0}}, {6: {'c': 1}}, {6: {'d': 0}}, {6: {'e': 1}}, {6: {'f': 0}}, {6: {'g': 1}},
          {6: {'h': 0}},

          {5: {'a': 1}}, {5: {'b': 0}}, {5: {'c': 1}}, {5: {'d': 0}}, {5: {'e': 1}}, {5: {'f': 0}}, {5: {'g': 1}},
          {5: {'h': 0}},

          {4: {'a': 1}}, {4: {'b': 0}}, {4: {'c': 1}}, {4: {'d': 0}}, {4: {'e': 1}}, {4: {'f': 0}}, {4: {'g': 1}},
          {4: {'h': 0}},

          {3: {'a': 1}}, {3: {'b': 0}}, {3: {'c': 1}}, {3: {'d': 0}}, {3: {'e': 1}}, {3: {'f': 0}}, {3: {'g': 1}},
          {3: {'h': 0}},

          {2: {'a': 1}}, {2: {'b': 0}}, {2: {'c': 1}}, {2: {'d': 0}}, {2: {'e': 1}}, {2: {'f': 0}}, {2: {'g': 1}},
          {2: {'h': 0}},

          {1: {'a': 1}}, {1: {'b': 0}}, {1: {'c': 1}}, {1: {'d': 0}}, {1: {'e': 1}}, {1: {'f': 0}}, {1: {'g': 1}},
          {1: {'h': 0}}
          ]
    indexI = input("Enter index  i number between 1 to 8:")
    indexJ = (input("enter chars between a to h:"))
    indexI = int(indexI)

    check_black(indexI, indexJ,l1);


if __name__ == "__main__":
    main()








