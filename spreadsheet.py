
class SpreadSheet:

    def __init__(self):
        self._cells = {}

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        value = self._cells.get(cell, "")
        if value.startswith("="):
            if value[1:].startswith("'") and value[-1] == "'":
                return value[2:-1]
            try:
                # Check if it's a reference to another cell
                if value[1].isalpha():
                    referenced_value = self._cells.get(value[1:])
                    if referenced_value.isdigit():
                        return int(referenced_value)
                    elif referenced_value.startswith("'") and referenced_value.endswith("'"):
                        return referenced_value[1:-1]
                    elif referenced_value.startswith("="):
                        return self.evaluate(value[1:])
                    elif '.' in referenced_value:
                        return "#Error"
                    return referenced_value
                return int(value[1:])
            except ValueError:
                return "#Error"
        if value.startswith("'") and value.endswith("'"):
            return value[1:-1]
        try:
            return int(value)
        except ValueError:
            return "#Error"

