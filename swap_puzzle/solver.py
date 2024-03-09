from grid import Grid


class Solver(Grid):
    def __init__(self, n, m, initial_state=None):
        super().__init__(n, m, initial_state)
        self.n = n
        self.m = m

    def creer_matrice(self,n,m):
        return [[i+j*self.m+1 for i in range(self.m)]for j in range(self.n)]


#Solution naïve
    def get_solution(self):
        swp = []
        nb = 0
        Lo = self.creer_matrice(self.n, self.m)  # Use self to access the class attribute
        while self.state != Lo:
            for i in range(1, self.n * self.m + 1):
                x = self.trouver_indice_element(Lo, i)  # Use self to access the method
                for k in range(self.n):
                    for j in range(self.m):
                        if self.state[k][j] == i:
                            ind = [k, j]
                while ind[0] != x[0]:
                    nb += 1
                    if x[0] < ind[0]:
                        self.swap((ind[0] - 1, ind[1]), (ind[0], ind[1]))
                        swp.append(((ind[0] - 1, ind[1]), (ind[0], ind[1])))
                        ind[0] -= 1
                    elif x[0] > ind[0]:
                        self.swap((ind[0] + 1, ind[1]), (ind[0], ind[1]))
                        swp.append(((ind[0] + 1, ind[1]), (ind[0], ind[1])))
                        ind[0] += 1
                while ind[1]!=x[1]:
                    if x[1] < ind[1]:
                        self.swap((ind[0], ind[1] - 1), (ind[0], ind[1]))
                        swp.append(((ind[0], ind[1] - 1), (ind[0], ind[1])))
                        ind[1] -= 1
                    elif x[1] > ind[1]:
                        self.swap((ind[0], ind[1]+1), (ind[0], ind[1]))
                        swp.append(((ind[0], ind[1]+1), (ind[0], ind[1])))
                        ind[1] += 1

        return nb, swp