d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
