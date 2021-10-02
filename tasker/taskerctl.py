import fire
import yaml

class TaskerCli:
    def __init__(self, uppath):

        with open("example.yaml", "r") as stream:
            try:
                print(yaml.safe_load(stream))
            except yaml.YAMLError as exc:
                print(exc)

    def list_tasks(self):

if __name__ == '__main__':
    fire.Fire()
