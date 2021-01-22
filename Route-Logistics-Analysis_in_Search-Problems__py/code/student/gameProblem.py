
'''
    Class gameProblem, implements simpleai.search.SearchProblem
'''


from simpleai.search import SearchProblem
# from simpleai.search import breadth_first,depth_first,astar,greedy
import simpleai.search

class GameProblem(SearchProblem):

    # Object attributes, can be accessed in the methods below

    MAP=None
    POSITIONS=None
    INITIAL_STATE=None
    GOAL=None
    CONFIG=None
    AGENT_START=None
    SHOPS=None
    CUSTOMERS=None
    MAXBAGS = 0

    MOVES = ('West','North','East','South')

   # --------------- Common functions to a SearchProblem -----------------

    def actions(self, state):

        '''returns available actions at each given step'''
        actions = ['West','North','East','South']

        # At loadable pizza AND has room (2 max)
        if ( (state[0],state[1]) in self.POSITIONS['pizza']) and (state[2] < 2):
            actions.append('Load')
        #At customer AND unloaded as many as possible
        if (self.getAttribute((state[0],state[1]),'unload')) and (state[2] > 0):
            actions.append('Unload')

        if ((state[0]+1 > self.CONFIG['map_size'][0]-1) or (self.getAttribute((state[0]+1,state[1]), 'blocked'))):
            actions.remove('East')
        if (state[1]-1 < 0) or (self.getAttribute((state[0],state[1]-1), 'blocked')):
            actions.remove('North')
        if ((state[1]+1 >= self.CONFIG['map_size'][1])) or (self.getAttribute((state[0],state[1]+1), 'blocked')):
            actions.remove('South')
        if (state[0]-1 < 0) or (self.getAttribute((state[0]-1,state[1]), 'blocked')):
            actions.remove('West')
        return actions

    
    def result(self, state, action):
        '''Returns the state reached from this state when the given action is executed'''
        nextstate = list(state)

        if action == 'Load':
            nextstate[2] = nextstate[2] + 1
        if action == 'Unload':
            nextstate[3] = nextstate[3] + 1
            nextstate[2] = nextstate[2] - 1
        if action == 'East':
            nextstate[0] = nextstate[0] + 1
        if action == 'South':
            nextstate[1] = nextstate[1] + 1
        if action == 'North':
            nextstate[1] = nextstate[1] - 1
        if action == 'West':
            nextstate[0] = nextstate[0]-1

        new_state = (nextstate[0],nextstate[1],nextstate[2],nextstate[3])
        return new_state


    def is_goal(self, state):
        return ( state == (0,0,0,2))


    def cost(self, state, action, state2):
        #insert cost function
        return 1


    def heuristic(self, state):
        # Heuristic = Manhattan Distance

        # Still pizzas left--> min dist of pizzas left
        if (state[2] <= len(self.POSITIONS['pizza'])) and (state[3] < 2): 
            dists = []
            for p in self.POSITIONS['pizza']:
                dists.append( abs(p[0]-state[0]) + abs(p[1]-state[1]) )
            return min(dists)

        # Delivering pizzas --> dist to customer
        elif (state[3] < len(self.POSITIONS['pizza'])) and (state[2] == 0):
            return (abs(self.POSITIONS['customer1'][0][0]-state[0]) + abs(self.POSITIONS['customer1'][0][1]-state[1]))
        
        # Go home!
        else:
            return (abs(self.POSITIONS['start'][0][0]-state[0]) + abs(self.POSITIONS['start'][0][1]-state[1]))

    def setup (self):
        '''This method must create the initial state, final state (if desired) and specify the algorithm to be used.
           This values are later stored as globals that are used when calling the search algorithm.
           final state is optional because it is only used inside the is_goal() method

           It also must set the values of the object attributes that the methods need, as for example, self.SHOPS or self.MAXBAGS
        '''
        print ("\nMAP: ", self.MAP, '\n')
        #print ("POSITIONS: ", self.POSITIONS, '\n')
        #print ("CONFIG: ", self.CONFIG, '\n')

        #--> initial_state / state = (x, y, pizzas in bag, pizzas delivered)
        initial_state = (self.AGENT_START[0],self.AGENT_START[1] , 0 , 0)
        final_state= (0, 0, 0, 2)
        
        #algorithm= simpleai.search.astar
        #algorithm= simpleai.search.breadth_first
        #algorithm= simpleai.search.depth_first
        algorithm = simpleai.search.limited_depth_first
        return initial_state,final_state,algorithm

    def printState (self,state):
        '''Return a string to pretty-print the state '''

        pps=''
        return (pps)

    def getPendingRequests (self,state):
        ''' Return the number of pending requests in the given position (0-N).
            MUST return None if the position is not a customer.
            This information is used to show the proper customer image.
        '''
        return None

    # -------------------------------------------------------------- #
    # --------------- DO NOT EDIT BELOW THIS LINE  ----------------- #
    # -------------------------------------------------------------- #

    def getAttribute (self, position, attributeName):
        '''Returns an attribute value for a given position of the map
           position is a tuple (x,y)
           attributeName is a string

           Returns:
               None if the attribute does not exist
               Value of the attribute otherwise
        '''
        tileAttributes=self.MAP[position[0]][position[1]][2]
        if attributeName in tileAttributes.keys():
            return tileAttributes[attributeName]
        else:
            return None

    def getStateData (self,state):
        stateData={}
        pendingItems=self.getPendingRequests(state)
        if pendingItems >= 0:
            stateData['newType']='customer{}'.format(pendingItems)
        return stateData

    # THIS INITIALIZATION FUNCTION HAS TO BE CALLED BEFORE THE SEARCH
    def initializeProblem(self,map,positions,conf,aiBaseName):
        self.MAP=map
        self.POSITIONS=positions
        self.CONFIG=conf
        self.AGENT_START = tuple(conf['agent']['start'])

        initial_state,final_state,algorithm = self.setup()
        if initial_state == False:
            print ('-- INITIALIZATION FAILED')
            return True

        self.INITIAL_STATE=initial_state
        self.GOAL=final_state
        self.ALGORITHM=algorithm
        super(GameProblem,self).__init__(self.INITIAL_STATE)

        print ('-- INITIALIZATION OK')
        return True

    # END initializeProblem
