import sys
import string
import urllib.parse

_use_debug = False

sites = [
    'https://www.ufrgs.br/.../filmes-dublados-democratizacao-ou-crise-d...',
    'www.jornalmateriaprima.com.br/.../filmes-dublados-mutilam-a-arte...',
    'www.filmesonlinegratis.com/',
    'www.filmesonlinegratis.com/',
    'kodidogiba.blogspot.com › ... › Dicas do Giba › dublados › filmes',
    'https://tvuol.uol.com.br/.../filmes-dublado-e-completos-no-veoh-201...',
    'https://www.youtube.com/watch?v=NIazKisX2r4',
    'https://www.youtube.com/watch?v=NIazKisX2r4',
    'https://www.englishexperts.com.br/.../como-dizer-filmes-dublados-...',
    'www.redecanais.net/browse-filmes-dublado-videos-68-date.html',
    'https://www.youtube.com/watch?v=bUFd25kb7tk',
    'https://www.youtube.com/watch?v=bUFd25kb7tk',
    'https://canaldoensino.com.br/.../10-motivos-para-assistir-filmes-lege...',
    'https://designmp.net/tag/filmes-dublado/',
    'https://www.youtube.com/watch?v=U3kJBt4HxAk'
]

site='https://www.ufrgs.br/.../filmes-dublados-democratizacao-ou-crise-d...'



class ParseUrl:
    
    # method 0
    @staticmethod
    def process_site(site):
        to_find = '/'
        counter = 0
        current_pos = 0
        counter_aux = 0
        for l in site:
            counter += 1
            if l in to_find:
                if _use_debug:
                    print('FOUND: %s' % l)
                counter_aux += 1
            if counter_aux == 3:
                current_pos = counter
                if _use_debug:
                    print('END! last postition: %s' % current_pos)
                break
        return site[:current_pos]

    # method 1
    @staticmethod
    def process_site_1(site):
        DEFAULT_START_POS = 8
        try:
            pos = site.find('/', DEFAULT_START_POS)
            #print('POS: %s' % pos)
            if pos == -1:
                pos = site.find(' ')
                return site[:pos]
        except Exception as e:
            print('POSITION! / not found! in: %s' % e)
        # print('Current position: %s' % site[:pos + 1])
        return site[:pos + 1]

    # method 2
    @staticmethod
    def process_site_2(sites):
        lst_urls = []
        for site in sites:
            if _use_debug == False:
                print(urllib.parse.urlparse(site)[1])
            lst_urls.append(urllib.parse.urlparse(site)[1])
        return lst_urls

    # method 3
    @staticmethod
    def process_from_file(filename):
        # This function read a file and return a list of urls.
        list_of_processed_urls = []
        try:
            f = open(filename, 'r')
            data = f.readlines()
            if _use_debug == False:
                #print('Searching from filename: %s ' % filename)
                #print('Total length: %s' % len(data))
                #print('Output type: %s' % type(data))
                #list_of_processed_urls.append(process_site_2(data))
                for line in data:
                    #print('Translated: %s' % ParseUrl.process_site_1(line))
                    list_of_processed_urls.append(ParseUrl.process_site_1(line))
        except Exception as e:
            print('[ERROR] Custom exception: %s' % e)
        return list_of_processed_urls



# filename = '/home/jessie/Development/py_scripts/buscador/awesome-movie-db/data/database.txt'

# method 0
# print(process_site(site))

# method 1
# process_site_1(site)

# method 2
# print(process_site_2(sites))

# method 3
# filename = sys.argv[1]
# ParseUrl.process_from_file(filename)
