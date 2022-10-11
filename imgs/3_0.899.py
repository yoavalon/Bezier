d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(1,0)

d.end()
