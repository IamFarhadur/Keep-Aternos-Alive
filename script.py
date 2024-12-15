from mcstatus import MinecraftServer
import time

# Replace this with your Aternos server's address
server_address = "Name_Ki_Dimu.aternos.me"

def keep_server_alive():
    while True:
        try:
            # Check server status
            server = MinecraftServer.lookup(server_address)
            status = server.status()
            print(f"Server is online with {status.players.online} players.")
        except Exception as e:
            print(f"Failed to reach the server: {e}")
        
        time.sleep(300)

if __name__ == "__main__":
    print(f"Starting server monitoring for {server_address}...")
    keep_server_alive()
