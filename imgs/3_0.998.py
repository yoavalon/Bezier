d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.position_pen(2,2)

d.end()
