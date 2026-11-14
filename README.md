# Steaming Ramen — Best-Looking Food Picture

A bowl of ramen photographed like a magazine cover: rich glossy broth,
chopsticks lifting glistening noodles, a halved soft egg with a jammy
yolk, wisps of steam, warm side light against a dark moody background.

## What the program does

`main.py` copies the bundled `entry.png` to
`$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`).

## How to run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The output is a JPEG image (1024 × 683 px, ~130 KB) named `entry.png`,
within the competition limits (≤ 1 MiB, ≤ 1024 × 1024 px).

## License

MIT — see `LICENSE`.
