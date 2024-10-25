from states import States

class HeuristicFactory:
    @staticmethod
    def create_heuristic(heuristic_name):
        if heuristic_name == 'manhattan':
            return States().calc_manhattan_cost
        elif heuristic_name == 'euclidean':
            return States().calc_euclidean_cost
        else:
            raise ValueError('Invalid heuristic name')
