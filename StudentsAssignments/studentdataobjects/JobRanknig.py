class JOBRanking:
    def __init__(self, job, ranking):
        self.JOB = job
        self.Ranking = ranking

    def getJOB (self):
        return self.JOB
    
    def getRanking (self):
        return self.Renking
    
    def __repr__(self):
        return f"JOBRanking(JOB={self.JOB}, Ranking={self.Ranking})"
