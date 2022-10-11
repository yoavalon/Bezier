d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
