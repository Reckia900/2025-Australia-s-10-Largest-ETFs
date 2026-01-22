# Contributing Guidelines

## How to Contribute

We welcome contributions to the Financial Modelling System! Here are some ways you can help:

### Types of Contributions

1. **Bug Reports**: Report issues via GitHub Issues
2. **Feature Requests**: Suggest new features or improvements
3. **Code Contributions**: Submit pull requests with enhancements
4. **Documentation**: Improve or expand documentation
5. **Testing**: Add test cases or improve test coverage

### Development Setup

1. Fork the repository
2. Clone your fork: `git clone <your-fork-url>`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Install in development mode: `pip install -e ".[dev]"`
5. Make your changes
6. Run tests: `pytest tests/ -v`
7. Commit with clear messages
8. Push to your fork
9. Open a pull request

### Code Style

- Follow PEP 8
- Use type hints
- Write docstrings for functions and classes
- Run `black` and `isort` before committing

```bash
black financial_modelling/
isort financial_modelling/
```

### Testing Requirements

- Write tests for new features
- Maintain or improve code coverage
- All tests must pass before PR approval

### Pull Request Guidelines

- Clear description of changes
- Reference any related issues
- Include test cases
- Update documentation if needed
- Keep commits focused and clean

## Areas for Enhancement

### High Priority
- [ ] Real-time data streaming
- [ ] Additional optimization algorithms (genetic algorithm, particle swarm)
- [ ] Performance attribution analysis
- [ ] Factor analysis framework

### Medium Priority
- [ ] Machine learning predictions
- [ ] Multi-currency portfolio support
- [ ] Advanced risk models (GARCH, Jump-Diffusion)
- [ ] Backtesting framework

### Low Priority
- [ ] Historical scenario analysis
- [ ] Monte Carlo simulation enhancements
- [ ] Additional visualization types
- [ ] RESTful API for data access

## Code Review Process

1. Maintainers review all PRs
2. Feedback provided for any changes needed
3. Once approved, PR is merged
4. Thank you for contributing!

---

Thank you for helping improve the Financial Modelling System!
