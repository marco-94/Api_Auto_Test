import random
from config.config import DATA_PATH


def createPhone():
    with open(DATA_PATH + '\phonelist.txt', 'w') as f:
        for k in range(100):
            prelist=["130", "131", "132", "133", "134", "135", "136", "137", "138", "139",
                     "147", "150", "151", "152", "153", "155", "156", "157", "158", "159",
                     "186", "187", "188", "189"]
            f.write(random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8)))
            f.write("\n")

if __name__ == '__main__':
    createPhone()

