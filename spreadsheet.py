
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
                        if '.' in referenced_value:
                            result = "#Error"
                        else:
                            result = self.evaluate(referenced_cell)
                    else:
                        # Evaluate arithmetic expressions
                        expression = value[1:]
                        result = eval(expression, {'__builtins__': None}, {})
                        if isinstance(result, float) and not result.is_integer():
                            result = "#Error"
                        elif isinstance(result, float) and result.is_integer():
                            result = int(result)
                except:
                    result = "#Error"
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        else:
            try:
                result = int(value)
            except ValueError:
                try:
                    result = float(value)
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = "#Error"
                except ValueError:
                    result = "#Error"
        
        self._evaluating.remove(cell)
        return result

