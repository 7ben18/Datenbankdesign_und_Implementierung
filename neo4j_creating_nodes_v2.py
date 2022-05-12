import random
import lipsum
import json
import uuid

username = ["7ben18", "Stellarmilk", "Marvinra", "Zestolory", "Luuzemp"]
firstname = ["Ben", "Gabriel", "Marvin", "Simon", "Lukas"]
lastname = ["Tran", "Torres Gamez", "von Rappard", "Luder", "Zemp"]

category = ["School", "Gaming", "Lifestyle", "Movies", "Food"]

categories = []
posts = []
comments = []
users = []

nodes = []

relations = []


#
# Helpers
#

def generateId() -> str:
    return str(uuid.uuid4())


def getRandomString(length: int) -> str:
    return lipsum.generate_words(length)


def mergeNodes():
    [nodes.append({'n': c, 'type': 'Comment'}) for c in comments]
    [nodes.append({'n': p, 'type': 'Post'}) for p in posts]
    [nodes.append({'n': u, 'type': 'User'}) for u in users]
    [nodes.append({'n': c, 'type': 'Category'}) for c in categories]


def getRandomCategoryId():
    return categories[random.randint(0, len(categories) - 1)]['id']


def getRandomUserId():
    return users[random.randint(0, len(users) - 1)]['id']


def getRandomCommentId():
    return comments[random.randint(0, len(comments) - 1)]['id']


def getRandomPostId():
    return posts[random.randint(0, len(posts) - 1)]['id']


#
# Node creation
#

def createUsers():
    for i, user in enumerate(username):
        users.append({
            'id': generateId(),
            'username': user,
            'firstname': firstname[i],
            'lastname': lastname[i]
        })


def createCategories():
    for cat in category:
        categories.append({
            'id': generateId(),
            'title': cat
        })


def createPosts(num=100):
    for _ in range(num):
        posts.append({
            'id': generateId(),
            'title': getRandomString(5),
            'content': getRandomString(30)
        })


def createComments(num=200):
    for _ in range(num):
        comments.append({
            'id': generateId(),
            'text': getRandomString(12)
        })


#
# Relations
#

def createPostRelations():
    for post in posts:
        relations.append({
            'sourceType': 'Post',
            'targetType': 'Category',
            'sourceId': post['id'],
            'targetId': getRandomCategoryId(),
            'relationType': 'IS_OF_TYPE'
        })
        relations.append({
            'sourceType': 'User',
            'targetType': 'Post',
            'sourceId': getRandomUserId(),
            'targetId': post['id'],
            'relationType': 'CREATES'
        })


def createCommentRelations():
    for i, comment in enumerate(comments):
        relations.append({
            'sourceType': 'Comment',
            'targetType': 'Post' if i % 2 == 0 else 'Comment',
            'sourceId': comment['id'],
            'targetId': getRandomPostId() if i % 2 == 0 else getRandomCommentId(),
            'relationType': 'BELONGS_TO'
        })
        relations.append({
            'sourceType': 'User',
            'targetType': 'Comment',
            'sourceId': getRandomUserId(),
            'targetId': comment['id'],
            'relationType': 'CREATES'
        })


def printNodes():
    for node in nodes:
        print("CREATE (n:{}{})".format(node['type'], json.dumps(node['n'])))


def printRelations():
    for relation in relations:
        print("MATCH (source:{}), (target:{}) WHERE source.id = {} AND target.id = {} CREATE (source)-[{}]->(target)".format(relation['sourceType'], relation['targetType'], relation['sourceId'], relation['targetId'], relation['relationType']))


if __name__ == '__main__':
    createUsers()
    createCategories()
    createPosts()
    createComments()

    createPostRelations()
    createCommentRelations()

    mergeNodes()

    printNodes()
    printRelations()

