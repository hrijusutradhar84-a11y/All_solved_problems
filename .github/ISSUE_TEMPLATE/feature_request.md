name: 🚀 Improvement
description: Suggest improvements to existing solutions
title: "[IMPROVEMENT] "
labels: ["improvement", "optimization"]
assignees: []

body:
  - type: markdown
    attributes:
      value: |
        ## Improvement Suggestion 🎯
        Help us optimize or improve existing solutions!

  - type: textarea
    id: problem-file
    attributes:
      label: 📁 Problem File
      description: Which file would you like to improve?
      placeholder: "Example: array/two_sum.py"
    validations:
      required: true

  - type: dropdown
    id: improvement-type
    attributes:
      label: 🔧 Type of Improvement
      description: What type of improvement are you suggesting?
      options:
        - Select an option
        - Performance Optimization
        - Memory Optimization
        - Code Readability
        - Better Documentation
        - Additional Test Cases
        - Alternative Approach
        - Edge Case Handling
        - Other
    validations:
      required: true

  - type: textarea
    id: current-code
    attributes:
      label: 📝 Current Code
      description: Show the current implementation
      placeholder: |
        ```python
        def two_sum(nums, target):
            # current implementation
        ```
      render: markdown

  - type: textarea
    id: proposed-improvement
    attributes:
      label: ✨ Proposed Improvement
      description: Describe your suggested improvement
      placeholder: |
        ```python
        def two_sum(nums, target):
            # improved implementation
        ```
      render: markdown
    validations:
      required: true

  - type: textarea
    id: benefits
    attributes:
      label: 💪 Benefits
      description: What benefits does this improvement provide?
      placeholder: |
        - Faster execution (from O(n²) to O(n))
        - Clearer code
        - Handles edge cases better
    validations:
      required: true

  - type: textarea
    id: complexity-comparison
    attributes:
      label: 📊 Complexity Comparison
      description: Compare time and space complexity
      placeholder: |
        Current:
        - Time: O(n²)
        - Space: O(1)
        
        Proposed:
        - Time: O(n)
        - Space: O(n)

  - type: textarea
    id: benchmark
    attributes:
      label: ⏱️ Performance Benchmark (Optional)
      description: Any performance measurements?
      placeholder: "Show timing comparisons if available"

  - type: checkboxes
    id: checklist
    attributes:
      label: ✓ Checklist
      options:
        - label: I have tested the proposed improvement
          required: false
        - label: I have provided complexity analysis
          required: true
        - label: I have shown the benefits clearly
          required: true
