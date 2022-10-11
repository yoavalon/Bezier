d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.long)
d.position_pen(3,1)

d.end()
