"""bitahub_test."""

from tmux_bitahub import get_result  # type: ignore


class Test:
    """Test."""

    def test_get_result(self):
        """Test get_result."""
        with open("assets/html/debug.html") as f:
            html = f.read()
        result = get_result(html)
        assert result == (
            "#[fg=black]8:#[fg=red]0 #[fg=black]7:#[fg=red]0 "
            "#[fg=black]6:#[fg=green]1 #[fg=black]5:#[fg=red]0 "
            "#[fg=black]4:#[fg=green]1 #[fg=black]3:#[fg=green]2 "
            "#[fg=black]2:#[fg=red]0 #[fg=black]1:#[fg=red]0#[fg=default]"
        )
