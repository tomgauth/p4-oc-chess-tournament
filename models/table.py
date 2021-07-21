import tinydb


class Table(tinydb.table.Table):

    def test(self):
        print("this is a test")
    pass


# serialize
# can do the normal db stuff
