from random import *
def nahodna_veta():
    kto = choice(('Kamarát','Spolužiak','Andrej','Roman','Gertruda','Helena'))
    corobil = choice(('videl','prezradil','povedal','napísal','zistil',
                        'nakreslil'))

    ake = choice(('veľké','malé','obrovské','drobné','smutné','veselé'))
    co = choice(('tajomstvo','prekvapenie','predsavzatie'))
    if kto=='Gertruda' or kto=='Helena':
        spojene = kto +' '+corobil+'a'+' '+ake+' '+co+'.'
    else:
        spojene = kto +' '+corobil+' '+ake+' '+co+'.'
    print(spojene)
for i in range(1,21):
    nahodna_veta()
