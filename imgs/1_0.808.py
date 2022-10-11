d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.position_pen(0,0)
d.straight_line(Direction.NW, Length.medium)

d.end()
