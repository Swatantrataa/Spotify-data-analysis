
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
df2= pd.read_csv("C:\\Users\\swata\\Desktop\\spotify2023.csv")
print(df2)

#spotify2023.csv contains a comprehensive list of the most famous songs as listed on Spotify.
#The dataset includes information such as track name, artist(s)name,release date,Spotify playlists 
#and charts , streaming statistics,Apple Music presence , Deezer presence,Shazam charts,and various audio features.

df3=df2[["track_name","artist(s)_name","streams"]]

print("Trending #1 on spotify")
print("=========================================================================")
print(df3.head(1))
print(" ")

#Spotify creates various playlists based on trends,popularity ,genre and listeners preferences. Here are few playlists
# and charts in Spotify
 
#there are songs which are included in multiple charts. SONGS THAT APPEAR IN MAXIMUM NO. of SPOTIFY CHARTS
print("SPOTIFY GLOBAL TOP50 CHARTS")
print("============================================================================")
print(df2[["track_name","artist(s)_name","in_spotify_charts",]].head(50).sort_values("in_spotify_charts",ascending=False))
print(" ")

print("100 MOST STREAMED SONGS ON SPOTIFY ")
print(69*"=")
print(df3.head(100).sort_values("streams",ascending=False))
print(" ")

# WHAT ARE THE VARIOUS FEATURES OUR DATASET CONTAINS? 
print("VARIOUS FEATURES OF FEW MOST POPULAR SONGS")
for i,j in df2.head(10).iterrows():

    print("============================================================")
    print("Song NO",i)
    print(i,j)
    
print(" ")
print("Spotify's DANCE JAM PLAYLIST")
print("><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><")
dancedf=df2[["track_name","artist(s)_name","danceability_%","streams"]]
print(dancedf.sort_values("danceability_%",ascending=False).head(200))
print(" ")

print("Spotify's ACOUSTIC PLAYLISTS")
print(40*"-o-")
print(df2[["track_name","artist(s)_name","acousticness_%"]].sort_values("acousticness_%",ascending=False).head(100))
print(" ")

print("BEST CONCERT SONGS PLAYLISTS")
print(35*"--*--")
print(df2[["track_name","artist(s)_name","liveness_%","streams"]].sort_values("liveness_%",ascending=False).head(150))
print(" ")

print("Songs released on 2023")
print(30*"=")
print(df2.loc[df2["released_year"]==2023])
print(" ")
 

print("ABOUT DF2")


print(df2.info())
print(" ")

print("Total no. of elements present in df2 (spotify2023.csv)")
print(df2.size)
print(" ")
print("total no. of rows and columns")
print(df2.shape)



print("SONGS INCLUDED IN 100+ SPOTIFY CHARTS ")
print(40*"-")
print(df2.loc[df2["in_spotify_charts"]>100])
print(" ")

print("maximum streams attained by any song")
print(df2["streams"].max())
print("minimum streams attained by any songs")
print(df2["streams"].min())


print("   ===============================GRAPHS AND PLOTS ============================")
  
#RELATION BETWEEN POPULARITY (STREAMS) OF SONGS AND INSTRUMENTALNESS_%
pl.title("Streams and instrumentalness_% relation")
pl.xlabel("instrumentalness_%")
pl.ylabel("streams")
pl.bar(df2["instrumentalness_%"],df2["streams"],color="magenta")
pl.show()

#RELATION BETWEEN Speechiness(no of different spoken words in song) and streams 

pl.scatter(df2["speechiness_%"],df2["streams"],color="g",marker="*",s=10)
pl.xlabel("speechiness_%")
pl.ylabel("streams(in billion)")
pl.title("Relation between Streams and Speechiness")
pl.figure(figsize=(25,20))
pl.show()



pl.title("Relation between STREAMS ,INSTRUMENTALNESS AND ENERGY")
pl.scatter(df2["instrumentalness_%"],df2["streams"],color="red",marker="*",s=8)
pl.scatter(df2["energy_%"],df2["streams"], color="yellow",marker="*",s=8)
pl.xlabel("intrumentalness_% (red) and energy_%(yellow)")
pl.ylabel("Streams(in billion)")
pl.figure(figsize=(30,35))
pl.show()


pl.title("Relation between  and month of release")
pl.scatter(df2["released_month"],df2["streams"],color="orange",marker="^",s=8)
pl.ylabel("Months")
pl.xlabel("Streams(in billion)")
pl.show()


pl.title("danceability vs valence_% and energy_%")
pl.bar(df2["valence_%"],df2["danceability_%"],color="blue")
pl.bar(df2["energy_%"],df2["danceability_%"],color="orange")
pl.xlabel("valence_% and energy_%")
pl.ylabel("danceability_%")
pl.show()


pl.title("Relation BETWEEEN BPM and INSTRUMENTALNESS")
pl.bar(df2["bpm"],df2["instrumentalness_%"],color="brown")
pl.xlabel("bpm")
pl.ylabel("instrumentalness_%")
pl.show()


pl.title("relation between streams and release year of song ")
pl.bar(df2["released_year"],df2["streams"],color="yellow")
pl.xlabel("Release year of songs")
pl.ylabel("Streams")
pl.show()

print(" ")

#ACCESSING songs by your favourite  artist 

print("SONGS BY TAYLOR SWIFT")
print(50*"*")
print(df3[df3["artist(s)_name"]=="Taylor Swift"])
print(" ")
 

print("SONGS BY BTS ")
print(40*"=")
print(df3[df3["artist(s)_name"]=="BTS"])
print(" ")

print("SONGS BY Eminem")
print(df3[df3["artist(s)_name"]=="Eminem"])
print(" ")

print("SONGS BY Ed Sheeran")
print(30*"-o-")
print(df3[df3["artist(s)_name"]=="Ed Sheeran"])
print(" ")

print("SONGS BY JUSTIN BIEBER")
print(35*"--*--")
print(df3[df3["artist(s)_name"]=="Justin Bieber"])
print(" ")







