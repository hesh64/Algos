import collections


def accountsMerge(accounts):
    email_to_name = {}
    graph = collections.defaultdict(set)

    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            graph[acc[1]].add(email)
            graph[email].add(acc[1])
            email_to_name[email] = name
    seen = set()
    ans = []
    for email in graph:
        if email not in seen:
            seen.add(email)
            stack = [email]
            component = []
            while stack:
                node = stack.pop()
                component.append(node)
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            ans.append([email_to_name[email]] + sorted(component))
    return ans


def dfs_helper(graph, key, emails, visited):
    visited[key] = True
    for email in graph[key]:
        if visited[email] is False:
            emails.append(email)
            dfs_helper(graph, email, emails, visited)

    return emails


def accounts_merge(accounts):
    graph = collections.defaultdict(set)
    email_to_names = {}

    for account in accounts:
        name = account[0]
        for email in account[1:]:
            graph[email].add(account[1])
            graph[account[1]].add(email)
            email_to_names[account[1]] = name

    result = []
    visited = {k: False for k in graph.keys()}
    for key in graph:
        if visited[key] is False:
            user = [email_to_names[key]]
            res = dfs_helper(graph, key, [], visited)
            user.extend([s for s in res])
            result.append(user)

    return result


def main():
    accounts = [["Sarah", "sarah22@email.com", "sarah@gmail.com", "sarahhoward@email.com"],
                ["Alice", "alicexoxo@email.com", "alicia@email.com", "alicelee@gmail.com"],
                ["Sarah", "sarah@gmail.com", "sarah10101@gmail.com"],
                ["Sarah", "sarah10101@gmail.com", "misshoward@gmail.com"]]
    result = accountsMerge(accounts)
    print(result)

    result = accounts_merge(accounts)
    print(result)


main()
