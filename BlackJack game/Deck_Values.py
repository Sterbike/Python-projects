
import Values

def deck_value(person):
    a = []
    for i in range(len(person)):
        valuesofcards = int(Values.card_values[person[i]])
        a.append(valuesofcards)
    b = (sum(a))
    return (b)






