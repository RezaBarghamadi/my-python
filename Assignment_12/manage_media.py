
class Media:      
    MEDIEA=[]
                                                             
    def __init__(self,i,t,n,d,s,u,du,c):

        self.id=id
        self.type=type
        self.name=n
        self.director=d
        self.imdb_score=s
        self.url=u 
        self.duration=du
        self.casts=c

    def showInfo(self):
        print("Id\tType\tName\tDirector\tScore\tUrl\tDuration\tCastes")
    for media in MEDIEA:
        print(media["id"],"\t" ,media["type"],"\t",media["name"],)


    def download(self):
        ...


MEDIEA=[]
def my_mediea():

    file=open("media.txt","r")

    for line in file:
        res=line.split(",")

        my_object=Media(res[0],res[1],res[2],res[3],res[4],res[5],res[6])

        MEDIEA.append(my_object)
        







