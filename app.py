from mqtt import Connection


def App():
    print("app")
    con = Connection(sub_topic="CMD")
    con.loop()




if __name__ == "__main__":
    App()