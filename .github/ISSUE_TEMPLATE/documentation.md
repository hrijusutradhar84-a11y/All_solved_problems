name: 📚 Documentation
description: Report missing or unclear documentation
title: "[DOCS] "
labels: ["documentation"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        ## Documentation Issue 📖
        Help us improve documentation and clarity!

  - type: textarea
    id: doc-issue
    attributes:
      label: 🤔 What's the issue?
      description: What documentation is missing or unclear?
      placeholder: "Example: The coin_change.py solution needs better explanation of the DP approach"
    validations:
      required: true

  - type: dropdown
    id: issue-type
    attributes:
      label: 📝 Issue Type
      description: What kind of documentation issue is this?
      options:
        - Select an option
        - Missing explanation
        - Unclear complexity analysis
        - Missing examples
        - Incorrect documentation
        - Better comments needed
        - README update needed
        - Other
    validations:
      required: true

  - type: textarea
    id: current-docs
    attributes:
      label: 📄 Current Documentation
      description: Quote the current documentation
      placeholder: "Current docstring or comment"

  - type: textarea
    id: suggested-improvement
    attributes:
      label: ✨ Suggested Improvement
      description: How should this be improved?
      placeholder: "Suggested text or explanation"
    validations:
      required: true

  - type: textarea
    id: rationale
    attributes:
      label: 💡 Why Is This Important?
      description: Explain why this documentation matters
      placeholder: "This will help learners understand the algorithm better"

  - type: checkboxes
    id: checklist
    attributes:
      label: ✓ Checklist
      options:
        - label: Issue is specific and actionable
          required: true
        - label: I have suggested a clear improvement
          required: true
