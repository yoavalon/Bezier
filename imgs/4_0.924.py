d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.position_pen(0,0)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.medium)

d.end()
