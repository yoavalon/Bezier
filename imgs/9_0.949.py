d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,2)
d.curve(Direction.N, Orient.left, Length.short, Radius.medium)

d.end()
