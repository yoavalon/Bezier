d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)

d.end()
