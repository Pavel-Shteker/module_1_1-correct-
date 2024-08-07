example = ('Любишь Слаанеш - люби и BURN IN PURGING FLAMES!')

ostatok=len(example)%2
polovina=len(example)//2
correct=ostatok+polovina-1 #коррекция для нечета
print ('1) ', example[0])
print ('2) ', example[-1])
if ostatok==1:
    print ('3) ', example[correct::])
print ('3) ', example[polovina+ostatok::])
print ('4) ', example[::-1])
print ('5) ', example[1::2])
