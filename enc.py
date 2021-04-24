import json,struct
#songdescenc by zanga
print("songdescenc by zanga")
songdescfilename=input("songdesc: ")
musictrackfilename=input("musictrack: ")
gamever=int(input("game version: "))
songdesc=json.load(open(songdescfilename))
musictrack=json.load(open(musictrackfilename))
enc=open(songdesc["COMPONENTS"][0]["MapName"]+"_songdesc.main_legacy.tpl.ckd","wb")
#header
enc.write(struct.pack(">i",1)+struct.pack(">i",5541))
enc.write(bytes.fromhex("1B857BCE0000006C00000000000000000000000000000000000000000000000000000000000000018AC2B5C6000000F4"))
#components
enc.write(struct.pack(">i",len(songdesc["COMPONENTS"][0]["MapName"]))+songdesc["COMPONENTS"][0]["MapName"].encode())
enc.write(struct.pack(">Q",8675833939940)+struct.pack(">i",0)+struct.pack(">i",1))
enc.write(struct.pack(">Q",377957122048)+struct.pack(">Q",7))
enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["LocaleID"]))
enc.write(struct.pack(">Q",12884901888)+struct.pack(">Q",0))
enc.write(struct.pack(">Q",4294967295)+struct.pack(">Q",1))
enc.write(struct.pack(">i",len(songdesc["COMPONENTS"][0]["Artist"]))+songdesc["COMPONENTS"][0]["Artist"].encode())
enc.write(struct.pack(">i",len(songdesc["COMPONENTS"][0]["DancerName"]))+songdesc["COMPONENTS"][0]["DancerName"].encode())
enc.write(struct.pack(">i",len(songdesc["COMPONENTS"][0]["Title"]))+songdesc["COMPONENTS"][0]["Title"].encode())
enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["NumCoach"]))
enc.write(struct.pack(">I",4294967295))
try:
    enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["Difficulty"]))
except KeyError:
    enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["SweatDifficulty"]))
enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["backgroundType"]))
enc.write(struct.pack(">I",songdesc["COMPONENTS"][0]["LyricsType"]))
enc.write(struct.pack(">Q",5351931904)+struct.pack(">Q",8589934608)+struct.pack(">I",1866479568))
enc.write(struct.pack(">I",musictrack["COMPONENTS"][0]["trackData"]["structure"]["previewEntry"]))
enc.write(struct.pack(">Q",16)+struct.pack(">I",2971648438))
enc.write(struct.pack(">I",musictrack["COMPONENTS"][0]["trackData"]["structure"]["previewLoopStart"]))
enc.write(struct.pack(">I",musictrack["COMPONENTS"][0]["trackData"]["structure"]["previewLoopEnd"]))
#colors
if(gamever>=2017):
    enc.write(struct.pack(">Q",26384795863)+struct.pack(">Q",4490318429912815577)+struct.pack(">f",1))
enc.write(struct.pack(">Q",4575657222244381511))
for element in [songdesc["COMPONENTS"][0]["DefaultColors"]["lyrics"][3],
                songdesc["COMPONENTS"][0]["DefaultColors"]["lyrics"][2],
                songdesc["COMPONENTS"][0]["DefaultColors"]["lyrics"][1],
                songdesc["COMPONENTS"][0]["DefaultColors"]["lyrics"][0]]:
    enc.write(struct.pack(">f",element))
enc.write(struct.pack(">q",-7144666366274961408)+struct.pack(">Q",4575657222473777152))
enc.write(struct.pack(">Q",4575657224135952580)+struct.pack(">Q",4563788917862666642))
enc.write(struct.pack(">Q",4463332153962266624)+struct.pack(">q",-4752536605098931830))
enc.write(struct.pack(">Q",1057129091)+struct.pack(">Q",4575657225527385191))
enc.write(struct.pack(">Q",4544008398721034409)+struct.pack(">Q",4440725847002841088))
enc.write(struct.pack(">Q",0))
enc.close()