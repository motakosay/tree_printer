![Directory tree.svg](https://visualpharm.com/assets/705/Folder%20Tree-595b40b65ba036ed117d40de.svg)

# TreePrinter
---

## Features

- **Hidden File Filtering**  
  Skips over system clutter like `.DS_Store`, `.git`, or other dotfiles — keeping the output clean and intentional.

- **Depth Control**  
  Optional `--depth` flag lets you limit how deep the tree grows, ideal for focusing on top-level structure or avoiding overwhelming detail.

- **Color-Coded Output**  
  Uses `colorama` to distinguish folders (blue) and files (green), making the tree easier to read and more visually expressive in terminal environments.

- **Unicode Tree Drawing**  
  Renders the hierarchy using `├─`, `└─`, and `│` characters for a familiar and elegant tree layout.

---

## Usage

```bash
python tree_printer.py /path/to/folder --depth 3
