INSTALLED_APPS = ['athanor_forum']

GLOBAL_SCRIPTS = dict()

GLOBAL_SCRIPTS['forum'] = {
    'typeclass': 'athanor.controllers.forum.AthanorForumController',
    'repeats': -1, 'interval': 60, 'desc': 'Forum BBS API',
    'locks': "admin:perm(Admin)",
}