# How to use L2 Auth

- Create a `.env` file considering `.env.example`
- Install the `requirements.txt`
- Run the script `app.py`

Expected payload (it might include rewards results):

```
https://clob.polymarket.com/rewards/user?date=2024-04-10&signature_type=1
{'limit': 200, 'count': 0, 'next_cursor': 'LTE=', 'data': []}
```
