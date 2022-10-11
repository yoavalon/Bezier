d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
