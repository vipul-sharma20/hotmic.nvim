## hotmic.nvim

Neovim plugin for [hotmic][hotmic].

### Requirements

- Neovim with vim.pack (0.12+/nightly)
- A python3 with pynvim: python3 -m pip install --user pynvim
- The hotmic CLI: pip install git+https://github.com/vipul-sharma20/hotmic

### Install

```lua
vim.pack.add({
    { src = "https://github.com/vipul-sharma20/hotmic.nvim" },
})
```

Register the remote-plugin commands and restart:

```vim
:UpdateRemotePlugins
```

Remote-plugin manifests are only regenerated on demand. Re-run
`:UpdateRemotePlugins` after every plugin update (or wire the autocmd), then
restart Neovim.

#### Auto-regenerating the manifest

regenerate on install/update via `PackChanged`:

```lua
vim.api.nvim_create_autocmd("PackChanged", {
callback = function(ev)
  local d = ev.data
  if d.spec and d.spec.name == "hotmic.nvim"
     and (d.kind == "install" or d.kind == "update") then
    vim.schedule(function() vim.cmd("UpdateRemotePlugins") end)
  end
end,
})
```

If pynvim isn't on default python3, Neovim at an interpreter that has it (before the plugin loads)

```lua
vim.g.python3_host_prog = "/path/to/python3"
```

### Usage

Start the listener in a terminal (see [hotmic doc][hotmic]), then drive it from Neovim:

```vim
:HotmicMark <label>
:HotmicSaveDuration <minutes> <name>
:HotmicSaveBetweenMarks
:HotmicTranscribe <file>
:HotmicSummarize <file>
```


[hotmic]: https://github.com/vipul-sharma20/hotmic
