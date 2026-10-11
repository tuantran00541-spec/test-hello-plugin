"""Test plugin for harness remote-install test."""
def greet(name="world"):
    return f"Hello, {name}! (from remote plugin)"
PLUGIN_INFO = {"name": "hello-plugin", "version": "0.1.0"}
