from booknlp.booknlp import BookNLP

print("Initializing BookNLP with small model...")

model_params = {
    "pipeline": "entity,quote,supersense,event,coref", 
    "model": "small"
}

booknlp = BookNLP("en", model_params)

# Input file to process
input_file = "158_emma.txt"

# Output directory to store resulting files in
output_directory = "test_output"

# File within this directory will be named ${book_id}.entities, ${book_id}.tokens, etc.
book_id = "emma_test"

print(f"Processing {input_file}...")
print(f"Output will be saved to {output_directory}/")

booknlp.process(input_file, output_directory, book_id)

print("BookNLP processing completed successfully!") 