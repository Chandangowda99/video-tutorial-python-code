from mongoengine import connect

connect(
    db='project1',
    host='127.0.0.1',
    port=27017,
    username='mongoadmin',
    password='secret',
    authentication_source='admin',
    alias='project1'
)

connect(
    db='project2',
    host='127.0.0.1',
    port=27017,
    username='mongoadmin',
    password='secret',
    authentication_source='admin',
    alias='project2'
)

