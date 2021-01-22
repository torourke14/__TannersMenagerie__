import random



def alignStrings(x, y) :

    S = [[0 for i in range (len(x)+1)] for j in range (len(y)+1)]

    for j in range(0, len(y)+1): #fill top row by i

        S[j][0] = j

    for i in range(0, len(x)+1): #fill first column by i

        S[0][i] = i

    

    for i in range(1, len(y)+1):

        for j in range(1, len(x)+1):

            csub = 12

            if (x[j-1] == y[i-1]): #no-op for sub

                csub = 0

            if (i > 1 and j > 1): #set S[i][j] to min of operation costs

                sub =    S[i-1][j-1] + csub

                delete = S[i-1][j] + 1

                insert = S[i][j-1] + 1

                swap =   S[i-2][j-2] + 13 + (2*csub)

                S[i][j] = min(sub, delete, insert, swap)

            else: # Set S[i][j] to min cost of any operation cost except swap

                sub =    S[i-1][j-1] + csub

                delete = S[i-1][j] + 1

                insert = S[i][j-1] + 1

                S[i][j] = min(sub, delete, insert)   

    return S



def extractAlignment(S,x,y) : 

    # S = optimal cost matrix from alignStrings, x,y = string x,y 

    path = []   # vector of edit operations

    h = len(x)

    w = len(y)

    while w > 0 or h > 0: # loop back to the beginning

        operations = []

        #check for swaps --> sub/no-ops --> then indels

        if (w > 1 and h > 1):

            if ((S[w][h]-13 == S[w-2][h-2]) or (S[w][h]-13-24 == S[w-2][h-2])):

                operations.append('swap')

        # check for sub/no-ops before indels

        if (w > 0 and h > 0): 

            if (S[w][h]-12 == S[w-1][h-1]):

                operations.append('sub')

            if ( (S[w][h] == S[w-1][h-1]) and (x[h-1] == y[w-1]) ):

                operations.append('no-op')

        # if at y[0], must traverse to S[0][0] w/dels

        if (w > 0):

            if (S[w][h]-1 == S[w-1][h]):

                operations.append('delete')

        # if at x[0], must traverse to S[0][0] w/inserts

        if (h > 0): 

            if (S[w][h]-1 == S[w][h-1]):

                operations.append('insert')

        

        rind = random.randint(0,len(operations)-1)

        if(operations[rind] == 'no-op'):

            w = w - 1

            h = h - 1

        if(operations[rind] == 'delete'):

            w = w - 1

        if(operations[rind] == 'insert'):

            h = h - 1

        if(operations[rind] == 'sub'):

            w = w - 1

            h = h - 1

        if(operations[rind] == 'swap'):

            w = w - 2

            h = h - 2

        path.insert(0, operations[rind])

    return (path)



def commonSubstrings(x,L,a):

    # params -- string x, integer 1<=L<= len(x), sequence of edits a

    # return -- substrings (len >= L) in x that aligns (via no-ops) to substring in y

    substrings = []

    substr = ""

    ind = 0 

    for i in range(0,len(a)): # loop through list of edits

        # If a no-op -- append x[ind] to substr until we use an op

        if(a[i]== 'no-op'): 

            substr = substr + x[ind]

            ind = ind + 1 

        else:

            # If not a no-op -- append substr, reset substr, increment 'ind'

            if (len(substr) >= L): 

                substrings.append(substr)

            substr = ""

            if(a[i] == 'insert'): 

                ind = ind + 1 

            if(a[i] == 'swap'): 

                ind = ind + 2     

    if ( len(substr) >= L ): # if list of edits a ends with a no-op

        substrings.append(substr)

    return substrings 



