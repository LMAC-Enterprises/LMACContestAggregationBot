class DefaultConfiguration:
    finalistMinimumReputation: int = 49
    finalistMinimumHP: int = 250

    mysqlServerAddress: str = ''
    mysqlUser: str = ''
    mysqlPassword: str = ''
    mysqlDatabase: str = ''

    searchInAccount: str = ''

    apiKey: str = ''
    apiUrl: str = ''


class Configuration(DefaultConfiguration):
    mysqlHost = "localhost"
    mysqlUser = ""
    mysqlPassword = ""
    mysqlDatabaseName = ""

    searchInAccount = 'lmac'

    searchInMaxPosts = 100

    apiKey = '<SECRET KEY>'
    apiUrl = 'http://<HOST>/lmac-api/v1/lmac'
