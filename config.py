DISCORD_TOKEN         = 'MTI1NjQ5MTkzMjY2Njk1Nzk0Nw.GPDdrT.NpMR5F_Oo1QWNVrAkZlAfnmr1qjIt6WsaGC-Bw'
cPREFIX               = '!'                                   # Префикс команды бота
embedColor            = 0x8c4bc9                              # Цвет плашки в дискорде

launcher = dict()
launcher['MUSTDIE']   = 'http://34.34.26.22:9274/Prestarter.jar'       # Ваша ссылка на windows версию лаунчера
launcher['LINUX/MAC'] = 'http://34.34.26.22:9274/Prestarter.exe'       # А здесь на linux/macos версию

db = dict()
db['host']            = 'localhost'                           # Хост mysql/mariadb
db['login']           = 'launchserver'                        # Имя пользователя mariadb
db['password']        = 'password'                            # Пароль от пользователя
db['db_name']         = 'db'                                  # База

scm = dict()
scm['skindir']        = './skins'                             # Путь к папке со скинами
scm['capedir']        = './capes'                             # Путь к папке с плащами
scm['url']            = 'http://34.34.26.22:9274/skinapi'            # Url из конфика nginx
scm['host']           = 'localhost'                           # Хост
scm['port']           = 8123                                  # Порт
scm['defaultSkin']    = './defaults/skin.png'                 # Путь к default скину
scm['defaultCape']    = './defaults/cape.png'                 # Путь к default плащу
