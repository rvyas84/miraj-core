class IdentifyUser:
    def identify_users(self, logs):
        user_actions = {}

        for log in logs:
            user_id = log.get("userId")
            action = log.get("action")

            if user_id is None or action is None:
                continue  # skip invalid entries

            if user_id not in user_actions:
                user_actions[user_id] = []

            user_actions[user_id].append(action)

        return user_actions
    

if __name__ == "__main__":

    logs = [
        {"action": "A", "userId": 1},
        {"action": "A", "userId": 1},
        {"action": "B", "userId": 2},
        {"action": "A", "userId": 1},
        {"action": "C", "userId": 2}
    ]

    result = IdentifyUser()
    print(result.identify_users(logs))


# Output
# {1: ['A', 'A', 'A'], 2: ['B', 'C']}