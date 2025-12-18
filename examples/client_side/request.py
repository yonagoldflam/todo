import requests


class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def new_user(self, username_password: dict[str, str]) -> None:
        response = requests.post(f"{self.base_url}/users", json=username_password)
        print(f"{response.status_code}")
        print(f"{response.json()}")

    def get_token(self, username_password: dict[str, str]) -> str:
        response = requests.post(f"{self.base_url}/users/login", json=username_password)
        print(response.status_code)
        print(response.json())
        token = response.json().get('access_token')
        return token

    def new_todo(self, todo: dict[str, str], token: str) -> None:
        response = requests.post(f"{self.base_url}/todos", json=todo, headers={'Authorization': f'Bearer {token}'})
        print(f"{response.status_code} \n{response.json()}")

    def get_all_todos(self, token: str) -> None:
        response = requests.get(f"{self.base_url}/todos", headers={'Authorization': f'Bearer {token}'})
        print(f'{response.status_code} \n{response.text}')

    def delete_todo(self, id: str, token: str) -> None:
        response = requests.delete(f"{self.base_url}/todos/{id}",
                                   headers={'Authorization': f'Bearer {token}'})
        print(response.status_code)
        print(response.json())


class Menu:
    def __init__(self):
        base_url = "http://localhost:8000"
        self.request = Request(base_url)
        self.current_token = None

    def menu(self):
        flag = True
        while flag:
            match input('1. insert new user \n2. login\n'):

                case '1':
                    username = input('enter new username: ')
                    password = input('enter new password: ')
                    self.request.new_user({'username': username, 'password': password})

                case '2':
                    username = input('enter your username: ')
                    password = input('enter your password: ')
                    self.current_token = self.request.get_token({'username': username, 'password': password})

                    dip_flag = True
                    while dip_flag:
                        match input('1. get all \n'
                                    '2. insert todo \n'
                                    '3. delete todo \n'
                                    '4. back to login \n'
                                    'any key. exit: '):
                            case '1':
                                self.request.get_all_todos(self.current_token)

                            case '2':
                                todo = input('enter todo: ')
                                due_date = input('enter date day/month/year houer:minuts: ')
                                self.request.new_todo({'todo': todo, 'due_date': due_date}, self.current_token)

                            case '3':
                                id = input('enter id to delete: ')
                                self.request.delete_todo(id, self.current_token)

                            case '4':
                                dip_flag = False

                            case _:
                                dip_flag = False
                                flag = False

                case _:
                    flag = False


menu = Menu()
if __name__ == '__main__':
    menu.menu()

"25/01/2025 12:13"
