
class SpreadSheet:
    def __init__(self):
        self._cells = {}
        self._evaluating = set()  # To track cells currently being evaluated

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def evaluate(self, cell: str):
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self._cells.get(cell, "")
        if value.startswith("="):
            if value[1:].startswith("'") and value[-1] == "'":
                result = value[2:-1]
            else:
                try:
                    # Check if it's a reference to another cell
                    if value[1].isalpha():
                        referenced_cell = value[1:]
                        referenced_value = self._cells.get(referenced_cell, "")
                        result = self.evaluate(referenced_cell)
                    else:
                        result = int(value[1:])
                except ValueError:
                    result = "#Error"
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        else:
            try:
                result = int(value)
            except ValueError:
                result = "#Error"
        
        self._evaluating.remove(cell)
        return result

