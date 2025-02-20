def function_with_closed_file(filename):
    try:
        with open(filename, 'w') as f:
            # ... code that might raise an exception ...
            f.write('This will be written to the file.')
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("File closed successfully.") # ensure this always executes, even if exception occurs
