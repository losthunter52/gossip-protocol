#---------------------------------------------------------------------------
# Database Class
#---------------------------------------------------------------------------

class Database:
    # init method
    def __init__(self):
        # initializes the database struct
        self.list = []

    # addJson method
    def addJson(self, json):
        # add a json to the database
        self.list.append(json)

    #get method
    def getJson(self):
        #return the json list
        return self.list

    # isNews method
    def isNews(self, json):
        # checks if the gossip is news
        response = "Yes"
        for index in self.list:
            if json == index:
                response = "No"
        return response

    # printData method
    def printData(self):
        # print the database content
        for data in self.list:
            print(data)