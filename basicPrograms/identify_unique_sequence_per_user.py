class IdentifySequence:
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

    def identify_sequence(self, logs):
        user_actions = self.identify_users(logs)
        pattern_map = {}

        for user_id, actions in user_actions.items():
            pattern = "".join(actions)
            pattern_map[pattern] = user_id

        return pattern_map
    

if __name__ == "__main__":

    logs = [
        {"action": "A", "userId": 1},
        {"action": "A", "userId": 1},
        {"action": "B", "userId": 2},
        {"action": "A", "userId": 1},
        {"action": "C", "userId": 2}
    ]

    result = IdentifySequence()
    print(result.identify_sequence(logs))


# Output
# {'AAA': 1, 'BC': 2}