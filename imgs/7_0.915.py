d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,3)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)

d.end()
