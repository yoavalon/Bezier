d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
