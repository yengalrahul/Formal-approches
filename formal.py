def simplification_one(clause):
    positive_atoms = clause[0]
    n = len(positive_atoms)
    positive_resolution_list = []
    for a in range(0, n):
        addition = True
        for b in range(a + 1, n):
            if positive_atoms[a] == positive_atoms[b]:
                addition = False
        if addition:
            positive_resolution_list.append(positive_atoms[a])
    return positive_resolution_list, clause[1]


clause1 = (["A", "A"], [])
clause2 = (["A", "B", "C", "A"], [])
clause3 = ([], [])
clause4 = (["A", "A", "A"], [])

print(simplification_one(clause1))

print(simplification_one(clause2))

print(simplification_one(clause3))

print(simplification_one(clause4))


def simplification_two(clause):
    negative_atoms = clause[1]
    n = len(negative_atoms)
    negative_resolution = []
    for a in range(0, n):
        addition = True
        for b in range(a + 1, n):
            if negative_atoms[a] == negative_atoms[b]:
                addition = False
        if addition:
            negative_resolution.append(negative_atoms[a])
    return clause[0], negative_resolution


clause1 = ([], ["A", "A"])
clause2 = ([], ["A", "B", "C", "A"])
clause3 = ([], [])
clause4 = ([], ["A", "A", "A"])

print(simplification_two(clause1))
print(simplification_two(clause2))
print(simplification_two(clause3))
print(simplification_two(clause4))


def resolution_check(clause1, clause2):
    combined = False
    # positive of clause1 & negative of clause2
    positive_atoms1 = clause1[0]
    negative_atoms2 = clause2[1]
    for a in positive_atoms1:
        for b in negative_atoms2:
            if a == b:
                combined = True
    # positive of clause2 & negative of clause1
    positive_atoms2 = clause2[0]
    negative_atoms1 = clause1[1]
    for a in positive_atoms2:
        for b in negative_atoms1:
            if a == b:
                combined = True
    return combined


def universal(clause):
    positive_atoms = clause[0]
    negative_atoms = clause[1]
    positive_resolution = []
    negative_resolution = []
    for a in positive_atoms:
        if a not in negative_atoms:
            positive_resolution.append(a)
    for b in negative_atoms:
        if b not in positive_resolution:
            negative_resolution.append(b)
    return positive_resolution, negative_resolution


print(universal((["A", "B", "c"], ["D", "c"])))


def resolution(clause1, clause2):
    positive_resolution = clause1[0] + clause2[0]
    negative_resolution = clause1[1] + clause2[1]
    clause = (positive_resolution, negative_resolution)
    clause = simplification_one(clause)
    clause = simplification_two(clause)
    clause = universal(clause)
    return clause


clause1 = (["A"], [])
clause2 = ([], ["A"])
clause3 = ([], ["B"])
clause4 = (["A", "B"], [])
clause5 = ([], ["A", "B"])
clause6 = (["B"], ["C"])
clause7 = (["C"], [])
clause8 = (["C"], ["A", "B"])
clause9 = (["B"], ["A"])
clause10 = ([], ["C"])
clause11 = (["A", "A", "B"], [])
clause12 = ([], ["A", "A"])
clause13 = ([], ["B", "B"])
clause14 = (["C"], ["C"])

print(resolution(clause1, clause2))

print(resolution(clause3, clause4))

print(resolution(clause1, clause5))

print(resolution(clause6, clause7))

print(resolution(clause8, clause10))

print(resolution(clause9, clause1))

print(resolution(clause4, clause2))


def satisfiable(clause):
    positive_atoms = clause[0]
    negative_atoms = clause[1]
    for a in positive_atoms:
        if a in negative_atoms:
            return True
    return False


def search_solution(clauses):
    for a in clauses:
        if satisfiable(a):
            clauses.remove(a)
    if len(clauses) != 0:
        cur_clause = clauses[0]
        for a in clauses[1:]:
            if resolution_check(cur_clause, a):
                clauses.remove(cur_clause)
                clauses.remove(a)
                cur_clause = resolution(cur_clause, a)
                if cur_clause == ([], []):
                    print("Unsatisfiable")
                else:
                    clauses.append(cur_clause)
                    return search_solution(clauses)


clause15 = (["B"], [])
clause16 = (["C"], ["A"])

print(search_solution([clause10, clause14]))

print(search_solution([clause4, clause9]))

print(search_solution([clause1, clause3]))

print(search_solution([clause11, clause12, clause13, clause14]))

print(search_solution([clause8, clause9, clause1, clause10]))

print(search_solution([clause1, clause5, clause6, clause7]))

print(search_solution([clause2, clause3, clause4]))

print(search_solution([clause1, clause2]))

print(search_solution([clause14]))

print(search_solution([clause8, clause16, clause1, clause15]))