def main():    

    x = "the white house office of the press secretary for immediate release march 06, 2017 president trump congratulates exxon mobil for job-creating investment program  washington, d.c. -- president donald j. trump today congratulated exxon mobil corporation on its ambitious $20 billion investment program that is creating more than 45,000 construction and manufacturing jobs in the united states gulf coast region.  president trump made a promise to bring back jobs to america. the spirit of optimism sweeping the country is already boosting job growth, and it is only the beginning.  “this is exactly the kind of investment, economic development and job creation that will help put americans back to work,” the president said. “many of the products that will be manufactured here in the united states by american workers will be exported to other countries, improving our balance of trade. this is a true american success story. in addition, the jobs created are paying on average $100,000 per year.”  darren w. woods, chairman and chief executive officer of exxon mobil announced the company’s investment program during a keynote speech today to an oil and gas industry conference in houston, texas.  “investments of this scale require a pro-growth approach and a stable regulatory environment and we appreciate the president’s commitment to both,” said woods. “the energy industry has proven it can operate safely and responsibly. private sector investment is enhanced by this administration’s support for smart regulations that support growth while protecting the environment.”  exxon mobil is strategically investing in new refining and chemical-manufacturing projects in the united states gulf coast region to expand its manufacturing and export capacity. the company’s growing the gulf program consists of 11 major chemical, refining, lubricant and liquefied natural gas projects at proposed new and existing facilities along the texas and louisiana coasts. investments began in 2013 and are expected to continue through at least 2022.  exxon mobil’s projects, once completed and operating at mature levels, are expected to have far-reaching and long-lasting benefits. projects planned or under way are expected to create more than 35,000 construction jobs and more than 12,000 full-time jobs. these are full-time manufacturing jobs that are mostly high-skilled and high-paying, and have annual salaries ranging from $75,000 to $125,000. these jobs will have a multiplier effect, creating many more jobs in the community that service these new investments."

    y = "exxonmobil plans investments of $20 billion to expand manufacturing in u.s. gulf region new projects expected to create more than 45,000 high-paying jobs across the region and thousands more through multiplier effect dateline: houston  public company information: nyse:xom  houston--(business wire)--exxon mobil corporation (nyse:xom) is expanding its manufacturing capacity along the u.s. gulf coast through planned investments of $20 billion over a 10-year period to take advantage of the american energy revolution, darren woods, chairman and chief executive officer, said monday.  the projects, at 11 proposed and existing sites, are expected to generate thousands of new high-paying jobs and $20 billion in increased economic activity in texas and louisiana, woods said, highlighting the company’s growing the gulf initiative in a keynote speech today at the ceraweek 2017 conference.  “the united states is a leading producer of oil and natural gas, which is incentivizing u.s. manufacturing to invest and grow,” said woods. “we are using new, abundant domestic energy supplies to provide products to the world at a competitive advantage resulting from lower costs and abundant raw materials. in this way, an upstream technology breakthrough has led to a downstream manufacturing renaissance.”  exxonmobil is strategically investing in new refining and chemical-manufacturing projects in the u.s. gulf coast region to expand its manufacturing and export capacity. the company’s growing the gulf expansion program, consists of 11 major chemical, refining, lubricant and liquefied natural gas projects at proposed new and existing facilities along the texas and louisiana coasts. investments began in 2013 and are expected to continue through at least 2022.  woods said that exxonmobil’s gulf expansion projects are expected to provide long-term economic benefits to the region, noting the creation of direct employment opportunities and the multiplier effects of the company’s investments.  “importantly, growing the gulf also creates jobs and lasting economic benefits for the communities where they’re located,” woods said. “all told, we expect these 11 projects to create over 45,000 jobs. many of these are high-skilled, high-paying jobs averaging about $100,000 a year. and these jobs will have a multiplier effect, creating many more jobs in the communities that service these new investments.”  according to the american chemistry council, chemical manufacturing is one of america’s top exporting industries, accounting for 14 percent of overall u.s. exports in 2015, and exports of specific chemicals linked to shale gas are projected to reach $123 billion by 2030. most of exxonmobil’s planned new chemical capacity investment in the gulf region is targeted toward export markets in asia and elsewhere.  “these projects are export machines, generating products that high-growth nations need to support larger populations with higher standards of living,” woods said. “those overseas markets are the motivation behind our investments. the supply is here; the demand is there. we want to keep connecting those dots.”  about exxonmobil  exxonmobil, the largest publicly traded international oil and gas company, uses technology and innovation to help meet the world’s growing energy needs. exxonmobil holds an industry-leading inventory of resources, is one of the largest refiners and marketers of petroleum products and its chemical company is one of the largest in the world. for more information, visit www.exxonmobil.com or follow us on twitter www.twitter.com/exxonmobil."

    S = alignStrings(x, y)

    a = extractAlignment(S, x, y)

    substrings9 = commonSubstrings(x, 9, a)

    print (substrings9)

if __name__ == "__main__":

    main()