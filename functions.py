import pickle
import classes

fileName = 'userSubscriptionData.pkl'

def getUsers():
    userList = pickle.load(open(fileName, 'rb'))
    return userList

def clearStorage():
    open(fileName, 'w').close()
    pickle.dump([], open(fileName, 'ab'), pickle.HIGHEST_PROTOCOL)

def userInList(user, channelID):
    userList = getUsers()
    userInList = False;

    if (not userList == []):
        for compareUser in userList:
            print(user.userID + " " + channelID)
            print(compareUser.subbedChannels)
            if ((user.userID == compareUser.userID) and (channelID in compareUser.subbedChannels)):
                userInList = True;

    return userInList;

def addUser(userToAdd, channelID):
    userList2 = getUsers()
    boolean = False
    with open(fileName, 'wb') as output:
        clearStorage()

        for compareUser in userList2:
            if (userToAdd.userID == compareUser.userID):
                boolean = True

                if (channelID not in compareUser.subbedChannels):
                    compareUser.addChannel(channelID)
                    # print("adding channel to user")
                    print(compareUser.subbedChannels)


        if (not boolean):
            userList2 = userList2 + [userToAdd]
            print("user not in list. adding.")

        # if (not boolean):
        print("updating list")
        pickle.dump(userList2, output, pickle.HIGHEST_PROTOCOL)

def removeUser(userToRemove, channelID):
    userList = getUsers()

    with open(fileName, 'wb') as output:
        clearStorage()


        for index in range(len(userList)):
            if (userToRemove.userID == userList[index].userID):
                del userList[index]

        print('updating list')
        pickle.dump(userList, output, pickle.HIGHEST_PROTOCOL)
