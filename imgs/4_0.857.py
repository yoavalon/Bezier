d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.long)

d.end()
