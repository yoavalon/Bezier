d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.SW, Length.short)

d.end()
