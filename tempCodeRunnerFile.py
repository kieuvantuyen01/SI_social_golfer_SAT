    nWeeks, size, nGroups = data
        nPlayers = nGroups * size

        result_dict = {
            "Problem": f"{nWeeks}-{size}-{nGroups}",
            "Type": "PyCSP",
            "Time": "",
            "Result": "",
            "Variables": 0,
        }
        result_dict["Variables"] = nWeeks * nPlayers

        print(f"Social Golfer Problem with {nPlayers} players, {nGroups} groups of size {size} and {nWeeks} weeks")

        # x[w][p] is the group admitting on week w the player p
        x = VarArray(size=[nWeeks, nPlayers], dom=range(nGroups))

        satisfy(
            # ensuring that two players don't meet more than one time
            [
                If(
                    x[w1][p1] == x[w1][p2],
                    Then=x[w2][p1] != x[w2][p2]
                ) for w1, w2 in combinations(range(nWeeks), 2) for p1, p2 in combinations(range(nPlayers), 2)
            ],
            # respecting the size of the groups
            [Cardinality(x[w], occurrences={i: size for i in range(nGroups)}) for w in range(nWeeks)],
            # tag(symmetry-breaking)
            LexIncreasing(x, matrix=True)
        )
        
        # solve_time = time.time() - start_time
        result_dict["Clauses"] = len(posted())
        # Create a Process