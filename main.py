from venmo_api import Client, AuthenticationApi
from discordwebhook import Discord
import datetime

current_date = datetime.date.today()
current_month_name = current_date.strftime("%B").lower()

# input webhook url
discord = Discord(url=)

requests = []



# Initialize api client using an access-token
client = Client(access_token)


friends = [
    {
        "username": "friend1",
        "id": "12345",
        "amount": 0
    } ,   
    {
        "username": "friend2",
        "id": "54321",
        "amount:": 0
    },
    {
        "username": "friend3",
        "id": "67890",
        "amount:": 0
    }
]




for friend in friends:
    name = friend["username"]
    id = friend["id"]
    desc = "test " + current_month_name
    amount = friend["amount"]

    success = client.payment.request_money(amount, desc, id)

    if success:
        requests.append(success)
        discord.post(
            embeds=[{"title": "Successful Venmo Request! ✅", "description": f"Requested ${amount} from @{name} for '{desc}'"}]
        )
    else:
        discord.post(
            embeds=[{"title": "Failed Venmo Request! ❌", "description": f"Unable to request ${amount} from @{name} for '{desc}'"}]
        )

