# 9. Online Voting System
# • Description: Create a console application for an online voting system. Implement classes for Voter, Candidate, and Election. Include features for registering voters, casting votes, and displaying results.
# • OOP Concepts: Composition (elections consist of candidates), Inheritance (different voter types), and Encapsulation (managing voter information).

class Voter:
    voter_count=0
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.voter_id=f'V-{Voter.voter_count+1}'
        Voter.voter_count+=1
        self.voted=False
    def __str__(self):
        return f'Voter ID: {self.voter_id}\nName: {self.name}\nAge: {self.age}\n'
class Candidate:
    def __init__(self,name,party):
        self.name=name
        self.party=party
        self.votes=0
    def add_vote(self):
        self.votes+=1
    def __str__(self):
        return f'Candidate name: {self.name}\nParty: {self.party}\nTotal number of votes: {self.votes}\n'
class Election:
    def __init__(self,electionYear):
        self.election_Year=electionYear
        self.candidates=[]
        self.voters=[]
    def register_candidate(self,candidate):
        self.candidates.append(candidate)
    def register_voter(self,voter):
        self.voters.append(voter)
    def cast_vote(self,voter_id,candidate_name):
        voter=next((v for v in self.voters if v.voter_id==voter_id),None)
        candidate=next((c for c in self.candidates if c.name==candidate_name),None)
        if not voter:
            print("Voter not found.")
            return
        if voter.voted==True:
            print("Voter has already voted.")
            return
        if not candidate:
            print("Candidate not found.")
            return
        voter.voted=True
        candidate.add_vote()
        print("Voter voted.")
    def displayResult(self):
        print("Election result:")
        for candidate in self.candidates:
            print(f'Candidate:{candidate.name}\t\tVotes:{candidate.votes}')

c1=Candidate("Balen","Independent")
c2=Candidate("KP OLI","Congress")
v1=Voter("Pragyan",23)
v2=Voter("Hira",23)
v3=Voter("Nita",34)
v4=Voter("Rita",54)
v5=Voter("Sher Deuba",89)
e1=Election(2084)
e1.register_candidate(c1)
e1.register_candidate(c2)
e1.register_voter(v1)
e1.register_voter(v2)
e1.register_voter(v3)
e1.register_voter(v4)
e1.register_voter(v5)
e1.cast_vote('V-1',"Balen")
e1.cast_vote('V-2',"Balen")
e1.cast_vote('V-3',"Balen")
e1.cast_vote('V-4',"Balen")
e1.cast_vote('V-5',"KP OLI")
e1.displayResult()

