d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.position_pen(1,0)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(0,3)

d.end()
