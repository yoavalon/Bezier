d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.long)
d.position_pen(2,0)

d.end()
