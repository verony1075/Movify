import openai
import os
import time
import re

openai.api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=openai.api_key)

def ask_ai(prompt):
    max_retries = 5
    retry_delay = 1

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Use the appropriate model
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,  # Increase token limit for longer responses
                n=1,
                temperature=0.5,
            )
            return response.choices[0].message['content'].strip()
        except Exception as e:
            if "rate limit" in str(e).lower():
                if attempt < max_retries - 1:
                    time.sleep(retry_delay)
                    retry_delay *= 2  # exponential backoff
                else:
                    return f"Rate limit exceeded: {str(e)}"
            elif "invalid request" in str(e).lower():
                return f"Invalid request: {str(e)}"
            elif "authentication" in str(e).lower():
                return f"Authentication failed: {str(e)}"
            else:
                return f"API error: {str(e)}"

def get_movie_recommendation(movies, ratings, genre, age_rating, year_range):
    prompt = (
        f"Using this list of films watched by a user: {movies} and the ratings out of 5 they gave these films: {ratings}, "
        f"can you give a movie recommendation? The user prefers {genre} genre, with an age rating of {age_rating}, "
        f"and movies released in the years {year_range} inclusive. "
        f"Please only output a numbered list of 5 movies and a sentence-long plot summary for each."
    )
    return ask_ai(prompt)

def get_trivia(films):
    prompt = (
        f"From this film watched by a user: {films}, take the film "
        f"and generate 5 movie trivia questions based on that film with the answer posed as multiple choice questions "
        f"and include only 3 answers to choose from."
    )
    return ask_ai(prompt)

def parse_trivia_response(response):
    """
    Parses the trivia response to extract a list of questions, posed answers, and correct answers.
    """
    lines = response.strip().split('\n')

    trivia_data = []
    question = None
    posed_answers = []
    correct_answer = None

    for line in lines:
        line = line.strip()
        if re.match(r'^\d+\.', line):
            # If there's already a question, save the previous question's data
            if question is not None and correct_answer is not None:
                trivia_data.append({
                    'question': question,
                    'posed_answers': posed_answers,
                    'correct_answer': correct_answer
                })

            # Start a new question
            question = line
            posed_answers = []
            correct_answer = None  # Reset correct_answer for the new question
        elif line.startswith('Answer:'):
            correct_answer = line.split('Answer:')[1].strip()
        else:
            posed_answers.append(line)

    # Add the last question
    if question is not None and correct_answer is not None:
        trivia_data.append({
            'question': question,
            'posed_answers': posed_answers,
            'correct_answer': correct_answer
        })

    return trivia_data

def ask_trivia_questions(trivia_data_list):
    """
    Asks a list of trivia questions, validates the user's answers, and tracks the score.
    """
    score = 0
    for trivia_data in trivia_data_list:
        print(f"{trivia_data['question']}\n")

        for answer in trivia_data['posed_answers']:
            print(answer)

        user_answer = input("\nYour answer (e.g., A, B, C): ").strip().upper()
        correct_answer_letter = trivia_data['correct_answer'].split(' ')[0]

        if user_answer in correct_answer_letter:
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, that's incorrect. The correct answer was {trivia_data['correct_answer']}.\n")

    print(f"\nYour final score is {score}/{len(trivia_data_list)}\n")

def start_trivia(films):
    gpt_response = get_trivia(films)
    parsed_questions = parse_trivia_response(gpt_response)
    return parsed_questions

def evaluate_trivia_answers(user_answers, trivia_data_list):
    score = 0
    for i, trivia_data in enumerate(trivia_data_list):
        correct_answer_letter = trivia_data['correct_answer'].split(' ')[0]
        user_answer = user_answers.get(f'answer_{i}')
        if user_answer and user_answer == correct_answer_letter:
            score += 1

    return score, len(trivia_data_list)
