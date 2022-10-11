d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(2,3)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)
d.position_pen(3,3)

d.end()
