from LLM import llm

def main():
    LLM = llm()

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit']:
            print('goodbye')
            break

if __name__ == '__main__':
    main()