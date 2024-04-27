def calculate_cost(params):
    """
    Calculates the cost for using ChatGPT for a dynamic assignment application in a school.

    Parameters:
    params (dict): A dictionary containing parameters for the cost calculation.

    Returns:
    float: The total cost of the assignment application.

    Explanation:
    - Extract parameters from the input dictionary.
    - Calculate the number of tokens based on the number of words (assuming 750 words per 1000 tokens).
    - Define costs for different models, fine-tuning, and embedding.
    - Determine the model to be used, considering fine-tuning and embedding.
    - Calculate the cost based on the chosen model, fine-tuning, embedding, number of students, and assignment subjects.
    - Return the total cost.
    """
    words = params["words"]
    tokens = words * 1.25  # Assuming 750 words per 1000 tokens
    model = params["model"]  # Which model to use
    fine_tuning = params["fine_tuning"]  # Fine-tuning required or not
    embed_model = params["embed_model"]  # For embedding model
    students = params["students"]
    assignment_sub_count = params["assignment_sub_count"]

    # Costs for different models
    models = {
        "gpt4": {"8k": 0.03, "32k": 0.06},
        "chatgpt": {"8k": 0.002, "32k": 0.002},
        "instructgpt": {
            "8k": {"ada": 0.0004, "babbage": 0.0005, "curie": 0.0020, "davinci": 0.0200},
            "32k": {"ada": 0.0004, "babbage": 0.0005, "curie": 0.0020, "davinci": 0.0200},
        },
    }

    # Fine-tuning costs
    fine_tuning_cost = {
        "ada": {"training": 0.0004, "usage": 0.0016},
        "babbage": {"training": 0.0006, "usage": 0.0024},
        "curie": {"training": 0.0030, "usage": 0.0120},
        "davinci": {"training": 0.0300, "usage": 0.120},
    }

    # Embedding model costs
    embedding_model = {"ada": 0.0004, "babbage": 0.005, "curie": 0.020, "davinci": 0.20}

    total_cost = 0.0

    instructgpt_models = ["ada", "babbage", "curie", "davinci"]
    if model in instructgpt_models:
        sub_model = model
        model = "instructgpt"

    if model == "instructgpt":
        if tokens > 32000:
            price_model = models[model]["32k"].get(sub_model, {})
        else:
            price_model = models[model]["8k"].get(sub_model, {})
    else:
        if tokens > 32000:
            price_model = models[model]["32k"]
        else:
            price_model = models[model]["8k"]

    if fine_tuning:
        total_cost += (tokens * fine_tuning_cost[sub_model]["training"]) + (
            tokens * fine_tuning_cost[sub_model]["usage"]
        )

    if embed_model:
        total_cost += tokens * embedding_model[sub_model]

    total_cost += price_model * students * assignment_sub_count

    return total_cost


params = {
    "words": 10000,
    "model": "ada",
    "fine_tuning": True,
    "embed_model": "ada",
    "students": 200,
    "assignment_sub_count": 8,
}

print(params)

cost = calculate_cost(params)
print(
    f"The total cost of using ChatGPT for an assignment application with {params['students']} students and {params['assignment_sub_count']} subjects is: ${cost:.2f}"
)
