from pythonosc import udp_client
import re

def is_valid_avatar_id(avatar_id: str) -> bool:
    pattern = r"^avtr_[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"
    return bool(re.match(pattern, avatar_id))

def main():
    ip = "127.0.0.1"
    port = 9000
    client = udp_client.SimpleUDPClient(ip, port)

    while True:
        user_input = input("Avatar IDまたはURLを入力してください: ").strip()
        if user_input == "":
            exit()

        pattern = re.compile(r'vrchat.com/home/avatar/([^/?#]+)')
        match = pattern.search(user_input)
        if match:
            avatar_id = match.group(1)
        else:
            avatar_id = user_input

        if is_valid_avatar_id(avatar_id):
            client.send_message("/avatar/change", avatar_id)
            print(f"アバターを{avatar_id}に変更しました")
        else:
            print("アバター IDが無効です")
        print()

if __name__ == '__main__':
    main()
