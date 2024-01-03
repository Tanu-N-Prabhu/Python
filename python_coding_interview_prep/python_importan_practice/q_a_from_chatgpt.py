import openai
import time

# Set up OpenAI API key
openai.api_key = "key..."


# Define function to get response from OpenAI
def ask_gpt(prompt):
    response = openai.Completion.create(
        engine="davinci", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    return response.choices[0].text.strip()


# Define input and output file paths
input_file = "ml_questions_input.txt"
output_file = "ml_questions_output.txt"

# Open input and output files
with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    # Read lines from input file and send to OpenAI
    for line in f_in:
        prompt = line.strip()
        if prompt != "":
            response = ask_gpt(prompt)
            print(response)

            # Write response to output file
            f_out.write(response + "\n\n")

            # Wait for a few seconds before sending the next prompt (to avoid API rate limiting)
            time.sleep(3)
