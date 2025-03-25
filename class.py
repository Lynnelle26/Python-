class Parent:
    parentAttr = 100
    #this inbuilt method will invoke by parent() constructor when an object is created
    def __init__(self):
        print("calling the parent constructor")

#
    def parentmethod(self):
        print("Calling the parent method")

    def __setattr__(self, attr):
        Parent.patrentAttr = attr                                                                                                                                                                                                                                                          
