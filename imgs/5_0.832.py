d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
