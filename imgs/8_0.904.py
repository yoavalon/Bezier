d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.S, Length.short)

d.end()
