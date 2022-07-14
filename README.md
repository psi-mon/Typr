# Typr
Simple terminal typing programm to check out python finally ;)

## Notes

### Debugging
```lua

-- Debug Specific Keybinding
keymap("n","<F5>","<cmd>call vimspector#Continue()<cr>",opts)
keymap("n","<F4>","<cmd>call vimspector#Launch()<cr>",opts)
keymap("n","<F3>","<cmd>call vimspector#Stop()<cr>",opts)
keymap("n","<F2>","<cmd>VimspectorReset<cr>",opts)
keymap("n","<F9>","<cmd>call vimspector#StepOver()<cr>",opts) --Step Over
keymap("n","<F10>","<cmd>call vimspector#StepOver()<cr>",opts) --Step Into
keymap("n","<F6>","<cmd>call vimspector#ToggleBreakpoint()<cr>",opts) --Toggle Breakpoint
keymap("n","<F8>","<Plug>VimspectorBalloonEval<cr>",term_opts)

```
#### Remote Debugging

- `python -m debugpy --listen 5678 --wait-for-client main.py` 
- `<F5>`
