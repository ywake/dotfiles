# Agent
- Think in English.
- Respond in Japanese.
- Use Japanese for documentation/comments.
- use `serena` mcp
- Tests do not work well in the sandbox, so please ask me to run them.
- In python, write a docstring for each function and class.
	- Google style.
	- title, summary, args, returns, raises.
	```python
	def test_function(arg1: int, arg2: str) -> bool:
		"""テスト関数

		この関数はコードの機能をテストします。

		Args:
			arg1(int): 最初の引数
			arg2(str): 第二の引数

		Returns:
			bool: 関数が成功した場合はTrue, それ以外はFalse

		Raises:
			ValueError: arg1が整数でない場合
			TypeError: arg2が文字列でない場合
		"""
		...
	```
- Add comments to each step in tests to clarify what is being tested.
- For simple read/write operations, do not execute them with code such as Python.

# Core Rules
You have two operating modes:
1. Plan Mode
	- Work with the user to define an implementation plan
	- Autonomously gather necessary information and compile the implementation plan
	- Do not make any changes
	- For responses to questions and other cases that do not involve changes, use Plan Mode
2. Act Mode
	- Make changes to the codebase based on the plan
- Start in Plan Mode and do not transition to Act Mode until the user approves the plan.
- At the beginning of each response, display `# Mode: PLAN` for Plan Mode or `# Mode: ACT` for Act Mode.
- Remain in Plan Mode unless the user explicitly requests transition to Act Mode by typing `ACT`.
- Return to Plan Mode after each response and when the user types `PLAN`.
- If the user requests an action while in Plan Mode, inform them that you are in Plan Mode and that they need to approve the plan first.
- In Plan Mode, output the complete updated plan with every response.
- In Plan Mode, gather information about the current state before proposing a plan.
