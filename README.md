# RBC Agent

This project involves building an agent to play Reconnaissance Blind Chess (RBC). The main focus is not only on playing proficient chess moves but also on addressing the challenge posed by partial observability within the domain. 

## Getting Started

1. **Read the Documentation**: Start by reading the documentation available [here](https://reconchess.readthedocs.io/en/latest/). This documentation provides essential information about Reconnaissance Blind Chess and its implementation.

2. **Install Dependencies**: Install the Python package required for the project. You can find the installation instructions in the documentation mentioned above.

3. **Example Bot**: Begin with the Trout bot example provided in the documentation. This bot will serve as the foundation for your agent.

4. **Play a Game**: Follow the instructions [here](https://reconchess.readthedocs.io/en/latest/bot_play.html) to play a game between your Trout bot and a random agent.

## Project Requirements

Your task is to create an agent that plays Reconnaissance Blind Chess according to the following specifications:

- **Board Representation**: Implement a system to track all possible board configurations considering the uncertainty about the opponent's pieces.

- **Move Execution**: Develop functionality to execute moves within the game.

- **Next Move Prediction**: Predict the next move based on the current board state.

- **Next State Prediction**: Predict the next state of the game.

- **Next State Prediction with Captures**: Enhance the prediction mechanism to handle captures.

- **Next State Prediction with Sensing**: Implement sensing to refine the list of possible board states.

- **Move Generation**: Generate valid moves for the agent.

- **Multiple Move Generation**: Extend move generation to handle multiple possible moves.

## Strategy

Your agent should employ the following strategy:

- **Sensing Move**: When making a sensing move, select a square uniformly at random to gather information about the opponent's pieces.

- **Whittling Down Possible Boards**: Utilize sensing information to narrow down the list of possible board configurations.

- **Move Selection**: Run Stockfish on all potential board states to determine the most popular move suggested by Stockfish across all boards. In case of ties, select a move randomly.


## DEBUGING
- if you get `ModuleNotFoundError: No module named 'pkg_resources'` then `pip install setuptools`

## References

For further details, you can refer to the paper by Perrotta et al. (2022) available [here](https://proceedings.mlr.press/v176/perrotta22a.html). This paper discusses existing attempts to play Reconnaissance Blind Chess.