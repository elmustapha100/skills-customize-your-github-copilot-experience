---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency, clarity, and learning-focused design for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

All assignment markdown files must follow these guidelines to maintain consistency across the educational portal and provide students with clear, actionable assignments.

## 1. Template Usage

- Assignment markdown files **must** follow the structure defined in [`templates/assignment-template.md`](../../templates/assignment-template.md)
- Each assignment must be created as a `README.md` file within its own folder
- Do not remove, skip, or reorder required sections from the template
- Preserve all emoji icons exactly as shown in the template

## 2. Section Structure and Guidance

### Title: 📘 Assignment: [Title]

- Replace `[Assignment Title]` with a concise, descriptive assignment name
- Examples: `Python Basics`, `Hangman Game Challenge`, `Data Analysis`, `Python Classes`
- Keep titles clear and engaging for students

### Objective: 🎯

- Write 1-2 sentences summarizing what students will learn or accomplish
- Focus on the **skills and concepts** students will practice, not just the deliverable
- Example: "Practice fundamental Python programming skills including user input, string formatting, arithmetic operations, and conditional statements by implementing simple functions."
- Include a list of skills practiced (e.g., "String manipulation, loops, conditionals, random selection")

### Tasks: 📝

Structure each task with consistent formatting:

#### Task Header: 🛠️ [Task Name]

Use action-oriented, specific task names that describe what the student will do.

**Description** subsection:
- Clearly state what the student must do to complete the task
- Be specific about expected outputs or behaviors
- Keep language concise and student-friendly

**Requirements** subsection:
- Always start with the phrase: "Completed program should:"
- Use bullet points to list expected outcomes or features
- Make requirements specific and **measurable** where possible
- Include example input/output in code blocks when helpful for clarity
- Ensure requirements are concrete and actionable

### Example Task Format

```markdown
### 🛠️ User Input and String Formatting

#### Description
Write a function called `welcome_message()` that interacts with the user and returns a formatted welcome message.

#### Requirements
Completed program should:

- Ask the user for their name, age, and favorite color using `input()`.
- Return a welcome message formatted as: `Hello, [name]! You are [age] years old and your favorite color is [color].`
- Example output: `Hello, Alice! You are 25 years old and your favorite color is blue.`
```

## 3. Content Guidelines

### Learning-Focused Design
- All content should have clear learning objectives
- Assignments should build skills progressively
- Include difficulty hints or prerequisite knowledge if applicable

### Student-Friendly Language
- Use clear, encouraging, and motivating language
- Avoid overly technical jargon without explanation
- Use inclusive language that welcomes all skill levels

### Requirements Clarity
- Each requirement should be testable and verifiable
- Avoid vague terms like "nice to have" or "extra credit" in Requirements sections
- If including optional enhancements, create a separate section or clearly mark them

## 4. Do Not Include

- Extra sections not in the template (no "Additional Resources", "Hints", or "Bonus Challenges" unless explicitly specified)
- Decorative content that doesn't contribute to learning objectives
- Overly long descriptions that distract from the core task
