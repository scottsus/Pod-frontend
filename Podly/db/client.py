import os
from dotenv import load_dotenv
from supabase import create_client, Client

class Client:
    def __init__(self):
        self.table_name = "Podcasts"

        load_dotenv()
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        self.client: Client = create_client(url, key)
    
    def fetch_data(self):
        res = self.client.table(self.table_name).select("*").execute()
        data = res.data

        DEBUG_MODE = False
        if DEBUG_MODE == True:
            import json
            pretty = json.dumps(data, indent=4, sort_keys=True)
            print(pretty)

        return data

cli = Client()
