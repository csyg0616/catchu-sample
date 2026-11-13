import pytest
from todo import TodoList

def test_add_and_complete():
    todos = TodoList()
    todos.add("장보기")
    todos.complete(0)
    assert todos.items[0]["done"] is True

def test_empty_title_rejected():
    with pytest.raises(ValueError):
        TodoList().add("   ")

def test_remaining_and_clear_done():
    todos = TodoList()
    todos.add("장보기")
    todos.add("운동")
    todos.complete(0)
    assert todos.remaining() == 1
    todos.clear_done()
    assert [item["title"] for item in todos.items] == ["운동"]
