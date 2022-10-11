d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)

d.end()
