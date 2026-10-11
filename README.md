# Digital Design and Computer Architecture

My record of working through Harris & Harris, *Digital Design and Computer Architecture*, cover to cover.

- Chapters 1–5: 2nd edition (2012, MIPS)
- Chapters 6–9: RISC-V edition (2021)
- Hardware practice: [HDLBits](https://hdlbits.01xz.net) and [EDA Playground](https://edaplayground.com). I write SystemVerilog and only read the VHDL.

The dated record of everything I did is in **[LOG.md](LOG.md)**. The commit history backs it up.

## Progress

| Ch | Title | Edition | Status |
|---|---|---|---|
| 1 | From Zero to One | 2nd | in progress |
| 2 | Combinational Logic Design | 2nd | |
| 3 | Sequential Logic Design | 2nd | |
| 4 | Hardware Description Languages | 2nd | |
| 5 | Digital Building Blocks | 2nd | |
| 6 | Architecture | RISC-V | |
| 7 | Microarchitecture | RISC-V | |
| 8 | Memory Systems | RISC-V | |
| 9 | Embedded I/O Systems | RISC-V | |

Book: `░░░░░░░░░` 0 / 9 chapters

## What's in here

| Folder | Contents |
|---|---|
| `notes/` | One file per chapter: key ideas in my own words |
| `exercises/` | End-of-chapter exercises I worked, one file per chapter |
| `hdlbits/` | My SystemVerilog solutions to HDLBits problems, grouped by HDLBits section |
| `LOG.md` | Dated log of every session |
| `log.py` | The script that writes to the log |

## Logging a session

From this folder, in PowerShell:

```
python log.py "Read 1.1-1.3, did exercises 1.1-1.5"
```

That adds a dated row to `LOG.md`, commits it, and pushes. Add `--local` to skip the push.
