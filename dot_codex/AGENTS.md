# Agent
- Lanuage
  - Think & respond in Japanese.
  - Use Japanese for documentation/comments.
- use `serena` mcp
- Markdownの記法を適材適所に幅広く使うことでわかりやすく伝えてください
- 特に指示がなければ、変更のコスト最小化よりも長期運用の自然さを重視した変更を主にしてください。

# Coding
- Add comments for each logical block in all code. For implementation code, explain the logic and intent. For tests, clarify what is being tested.

# Python
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