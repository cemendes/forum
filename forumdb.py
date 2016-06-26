#
# Database access functions for the web forum.
#

import psycopg2

## Database connection
db = psycopg2.connect("dbname=forum")
cur = db.cursor()

## Get posts from database.
def GetAllPosts():
  query = "select * from posts;"
  cur.execute(query)
  posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cur.fetchall())
#  db.close()
  #posts.sort(key=lambda row: row['time'], reverse=True) 
  return posts

    # '''Get all the posts from the database, sorted with the newest first.

    # Returns:
    #   A list of dictionaries, where each dictionary has a 'content' key
    #   pointing to the post content, and 'time' key pointing to the time
    #   it was posted.
    # '''
    # posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    # posts.sort(key=lambda row: row['time'], reverse=True)
    # return posts


## Add a post to the database.
def AddPost(content):
  print content
  cur.execute("insert into posts(content) values(%s)",(content,))
  db.commit()
#  db.close()
#     '''Add a new post to the database.

#     Args:
#       content: The text content of the new post.
#     '''
#      c = DB.cursor()
#      c.execute("insert into content values('dudu')")
#      DB.commit
# #    t = time.strftime('%c', time.localtime())
# #    DB.append((t, content))
