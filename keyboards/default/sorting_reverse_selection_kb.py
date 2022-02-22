from keyboards.constructors import DefaultSelectionKeyboard, DefaultSelectionKeyboardItem


sorting_reverse_selection_kb = DefaultSelectionKeyboard(
    [
        [
            DefaultSelectionKeyboardItem(
                text='Цена по возрастанию ⬆️',
                value=False
            ),
            DefaultSelectionKeyboardItem(
                text='Цена по убыванию ⬇️',
                value=True
            )
        ]
    ]
)
