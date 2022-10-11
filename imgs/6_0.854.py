d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)

d.end()
