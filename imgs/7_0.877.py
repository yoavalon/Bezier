d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
