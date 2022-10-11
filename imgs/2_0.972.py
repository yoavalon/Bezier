d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.E, Length.medium)

d.end()
