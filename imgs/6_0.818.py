d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)

d.end()
