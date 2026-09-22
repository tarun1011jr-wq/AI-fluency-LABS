import re
from config import COURSE_FEES, QUESTIONS


def workflow(question):
    # Find course codes such as CS101, AI202, DS303
    courses = re.findall(r"\b[A-Z]{2}\d{3}\b", question.upper())

    # Q1: Single course fee
    if len(courses) == 1 and "fee" in question.lower():
        course = courses[0]

        if course in COURSE_FEES:
            return f"The fee for {course} is Rs. {COURSE_FEES[course]}."

    # Q2: Two courses + 10% scholarship
    if len(courses) == 2 and "total" in question.lower() and "10%" in question:
        fee1 = COURSE_FEES[courses[0]]
        fee2 = COURSE_FEES[courses[1]]

        total = fee1 + fee2
        final_fee = total * 0.90

        return f"After a 10% scholarship, the total fee is Rs. {final_fee:.0f}."

    # Q3: Compare two courses
    if len(courses) == 2 and "more expensive" in question.lower():
        fee1 = COURSE_FEES[courses[0]]
        fee2 = COURSE_FEES[courses[1]]

        difference = abs(fee1 - fee2)

        if fee1 > fee2:
            return f"{courses[0]} is more expensive by Rs. {difference}."
        elif fee2 > fee1:
            return f"{courses[1]} is more expensive by Rs. {difference}."
        else:
            return "Both courses have the same fee."

    # Q4 and unknown questions
    return "No workflow rule matches this question."


print("=" * 60)
print("SYSTEM 2 - RULE-BASED WORKFLOW")
print("=" * 60)

for i, question in enumerate(QUESTIONS, start=1):
    print(f"\nQ{i}: {question}")
    print("-" * 60)
    print("Answer:")
    print(workflow(question))