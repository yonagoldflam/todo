import requests

class Request:
    def __init__(self, base_url):
        self.base_url = base_url

    def new_todo(self, todo: dict[str, str]):
        response = requests.post(f"{self.base_url}/todo", json=todo)
        print(response.status_code)
        print(response.text)

    def get_all_todos(self):
        response = requests.get(f"{self.base_url}/todos")
        print(response.status_code)
        print(response.text)

    def delete_todo(self, id: str):
        response = requests.delete(f"{self.base_url}/delete", params={"id": id})
        print(response.status_code)
        print(response.text)

class Menu:
    def __init__(self):
        base_url = "http://localhost:8000"
        self.request = Request(base_url)

    def menu(self):
        flag = True
        while flag:
            match input('1. get all \n2. insert todo \n3. delete todo \n'):
                case '1':
                    self.request.get_all_todos()

                case '2':
                    id = input('enter id: ')
                    todo = input('enter todo: ')
                    self.request.new_todo({'id':id, 'todo':todo})

                case '3':
                    id = input('enter id to delete: ')
                    self.request.delete_todo(id)

                case _:
                    flag = False

menu = Menu()
if __name__ == '__main__':
    menu.menu()