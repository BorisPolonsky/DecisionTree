import math
class DecisionTree():
    def __init__(self):
        self.__structure = None
        self.__Attributes = None

    def __Entropy(self,Attributes,TargetAttribute,Data):
        Entropy = 0.0
        freq = {}
        try:
            i = Attributes.index(TargetAttribute)
        except ValueError:
            raise DecisionTreeException(0)
        for individual in Data:
            if individual[i] in freq:
                freq[individual[i]]+=1
            else:
                freq[individual[i]] = 1
        for key in freq:
            P = float(freq[key] / len(Data))
            if P != 0:
                Entropy+=-P * math.log2(P)
            else:
                Entropy+=0
        return Entropy

    def __PickAttribute(self,Attributes,TargetAttribute,Data):
        ret = None
        Min_Conditional_Entropy = None
        if self.__Entropy(Attributes,TargetAttribute,Data) == 0:
            return ret
        for i in range(len(Attributes)):
            if Attributes[i] == TargetAttribute or self.__Entropy(Attributes,Attributes[i],Data) == 0:
                continue
            Conditional_Entropy = 0
            Data_Sepration = {}
            for individual in Data:
                if individual[i] in Data_Sepration:
                    Data_Sepration[individual[i]]+=[individual]
                else:
                    Data_Sepration[individual[i]] = [individual]
            for key in Data_Sepration:
                Conditional_Entropy+=len(Data_Sepration[key]) / float(len(Data)) * self.__Entropy(Attributes,TargetAttribute,Data_Sepration[key])
            if Min_Conditional_Entropy == None:
                Min_Conditional_Entropy = Conditional_Entropy
                ret = Attributes[i]
            elif Conditional_Entropy < Min_Conditional_Entropy:
                Min_Conditional_Entropy = Conditional_Entropy
                ret = Attributes[i]
            return ret

    def Generate(self,Data,Attributes,TargetAttribute):
        try:
            i_target = Attributes.index(TargetAttribute)
        except ValueError:
            raise DecisionTreeException(0)
        if len(Data) == 0:
            return
        self.__structure = [None,{}]#structure has to be mutable object
        self.__Attributes = Attributes
        Open = [[self.__structure,Data]]
        while Open != []:
            front = Open.pop(0)
            Best_Attribute = self.__PickAttribute(Attributes,TargetAttribute,front[1])
            if Best_Attribute != None:
                front[0][0] = Best_Attribute
                i = Attributes.index(Best_Attribute)
                Open_Increment = []
                Data_Seperation = {}
                for individual in front[1]:
                    if individual[i] in Data_Seperation:
                        Data_Seperation[individual[i]].append(individual)
                    else:
                        Data_Seperation[individual[i]] = [individual]
                for key in Data_Seperation:
                    front[0][1][key] = [None,{}]
                    Open_Increment.append([front[0][1][key],Data_Seperation[key]])
                Open+=Open_Increment
            else:
                front[0][1] = []
                freq = {}
                for individual in front[1]:
                    if individual[i_target] in freq:
                        freq[individual[i_target]]+=1
                    else:
                        freq[individual[i_target]] = 1
                for key in freq:
                    front[0][1].append((key,float(freq[key] / len(front[1]))))

    def Predict(self,Data):
        iterator = self.__structure
        while iterator[0] != None:
            i = self.__Attributes.index(iterator[0])
            try:
                iterator = iterator[1][Data[i]]
            except KeyError:
                raise DecisionTreeException(1)
        return iterator[1]

    def __BeOfTheSameClass(self,Attributes,TargetAttrbute,Data):
        try:
            i = Attributes.index(TargetAttrbute)
        except(ValueError):
            raise DecisionTreeException(0)
        Class_0 = Data[0][i]
        for individual in Data:
            if individual[i] != Class_0:
                return False
        return True
    def __repr__():
        ...

class DecisionTreeException(Exception):
    Exception_Dictionary = {0:"Invalid Target Attribute",1:"Unpredictable Data"}
    def __init__(self,ErrorCode):
        self.__ErrorCode = ErrorCode
    def __repr__(self):
        return DecisionTreeException.Exception_Dictionary[self.__ErrorCode]
A = DecisionTree()