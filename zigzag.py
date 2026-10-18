def convert(s,numRows):

    for i in range(n):
        idx = i
        delta_south = 2(numRows-1-i)
        delta_north = 2*i
        bool  going_south = True

        while(idx < len(s)):
            if(i==0):
                idx+=delta_south
            else if (i==numsRows-1):
                idx+= delta_north
            else:
                if(going_south):
                    idx+=delta_south
                else:
                    idx+=delta_north

                going_south = !going_south    
