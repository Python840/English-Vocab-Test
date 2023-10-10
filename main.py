import tkinter as tk

vocab = {
    # Data goes here in the format "key (german word): value (english word), both are strings and don't forget the comma! Example:
    "sehr interessiert, begeistert": "keen",
    "apartheid": "apartheid"
    # ...
}

class VocabularyTest:
    def __init__(self, root):
        self.root = root
        self.root.title("English Vocabulary Test")

        self.score = 0
        self.current_index = 0

        self.label = tk.Label(root, text="", font=("Arial", 12))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack()

        self.button = tk.Button(root, text="Submit", command=self.check_answer)
        self.button.pack(pady=10)

        self.display_question()

    def display_question(self):
        if self.current_index < len(vocab):
            german_word = list(vocab.keys())[self.current_index]
            self.label.config(text=f"What is the English translation of '{german_word}'? ")
            self.entry.pack()  # Show entry field
            self.button.pack()  # Show submit button
        else:
            self.show_result()

    def check_answer(self):
        if self.current_index < len(vocab):
            english_translation = vocab[list(vocab.keys())[self.current_index]]
            user_answer = self.entry.get().strip().lower()

            if user_answer in english_translation.lower():
                self.score += 1

            self.current_index += 1
            self.entry.delete(0, "end")
            self.display_question()
        else:
            self.show_result()

    def show_result(self):
        self.label.config(text=f"Test completed.\nYou scored {self.score} out of {len(vocab)}.")
        self.entry.pack_forget()  # Hide entry field
        self.button.pack_forget()  # Hide submit button

if __name__ == "__main__":
    root = tk.Tk()
    app = VocabularyTest(root)
    root.mainloop()
