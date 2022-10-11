d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,2)

d.end()
