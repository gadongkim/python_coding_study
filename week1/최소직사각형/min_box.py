def solution(sizes):

    for i in range (len(sizes)):
        if(sizes[i][0]>sizes[i][1]) : 
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0];

    W = 0
    H = 0
    for j in range (len(sizes)):
        if(sizes[j][0]>W) :
            W = sizes[j][0];
        if(sizes[j][1]>H) :
            H = sizes[j][1];
            
    return W*H

    # w = 0
    # h = 0
    # for a, b in sizes:
    #     if a > b : a, b = b, a
    #     w = max(a,w)
    #     h = max(b,h)
    # return w*h