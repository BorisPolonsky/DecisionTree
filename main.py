from decision_tree.decision_tree import DecisionTree
from random import choice


def main():
    data = []
    try:
        with open(r'.\TestData\SoybeanTraining.csv', "r") as f:
            for line in f:
                line = line.strip("\r\n")
                data.append(line.split(','))
            attributes = data[0]
            data.pop(0)
    except FileNotFoundError as e:
        print(e)
    else:
        tree = DecisionTree()
        target_attribute = "germination"
        tree.generate(data, attributes, target_attribute)
        print("Tree generated. ")
        sample = choice(data)
        print("predict data:")
        print(sample)
        print("Result:")
        print(tree.predict_prob(sample))

if __name__ == '__main__':
    main()
