from matrix import *
from draw import *

# file that generates a drawing script, since
# the script itself has over 2100 lines
# also set DEFAULT_COLOR to black, and the drawing color to green

def triangle(a,b,c):
    edges=[]
    add_edge(edges,*a,*b)
    add_edge(edges,*b,*c)
    add_edge(edges,*c,*a)
    return edges

def string(edges):
    ans=''
    for i in range(0,len(edges),2):
        ans+='line\n'
        ans+=' '.join(list(map(lambda x: str(int(x)),edges[i][:-1]+edges[i+1][:-1])))+'\n'
    return ans

file = open('script2.txt','w')
edges=triangle([50,50,0],[150,250,0],[250,50,0])
for i in range(360):
    matrix_mult(make_rotZ(1), edges)
    matrix_mult(make_scale(0.8,0.8,0.8),edges)
    matrix_mult(make_translate(250, 250, 0), edges)
    file.write(string(edges))
    matrix_mult(make_translate(-250, -250, 0), edges)
    matrix_mult(make_scale(5/4, 5/4, 5/4), edges)
file.write('display\n')
file.write('save\n03.png\n')
file.write('quit\n')
file.close()