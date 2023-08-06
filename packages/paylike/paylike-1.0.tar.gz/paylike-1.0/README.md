# paylike-python-sdk
Python implementation of Paylike.io's rest api

## Limitation
Only the transaction management part has been implemented, you can find the official api documentation here:
https://github.com/paylike/api-docs#transactions

## Basic Usage
```python
client = PaylikeApiClient(api_key, merchant_id)
```
### Methods
#### cancel_transaction
```python
'''
Void or partially void the reserved amount on a transaction
  - transactionId: String,      // required
  - amount: Decimal,            // If no amount is given, the full amount will be voided
'''
client.cancel_transaction(transaction_id, amount=None)
```
#### capture_transaction
```python
'''
Capture a transaction
  - transactionId: String,      // required
  - amount: Decimal,            // required
  - descriptor: String,         // optional, text on client bank statement
  - currency: String,           // optional, expected currency (for additional verification)
'''
client.capture_transaction(transaction_id, amount, descriptor='', currency=None)
```
#### create_payment_from_transaction
Make sure to read about [recurring payments](https://github.com/paylike/api-docs#recurring-payments).
```python
'''
Create a payment, based on an existing transaction (used for recurring payments)
  - transactionId: String,      // required
  - currency: String,           // required, three letter ISO
  - amount: Decimal,            // required, amount in minor units
  - descriptor: String,         // optional, the statement on the customers bankaccount. Will fallback to merchant descriptor
'''
client.create_payment_from_transaction(transaction_id, currency, amount, descriptor='')
```
#### create_payment_from_saved_card
Make sure to read about [recurring payments](https://github.com/paylike/api-docs#recurring-payments).
It's recommended to use create_payment_from_transaction
```python
'''
Create a payment from a saved card token
  - cardId: String,             // required
  - currency: String,           // required, three letter ISO
  - amount: Decimal,            // required
  - descriptor: String,         // optional, the statement on the customers bankaccount. Will fallback to merchant descriptor
'''
client.create_payment_from_saved_card(card_id, currency, amount, descriptor='')
```
#### get_transaction
```python
'''
Fetch a transaction
  - transactionId: String,      // required
'''
client.get_transaction(transaction_id)
```
#### get_transactions
```python
'''
Fetch transactions
  - limit: Number,              // optional, the number of transactions to fetch. Default 100
'''
client.get_transactions(limit=100)
```
#### refund_transaction
```python
'''
Refund, or partially refund a transaction
  - transactionId: String,      // required
  - amount: Decimal,            // required
  - descriptor: String,         // optional, the statement on the customers bankaccount. Will fallback to merchant descriptor
'''
client.refund_transaction(self, transaction_id, amount, descriptor="")

'''