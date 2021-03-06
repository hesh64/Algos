class RequestLimiter:
    def __init__(self):
        self.requests = {}

    def request_approver(self, timestamp, request):
        """return true if the message should be printed in the given
        timestamp, otherwise return false"""

        # 5 is our time limit
        if request not in self.requests or timestamp - self.requests[request] >= 5:
            self.requests[request] = timestamp
            print('Request Accepted')
            return True

        else:
            print('Request Rejected')
            return False


def main():
    obj = RequestLimiter()
    obj.request_approver(1, "send_message")
    obj.request_approver(2, "block")
    obj.request_approver(3, "send_message")
    obj.request_approver(8, "block")
    obj.request_approver(10, "send_message")
    obj.request_approver(11, "send_message")


main()
