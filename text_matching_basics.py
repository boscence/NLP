# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 10:35:42 2017

@author: ALD29146
"""
match_dict = {}

#%%

def jaccard_similarityz(x,y):
 
    intersection_cardinality = len(set.intersection(*[set(x), set(y)]))
    union_cardinality = len(set.union(*[set(x), set(y)]))
    return intersection_cardinality/float(union_cardinality)



def name_match(a,b):
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a,b = b,a
        n,m = m,n

    current = range(n+1)
    for i in range(1,m+1):
        previous, current = current, [i]+[0]*n
        for j in range(1,n+1):
            add, delete = previous[j]+1, current[j-1]+1
            change = previous[j-1]
            if a[j-1] != b[i-1]:
                change = change + 1
            current[j] = min(add, delete, change)
    
    jaccard_score = jaccard_similarityz(a.split(),b.split())
    distance_pct_a = current[n]/len(a.replace(" ", ""))
    match_dict[a+' and '+b] = {'name_a':a,'name_b':b,'edit_dist':current[n],'edit_dist_pct':distance_pct_a,'jaccard':jaccard_score}
    #return current[n]




#%%
name_match('juan gabriel de la fuente garcia','juan de la fuente garcia')
name_match('Pedro gabriel de la fuente garcia','juan de la fuente diez')
name_match('Andrew Boscence','Richard Boscence')
name_match('Anne Boscence','Andrew Boscence')
name_match('Andrew Boscence','Andres Boscence')
name_match('Andres De Los Santos Ausin','Andres De Los Santos Diez')
name_match('Andres De Los Santos Ausin','Andres De Los Santos Diez')


match_dict

