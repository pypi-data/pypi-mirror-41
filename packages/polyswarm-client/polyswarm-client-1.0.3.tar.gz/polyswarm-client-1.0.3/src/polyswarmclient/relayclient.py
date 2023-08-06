import logging
from polyswarmclient.verify import RelayWithdrawDepositGroupVerifier

logger = logging.getLogger(__name__)  # Initialize logger


class RelayClient(object):
    def __init__(self, client):
        self.__client = client
        self.parameters = {}

    async def post_deposit(self, amount, api_key=None):
        """Post a deposit to the relay contract

        Args:
            amount (int): The amount to deposit to the sidechain
            api_key (str): Override default API key
        Returns:
            Response JSON parsed from polyswarmd containing emitted events
        """
        deposit = {
            'amount': str(amount),
        }
        verifier = RelayWithdrawDepositGroupVerifier(amount, self.__client.account)
        success, results = await self.__client.make_request_with_transactions('POST', '/relay/deposit', 'home', verifier,
                                                                              json=deposit, api_key=api_key)
        if not success or 'transfers' not in results:
            logger.error('Expected deposit to relay', extra={'extra': results})

        return results.get('transfers', [])

    async def post_withdraw(self, amount, api_key=None):
        """Post a withdrawal to the relay contract

        Args:
            amount (int): The amount to withdraw from the sidechain
            api_key (str): Override default API key
        Returns:
            Response JSON parsed from polyswarmd containing emitted events
        """
        withdrawal = {
            'amount': str(amount),
        }
        verifier = RelayWithdrawDepositGroupVerifier(amount, self.__client.account)
        success, results = await self.__client.make_request_with_transactions('POST', '/relay/withdrawal', 'side', verifier,
                                                                              json=withdrawal, api_key=api_key)
        if not success or 'transfers' not in results:
            logger.error('Expected withdrawl from relay', extra={'extra': results})
            return {}

        return results.get('transfers', [])
