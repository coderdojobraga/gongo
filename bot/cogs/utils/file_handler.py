import json


class FileHandler:
    """
    This is a class to handle a json file.

    Attributes:
        file (string): The path to the json file being handled.
    """

    file = "bot/data/belts.json"

    def __init__(self: str, belt: str):
        """
        The constructor for the FileHandler class.

        Parameters:
            color (int): Color code to be displayed in discord embed.
        """
        self.belt = belt
        self.msg = self.get_info()[0]
        self.color = self.get_info()[1]

    def get_info(self) -> tuple:
        """
        The function to get the info from the belts.json file.

        Returns:
            msg (string): Variable that contains the message of the respective belt.
            color (int): Color code to be displayed in discord embed.
        """
        with open(self.file) as json_file:
            data = json.load(json_file)
            msg = f"Subiste para {self.belt} :clap:\n\nPróximos objetivos:"
            color = int(data[self.belt]["color"], 16)
            for param in data[self.belt]["goals"]:
                msg += "\n" + param

            return (msg, color)
