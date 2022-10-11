d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(0,2)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)

d.end()
