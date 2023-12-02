#
# 929. Unique Email Addresses
#
# Q: https://leetcode.com/problems/unique-email-addresses/
# A: https://leetcode.com/problems/unique-email-addresses/discuss/186655/Concise-C%2B%2B
#

class Solution:
    def numUniqueEmails(self, A: List[str]) -> int:
        unique = set()
        for email in A:
            user, domain = email.split('@')
            user = user.replace('.', '')
            i = user.find('+')
            if -1 < i:
                user = user[0 : i]
            unique.add(f'{user}@{domain}')
        return len(unique)
