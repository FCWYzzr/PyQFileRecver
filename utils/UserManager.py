import pickle as pkl
import os.path as path


class UserRecord:
    Dic = None

    def __init__(self):
        if path.exists("Records.map"):
            with open("Records.map", "rb") as f:
                self.Dic = pkl.load(f)
        else:
            master = input("Please input master's QQ")
            self.Dic = dict(master=master)
            self.Save()

    def Save(self):
        with open("Records.map", "wb") as f:
            pkl.dump(self.Dic, f)
        print("dict file saved")
