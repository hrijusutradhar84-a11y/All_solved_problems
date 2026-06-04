name: 🐛 Bug Report
description: Report a bug or incorrect solution
title: "[BUG] "
labels: ["bug", "needs-review"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        ## Thanks for reporting a bug! 🙏
        Please provide as much detail as possible to help us fix it.

  - type: textarea
    id: description
    attributes:
      label: 📝 Description
      description: Brief description of the bug or incorrect behavior
      placeholder: "Example: The two_sum solution returns wrong indices for negative numbers"
    validations:
      required: true

  - type: textarea
    id: problem-file
    attributes:
      label: 📁 Problem File
      description: Which file contains the bug?
      placeholder: "Example: array/two_sum.py"
    validations:
      required: true

  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: 🔄 Steps to Reproduce
      description: How can we reproduce this bug?
      placeholder: |
        1. Run the function with input: ...
        2. Expected output: ...
        3. Actual output: ...
    validations:
      required: true

  - type: textarea
    id: test-case
    attributes:
      label: 🧪 Test Case
      description: Provide a failing test case
      placeholder: |
        ```python
        >>> result = two_sum([-2, 7, 11, 15], 9)
        >>> print(result)
        # Got: []
        # Expected: [0, 1]
        ```
      render: markdown
    validations:
      required: true

  - type: textarea
    id: expected-behavior
    attributes:
      label: ✅ Expected Behavior
      description: What should happen instead?
      placeholder: "The function should return the correct indices regardless of input values"
    validations:
      required: true

  - type: textarea
    id: environment
    attributes:
      label: 🖥️ Environment
      description: Your environment details
      placeholder: |
        - Python version: 3.x
        - OS: Windows/Mac/Linux
        - How you ran the code: Direct execution/IDE/Other
      render: markdown

  - type: textarea
    id: additional-context
    attributes:
      label: 📌 Additional Context
      description: Any other information that might help
      placeholder: "Any error messages, stack traces, or screenshots"

  - type: checkboxes
    id: checklist
    attributes:
      label: ✓ Checklist
      options:
        - label: I have searched existing issues
          required: true
        - label: I have provided a minimal test case
          required: true
        - label: I have included the file path
          required: true
