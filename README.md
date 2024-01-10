The Legacy Modding wiki aims to be a comprehensive resource about creating mods for old versions of Minecraft. Currently it mainly focuses on Forge mod development for 1.7.10.

The wiki can be browsed **[here](https://legacymoddingmc.github.io/wiki/)**.

## Contributing

It's possible to contribute by simply editing the markdown files in the `docs` directory. The index page is at [docs/index.md](docs/index.md).

We use a custom markdown extension for rendering favicon links in the "list of mod forks" pages. The documentation for this can be found at [markdown_extensions/README.md](markdown_extensions/README.md).

### Testing

To test changes, it may be desirable to set up a local mkdocs server:

```
pip install mkdocs
python -m mkdocs serve
```

> Note: The use of `python -m` is deliberate. It puts our custom extension on the PYTHONPATH, unlike `mkdocs serve`, which doesn't work as a result.

The wiki will be browsable at [http://localhost:8000/](http://localhost:8000/) with live reloading.

## License

The wiki's contents are available under [Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/).
