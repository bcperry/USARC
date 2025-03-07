from studentdataobjects.JOBRanking import JOBRanking

class StudentDataObject:
    def __init__(self, unique_id, student_id, last_name, mos, oml, sorted_mos=None, branch_assigned=None, student_pick_num=None, duplicate=False, ranking_error=False):
        self.UniqueID = unique_id
        self.StudentID = student_id
        self.LastName = last_name
        self.JOB = mos  # List of JOBRanking objects
        self.OML = oml
        self.SortedJOB = sorted_mos if sorted_mos is not None else []  # List of JOBRanking objects
        self.BranchAssigned = branch_assigned
        self.StudentPickNum = student_pick_num
        self.Duplicate = duplicate
        self.RankingError = ranking_error

    def __repr__(self):
        return f"Student(UniqueID={self.UniqueID}, StudentID={self.StudentID}, LastName={self.LastName}, JOB={self.JOB}, OML={self.OML}, SortedJOB={self.SortedJOB}, BranchAssigned={self.BranchAssigned}, StudentPickNum={self.StudentPickNum}, Duplicate={self.Duplicate}, RankingError={self.RankingError})"
