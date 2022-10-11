d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,0)
d.position_pen(0,1)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.position_pen(1,2)

d.end()
