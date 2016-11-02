import DecisionTree

def main():
    try:
        file = open(r'.\TestData\SoybeanTraining.csv')
    except(IOError):
        print("Cannot open this file. ")
        return
    Data = []
    try:
        for line in file:
            line = line.strip("\r\n")
            Data.append(line.split(','))
        Attributes = Data[0]
        Data.pop(0)
    finally:
        file.close()
    tree = DecisionTree.DecisionTree()
    TargetAttribute = "germination"
    tree.Generate(Data,Attributes,TargetAttribute)
    print("Tree generated. ")
    print("Predict Data:")
    print(Data[-1])
    print("Result:")
    print(tree.Predict(Data[-1]))


if __name__ == '__main__':
    main()
