# file = open("Hw3Big.txt", encoding='utf8')
file = open("Hw3Small.txt", encoding='utf8')
lines = file.readlines()
file.close()

# MOVIE_DICTIONARY (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main().

def load_data_to_movie_dict(lines):
  movies = dict()
  # Your code here
  f=['HSET',' title',' genre',' votes',' rating',' release_year',' plot',' poster',' ibmdb_id']
  for i in lines:
    s=i.strip()
    fbpos=[i.find(e)+len(e) for e in f if i.find(e)!=-1]
    ffpos=[i.find(e) for e in f[1:] if i.find(e)!=-1]
    ffpos+=[1000000000]
    tem_dict=dict()
    for j in range(len(fbpos)):
      tem_s=s[fbpos[j]:ffpos[j]].strip().strip('\"')
      while tem_s.find('\\"')!=-1:
        bpos=tem_s.find('\\"')
        fpos=tem_s[bpos+2:].find('\\"')+bpos+2
        tem_s=tem_s[:bpos]+tem_s[bpos+2:fpos]+tem_s[fpos+2:]
      if j==0: k=int(tem_s.split(':')[1])
      elif j in [3,4]: tem_dict[f[j][1:]]=float(tem_s)
      elif j==5: tem_dict[f[j][1:]]=int(tem_s)
      else: tem_dict[f[j][1:]]=tem_s
    movies[k]=tem_dict
  return movies

#------------------------------------------------------------#

def summarize_movies_by_genre(movies):
  movies_by_genre = dict()
  # Your code here
  for i in movies:
    if movies[i]['genre'] not in movies_by_genre:
      movies_by_genre[movies[i]['genre']]=[i]
    else: movies_by_genre[movies[i]['genre']]+=[i]
  for j in movies_by_genre: movies_by_genre[j].sort()
  return movies_by_genre

#------------------------------------------------------------#

def calcualte_genre_stats(movies, movies_by_genre):
  genre_stats = dict()
  # Your code here
  for i in movies_by_genre:
    r=[movies[j]['rating'] for j in movies_by_genre[i]]
    v=[movies[j]['votes'] for j in movies_by_genre[i]]
    genre_stats[i]={'num':len(movies_by_genre[i]),'rating':round(sum(r)/len(r),2),'votes':round(sum(v)/len(v),2)}
  return genre_stats

#------------------------------------------------------------#    
# DO NOT DELETE OR MODIFIED THE CODE BELOW
#------------------------------------------------------------#

from collections import OrderedDict

# print "data" dict ordered by key
# if top is blank, print all members in the data
# if details is true, print detailed data
#   ; otherwise, print only the number of attributes
def print_ordered_dict(data, top='', details=True):
  if top == '':
    top = len(data)
  sorted_ids = sorted(data.keys())[:top]

  i = 0
  for id in sorted_ids:
    if details:
      print(id, data[id])
    else:
      print(id, len(data[id]))

#------------------------------------------------------------#
# *** MAIN PART ****
movies = load_data_to_movie_dict(lines)
movies_by_genre = summarize_movies_by_genre(movies)
genre_stats = calcualte_genre_stats(movies, movies_by_genre)

#------------------------------------------------------------#

# print(len(movies))
# print_ordered_dict(data=movies, top=200, details=False) # print attributes (Google Sheet1)
# print_ordered_dict(data=movies, top=200, details=True) # print data (Google Sheet2)

# print(len(movies_by_genre))
# print_ordered_dict(data=movies_by_genre, top=5, details=False) # print attributes (Google Sheet3)
# print_ordered_dict(data=movies_by_genre, top=5) # print data (Google Sheet4)
# print_ordered_dict(data=genre_stats, top=5) # print data (Google Sheet5)