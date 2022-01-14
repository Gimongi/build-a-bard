class Feature:
    title = ""
    description = ""


    # Will perform json lookup of feature and set description to it
    def __init__(self, title):
        # may need to lookup title as well. in case it is like darkvision_60 and in json we store a title: Darkvision
        self.title = title
        pass

    def __init__(self, title, description):
        pass

    def featureLookup(featName):
        pass