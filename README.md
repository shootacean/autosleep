# AutoSleep

## TODO

- [/] Output Markdown format
- [ ] 年初から現在までの達成率
- [ ] 月毎の達成率
- [x] Setup Formatter ( Black )
- [x] Setup Linter ( Ruff )
- [ ] Setup SAST ( Bandit )
- [ ] Setup DAST
- [ ] Setup Snyk
- [x] Setup TDD ( pytest )

## Usage

```shell
rye run python src/main.py
```

## Markdown Layout

```markdown
# AutoSleep <start date> - <end date>

> [!summary] xx % ( yy / zz )

> [!success] Streaks : n days !!!

## Monthly

- 2024-01 : xx % ( yy / zz )
- 2024-02 : xx % ( yy / zz )
- 2024-03 : xx % ( yy / zz )
- ...

```
