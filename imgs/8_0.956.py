d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.position_pen(0,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(0,0)
d.position_pen(1,2)

d.end()
