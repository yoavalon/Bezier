d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,3)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
