d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)

d.end()
