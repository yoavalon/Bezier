d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,3)
d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)

d.end()
