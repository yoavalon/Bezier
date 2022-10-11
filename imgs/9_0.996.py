d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)

d.end()
