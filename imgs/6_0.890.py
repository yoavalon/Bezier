d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
