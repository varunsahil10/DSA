# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Repository Overview

This is a Data Structures and Algorithms (DSA) practice repository containing Python solutions organized into Jupyter notebooks. The codebase follows a structured approach to problem-solving with implementations across various DSA topics including arrays, linked lists, trees, graphs, and algorithmic patterns.

## Common Development Commands

### Jupyter Notebook Operations
```bash
# Start Jupyter notebook server (if installed)
jupyter notebook

# Convert notebook to Python script
jupyter nbconvert --to python "filename.ipynb"

# Run a specific notebook cell-by-cell
jupyter nbconvert --execute --to notebook "filename.ipynb"
```

### Python Execution
```bash
# Run Python code directly
python3 script.py

# Execute a specific Python file extracted from notebook
python3 -c "exec(open('extracted_code.py').read())"
```

### Testing and Validation
```bash
# Run a specific solution with test input
python3 -c "
from solution_file import Solution
# Test with sample data
sol = Solution()
result = sol.method_name(test_input)
print(result)
"
```

## Architecture and Code Structure

### Repository Organization
- **Topic-based directories**: Each major DSA concept has its own directory (Lists, BST, Stack, Queue, etc.)
- **Difficulty segregation**: Problems are organized by difficulty levels (Easy, Medium, Hard) within topic directories, particularly following Striver's DSA sheet structure
- **Jupyter notebook format**: All solutions are contained in `.ipynb` files with embedded explanations and test cases

### Solution Pattern
Most solutions follow this consistent structure:
```python
class Solution:
    def methodName(self, params):
        # Algorithm implementation
        # Time complexity: O(...)  
        # Space complexity: O(...)
        pass

# Driver code with test cases usually included
# Input/output handling for competitive programming format
```

### Key Architectural Elements
- **Driver code integration**: Most notebooks include complete driver code templates compatible with competitive programming platforms
- **Multiple implementations**: Many problems include both optimal and brute force approaches with complexity analysis
- **Interactive development**: Code cells are designed for iterative testing and experimentation

### Problem Categories and Patterns
- **Arrays/Lists**: Fundamental operations, two-pointer techniques, sliding window, prefix sums
- **Trees**: BST operations, traversals (inorder, preorder, postorder, levelorder), tree construction
- **Graph algorithms**: Search algorithms, pathfinding, traversal patterns
- **Dynamic Programming**: Optimization problems with memoization and tabulation approaches
- **String manipulation**: Pattern matching, transformations, palindromes
- **Mathematical algorithms**: Number theory, combinatorics, geometric problems

### Coding Conventions
- Standard competitive programming input/output patterns
- Class-based solution structure with static method approach
- Comprehensive test case integration within notebooks
- Time and space complexity documentation in comments
- Edge case handling patterns (empty inputs, single elements, boundary conditions)

### Development Workflow
1. Problems are implemented in Jupyter notebooks for iterative development
2. Each notebook typically contains multiple approaches to the same problem
3. Driver code is included for immediate testing with sample inputs
4. Solutions follow competitive programming format for easy platform submission

## Working with This Repository

When implementing new solutions:
- Follow the existing class-based structure with Solution class
- Include comprehensive test cases within the notebook
- Document time and space complexity
- Provide both brute force and optimized approaches when applicable
- Use descriptive variable names that clarify the algorithm logic
- Include driver code compatible with competitive programming platforms

When debugging:
- Use the interactive nature of Jupyter notebooks to test individual components
- Leverage the existing test cases to validate solutions
- Check edge cases systematically using the provided templates

The repository structure makes it easy to locate specific problem types and patterns, enabling efficient practice and reference during problem-solving sessions.