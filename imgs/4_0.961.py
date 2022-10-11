d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(0,2)

d.end()
