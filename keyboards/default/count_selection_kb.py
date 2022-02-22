from keyboards.constructors import DefaultSelectionKeyboard, DefaultSelectionKeyboardItem


available_numbers = [1, 3, 6, 9]
count_selection_kb = DefaultSelectionKeyboard(
    [
        [DefaultSelectionKeyboardItem(str(number), number) for number in available_numbers]
    ]
)
