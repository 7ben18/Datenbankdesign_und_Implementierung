import random
username = ["7ben18", "Stellarmilk", "Marvinra", "Zestolory", "Luuzemp"]
firstname = ["Ben", "Gabriel", "Marvin", "Simon", "Lukas"]
lastname = ["Tran", "Torres Gamez", "von Rappard", "Luder", "Zemp"]

category = ["School","Gaming","Lifestyle","Movies","Food"]

comment_text = ["Extra thought out! Leading the way mate.",
                "Hugely magical camera angle, friend.",
                "Engaging work you have here.",
                "Adore your shot, friend.",
                "Super strong :-)",
                "I wonder what would have happened if I made this",
                "I think I'm crying. It's that admirable.",
                "White. Leading the way mate."]

random_words = ["Lorem","ipsum","dolor","sit","amet","consetetur","sadipscing","elitr",
                "sed","diam","nonumy","eirmod","tempor","invidunt","ut","labore",
                "et","dolore","magna","aliquyam","erat","sed","diam","voluptua",
                "At","vero","eos","et","accusam","et","justo","duo","dolores",
                "et","ea","rebum","Stet","clita","kasd","gubergren","no","sea",
                "takimata","sanctus","est","Lorem","ipsum","dolor","sit","amet",
                "Lorem","ipsum","dolor","sit","amet","consetetur","sadipscing",
                "elitr","sed","diam","nonumy","eirmod","tempor","invidunt","ut",
                "labore","et","dolore","magna","aliquyam","erat","sed","diam",
                "voluptua","At","vero","eos","et","accusam","et","justo","duo",
                "dolores","et","ea","rebum","Stet","clita","kasd","gubergren","no",
                "sea","takimata","sanctus","est","Lorem","ipsum","dolor","sit","amet",
                "Lorem","ipsum","dolor","sit","amet","consetetur","sadipscing","elitr",
                "sed","diam","nonumy","eirmod","tempor","invidunt","ut","labore","et",
                "dolore","magna","aliquyam","erat","sed","diam","voluptua","At","vero",
                "eos","et","accusam","et","justo","duo","dolores","et","ea","rebum",
                "Stet","clita","kasd","gubergren","no","sea","takimata","sanctus","est",
                "Lorem","ipsum","dolor","sit","amet","","","Duis","autem","vel","eum",
                "iriure","dolor","in","hendrerit","in","vulputate","velit","esse","molestie",
                "consequat","vel","illum","dolore","eu","feugiat","nulla","facilisis","at",
                "vero","eros","et","accumsan","et","iusto","odio","dignissim","qui","blandit",
                "praesent","luptatum","zzril","delenit","augue","duis","dolore","te","feugait",
                "nulla","facilisi","Lorem","ipsum","dolor","sit","amet","consectetuer","adipiscing",
                "elit","sed","diam","nonummy","nibh","euismod","tincidunt","ut","laoreet","dolore",
                "magna","aliquam","erat","volutpat","","","Ut","wisi","enim","ad","minim",
                "veniam","quis","nostrud","exerci","tation","ullamcorper","suscipit","lobortis",
                "nisl","ut","aliquip","ex","ea","commodo","consequat","Duis","autem","vel",
                "eum","iriure","dolor","in","hendrerit","in","vulputate","velit","esse","molestie",
                "consequat","vel","illum","dolore","eu","feugiat","nulla","facilisis","at","vero",
                "eros","et","accumsan","et","iusto","odio","dignissim","qui","blandit","praesent",
                "luptatum","zzril","delenit","augue","duis","dolore","te","feugait","nulla"]

def create_category():
    cnt = 0
    while cnt <= len(category) - 1 :
        print("CREATE (p" + str(cnt) + ":Catergory{category_id:" + str(cnt) \
              + ", category:" + "\"" + category[cnt] + "\"" \
              + "})")
        cnt += 1

def create_person():
    cnt = 0
    while cnt <= len(username) - 1 :
        print("CREATE (p" + str(cnt) + ":Person{person_id:" + str(cnt) \
              + ", username:" + "\"" + username[cnt] + "\"" \
              + ", fistname:" + "\"" + firstname[cnt] + "\"" \
              + ", lastname:" + "\"" + lastname[cnt] + "\"" \
              + "})")
        cnt += 1

post_title = [] # Brauche ich fuer die Beziehung von Kommentar und Post!
def create_post(number: int):
    cnt = 0
    while cnt <= number:
        random_cat = random.choice(category)
        random_user = random.choice(username)
        random_title = random.choices(random_words, k = random.choice(range(5, 12)))
        random_title = " ".join([str(item) for item in random_title])
        random_content = random.choices(random_words, k=random.choice(range(50, 150)))
        random_content = " ".join([str(item) for item in random_content])

        print("CREATE (po" + str(cnt) + ":Post{post_id:" + str(cnt) + ", username:" \
              + "\"" + str(random_user) + "\"" \
              + ", category:" + "\"" + str(random_cat) + "\"" \
              + ", title:" + "\"" + str(random_title) + "\"" \
              + ", content:" + "\"" + str(random_content) + "\"" + "})")

        post_title.append(random_title)
        cnt += 1


def create_comment():
    cnt = 0
    while cnt <= len(post_title) - 1:
        random_text = random.choices(random_words, k=random.choice(range(25, 100)))
        random_text = " ".join([str(item) for item in random_text])
        random_user = random.choice(username)
        print("CREATE (com" + str(cnt) + ":Comment{comment_id:" + str(cnt) \
              + ", username:" + "\"" + str(random_user) + "\"" \
              + ", post_title:" + "\"" + post_title[0] + "\"" \
              + ", text:" + "\"" + str(random_text) + "\"" \
              + "})")
        cnt += 1



def realtion_person_post():
    cnt = 0
    while cnt <= len(username) - 1:
        print("MATCH (n:Person), (po:Post) " + \
              "WHERE n.username = " + "\"" + str(username[cnt]) + "\"" \
              + "AND po.username = " + "\"" + username[cnt] + "\"" \
              + "CREATE (n)-[p:post]->(po)")
        cnt += 1

def realtion_person_comment():
    cnt = 0
    while cnt <= len(username) - 1:
        print("MATCH (n:Person), (com:Comment) " + \
              "WHERE n.username = " + "\"" + str(username[cnt]) + "\"" \
              + " AND com.username = " + "\"" + username[cnt] + "\"" \
              + " CREATE (n)-[co:comment]->(com)")
        cnt += 1

def realtion_category_post():
    cnt = 0
    while cnt <= len(category) - 1:
        print("MATCH (cat:Catergory), (po:Post) " + \
              "WHERE cat.category = " + "\"" + str(category[cnt]) + "\"" \
              + " AND po.category = " + "\"" + str(category[cnt]) + "\"" \
              + " CREATE (po)-[t:type]->(cat)")
        cnt += 1


def realtion_comment_post():
    cnt = 0
    while cnt <= len(post_title) - 1:
        print("MATCH (com:Comment), (po:Post) " + \
              "WHERE com.post_title = " + "\"" + str(post_title[cnt]) + "\"" \
              + " AND po.title = " + "\"" + str(post_title[cnt]) + "\"" \
              + " CREATE (com)-[cm:comenting]->(po)")
        cnt += 1

realtion_comment_post()


create_person()
print()
create_post(1)
print()
create_comment()
print()
create_category()
print()
realtion_comment_post()
print()
realtion_person_post()
print()
realtion_category_post()
print()
realtion_person_comment()

